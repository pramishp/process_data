import re
import uuid
from abc import ABC, abstractmethod
from datetime import datetime

import PTN
from process_data_vicaaya import get_matching_pattern, HOST_NAME_EXCEPTION_PATTERNS

from process_data_vicaaya.constants import stream_types_2_id, NAME_CLEANER_PATTERNS
from process_data_vicaaya.utils import dict_2_default_dict, get_domain_from_url, \
    parse_episode_from_name, get_title_from_name, get_episode_number_or_range_string, suggestion_transform, \
    none_to_null_transform, is_empty, clean_title


class BaseStream(ABC):
    IMDB_ID_PATTERN = r"tt[0-9]+"
    DATE_TIME_FORMATS = ["%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M:%S.%f"]
    NAME_CLEANER_PATTERNS = NAME_CLEANER_PATTERNS

    def __init__(self, data):
        self.embed_link = data['embed_link']
        self.host_id = self.get_host_id()
        self.poster = data['poster'] if data['poster'] else None
        self.h_name = data['h_name'] if data['h_name'] else None

        self.site_link = data['site_link']
        self.site_id = self.get_site_id()
        self.site_item_id = data['site_item_id']
        self.s_name = data['s_name'] if data['s_name'] else data["title"]
        self.s_e_no = data['s_e_no'] if data['s_e_no'] else None

        # qualities
        self.quality = data['s_i_quality'] if data['s_i_quality'] else None
        self.site_all_quality = data["s_a_quality"] if data["s_a_quality"] else None
        self.h_i_quality = data['h_i_quality'] if data['h_i_quality'] else None

        # size
        self.size = data['h_i_size'] if data['h_i_size'] else None

        # if 'tags' is available
        self.tags = data["tags"] if data["tags"] else []

        self.stream_type = data['stream_type']
        self.stream_type_id = stream_types_2_id[data['stream_type']]
        self.release_date = data['release_date'] if data['release_date'] else None
        self.site_images = data['site_images']
        self.imdb_id = data['imdb_id'] if self.check_imdb_id(data['imdb_id']) else None
        self.h_info = self.parse_info_from_name(self.h_name)
        self.s_info = self.parse_info_from_name(self.s_name)
        self.s_extracted_name = self.get_title()
        self.created_at = data['created_at'] if data['created_at'] else datetime.now()

    def get_poster(self):
        if self.poster:
            if isinstance(self.poster, list) and len(self.poster) > 0:
                return self.poster[0]
            if not is_empty(self.poster):
                return self.poster
        return None

    def check_imdb_id(self, imdb_id):
        if not imdb_id:
            return None
        return len(re.findall(BaseStream.IMDB_ID_PATTERN, imdb_id)) != 0

    def get_datetime_obj(self):
        if isinstance(self.created_at, datetime):
            return self.created_at
        datetime_obj = None
        for date_format in BaseStream.DATE_TIME_FORMATS:
            try:
                datetime_obj = datetime.strptime(self.created_at, date_format)
                break
            except ValueError as e:
                pass

        if datetime_obj is None:
            raise Exception("couldn't match datetime format")
        return datetime_obj

    def is_host_name_invalid(self):
        host_name_exception_matched_pattern = get_matching_pattern(HOST_NAME_EXCEPTION_PATTERNS, self.h_name)
        if host_name_exception_matched_pattern:
            return True
        return False

    def get_cleaned_name(self, name):
        """
         if is_empty(name):
            return None
        matched_pattern = get_matching_pattern(BaseStream.NAME_CLEANER_PATTERNS, name)
        if matched_pattern:
            return re.findall(matched_pattern, name)[0]
        return None
        """
        # better to use get title
        return self.get_title()

    def get_title(self):
        s_title = self.s_info["title"]
        if s_title:
            return s_title
        h_title = self.h_info["title"]
        if h_title:
            return h_title
        if self.h_name:
            return self.h_name
        return self.s_name

    @abstractmethod
    def get_display_title(self):

        return self.get_title().strip()

    def parse_info_from_name(self, name):
        if name:
            info = dict_2_default_dict(PTN.parse(name))
            year = info['year'] if info['year'] else None
            title = get_title_from_name(name)
            quality = info['quality'] if info['quality'] else None
            return dict_2_default_dict({**info, "year": year, "title": title, "quality": quality})
        return dict_2_default_dict({"year": None, "title": None, "quality": None})

    def get_episode_season(self):
        if isinstance(self.s_e_no, dict) and (self.s_e_no["season"] or self.s_e_no["episode"]):
            return self.s_e_no
        if self.s_e_no and len(self.s_e_no) > 2:
            s_e = parse_episode_from_name(self.s_e_no)
            if s_e["season"] and s_e["episode"]:
                return s_e
        s_e_from_host = parse_episode_from_name(self.h_name)
        return s_e_from_host

    def get_release_year(self):
        released_year = self.release_date
        if released_year:
            return released_year
        released_year = self.s_info["year"]
        if not released_year:
            released_year = self.h_info['year']
        try:
            released_year = int(released_year)
            return str(released_year)
        except:
            return None

    def get_quality(self):
        if self.quality:
            return self.quality
        if self.site_all_quality:
            return self.site_all_quality
        if self.h_i_quality:
            return self.h_i_quality

        quality = self.s_info["quality"]
        if not quality:
            quality = self.h_info["quality"]
        return quality

    def get_size(self):
        if self.size:
            return self.size
        if self.s_info["size"]:
            return self.s_info["size"]
        if self.h_info["size"]:
            return self.h_info["size"]
        return None

    def get_resolution(self):
        h_info = self.h_info["resolution"] if self.h_info["resolution"] else None
        return h_info

    def get_tags(self):
        quality = self.get_quality()
        resolution = self.get_resolution()
        size = self.get_size()
        item_type = self.stream_type
        if quality:
            self.tags.append(quality.lower())
        if resolution:
            self.tags.append(resolution.lower())
        # if size:
        #     tags.append(size.lower())
        if item_type and "anime" in item_type:
            self.tags.append(item_type.lower())

        # keeps only the alphanumeric characters
        self.tags = list(map(lambda x: re.sub(r"\W+", "", x), self.tags))
        return self.tags

    def get_id(self):
        _id = uuid.uuid5(uuid.NAMESPACE_URL, self.embed_link)
        return str(_id)

    def get_ads_frequency(self):
        return 0

    @abstractmethod
    def get_titles(self):
        return []

    def get_suggestions(self):
        suggestions = []
        for title in self.get_titles():
            shingles = suggestion_transform(title.strip())
            suggestions = [*suggestions, *shingles]
        return list(set(suggestions))

    def get_host_id(self):
        if self.embed_link:
            result = get_domain_from_url(self.embed_link)
            if result:
                return result
            else:
                raise Exception("Cant extract host id from embed link")
        raise Exception("No embed link")

    def get_site_id(self):
        if self.site_link:
            result = get_domain_from_url(self.site_link)
            if result:
                return result
            else:
                raise Exception("Cant extract site id from site link")
        raise Exception("No site link")

    def get_data(self):
        s_e_no = self.get_episode_season()
        episode_in_range = False
        # episode
        episode = s_e_no["episode"]
        if isinstance(episode, list):
            episode_in_range = True
        episode = get_episode_number_or_range_string(episode)
        episode = str(episode) if episode else None
        # season
        season = s_e_no["season"]
        season = str(season) if season else None

        final_dict = {
            "unique_key": self.get_id(),
            "s_id": self.site_id,
            "host_id": self.host_id,
            "embed_link": self.embed_link,
            "search_titles": self.get_titles(),
            "completion_suggestions": {"input": self.get_suggestions()},
            "title": clean_title(self.get_display_title()),
            "s_name": self.s_name,
            "h_name": self.h_name,
            "poster": self.get_poster(),
            "stream_type": self.stream_type,
            "stream_type_id": self.stream_type_id,
            "imdb_id": self.imdb_id,
            "s_e_no": {"season": season, "episode": episode},
            "episode_in_range": episode_in_range,
            "quality": self.get_quality(),
            "tags": self.get_tags(),
            "ads_frequency": self.get_ads_frequency(),
            "views": 0,
            "report_count": 0,
            "reported": False,
            "report_verified": False,
            "site_link": self.site_link,
            "created_at": self.get_datetime_obj().strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at": self.get_datetime_obj().strftime("%Y-%m-%d %H:%M:%S")
        }

        return none_to_null_transform(final_dict)
