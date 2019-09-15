import re
from datetime import datetime
from abc import ABC, abstractmethod
import PTN
import anitopy
from process_data_vicaaya.constants import NAME_CLEANER_PATTERNS
from process_data_vicaaya.utils import get_matching_pattern, dict_2_default_dict


class BaseStream(ABC):
    IMDB_ID_PATTERN = r"tt[0-9]+"
    DATE_TIME_FORMATS = ["%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M:%S.%f"]
    NAME_CLEANER_PATTERNS = NAME_CLEANER_PATTERNS

    def __init__(self, data):
        self.host_id = data['host_id']
        self.embed_link = data['embed_link']
        self.poster = data['poster'] if data['poster'] else None
        self.h_name = data['h_name'] if data['h_name'] else None

        self.site_id = data['site_id']
        self.site_item_id = data['site_item_id']
        self.s_name = data['s_name']
        self.s_e_no = data['s_e_no'] if data['s_e_no'] else None
        self.quality = data['quality']
        self.stream_type = data['stream_type']
        self.site_link = data['site_link']
        self.release_date = data['release_date'] if data['release_date'] else None
        self.site_images = data['site_images']
        self.imdb_id = data['imdb_id'] if self.check_imdb_id(data['imdb_id']) else None

        self.h_info = self.parse_info_from_name(self.h_name)
        self.s_info = self.parse_info_from_name(self.s_name)

        self.created_at = data['created_at'] if data['created_at'] else datetime.now()

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

    def get_cleaned_name(self, name):
        matched_pattern = get_matching_pattern(BaseStream.NAME_CLEANER_PATTERNS, name)
        if matched_pattern:
            return re.findall(matched_pattern, name)[0]
        return None

    def parse_info_from_name(self, name):
        if name:
            info = dict_2_default_dict(PTN.parse(name))
            year = info['year'] if info['year'] else None
            title = info['title'] if info['title'] else None
            quality = info['quality'] if info['quality'] else None
            return dict_2_default_dict({**info, "year": year, "title": title, "quality": quality})
        return dict_2_default_dict({"year": None, "title": None, "quality": None})

    def parse_episode_from_name(self, name):
        info = dict_2_default_dict(anitopy.parse(name))
        episode = info["episode_number"] if info["episode_number"] else None
        season = info["anime_season"] if info["anime_season"] else None
        return {"episode": episode, "season": season}

    def get_episode_season(self):
        if self.s_e_no:
            return self.parse_episode_from_name(self.s_e_no)
        s_e_from_host = self.parse_episode_from_name(self.h_name)
        return s_e_from_host

    def get_release_year(self):
        released_year = self.release_date
        if released_year:
            return released_year
        released_year = self.s_info["year"]
        if not released_year:
            released_year = self.h_info['year']
        return released_year

    def get_quality(self):
        if self.quality:
            return self.quality
        quality = self.s_info["quality"]
        if not quality:
            quality = self.h_info["quality"]
        return quality

    def get_resolution(self):
        h_info = self.h_info["resolution"] if self.h_info["resolution"] else None
        return h_info

    def get_tags(self):
        quality = self.get_quality()
        resolution = self.get_resolution()
        tags = []
        if quality:
            tags.append(quality.lower())
        if resolution:
            tags.append(resolution.lower())
        return tags

    @abstractmethod
    def get_titles(self):
        pass

    def get_suggestions(self):
        return self.get_titles()
