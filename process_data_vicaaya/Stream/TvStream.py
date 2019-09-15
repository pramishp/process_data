from process_data_vicaaya.Stream.BaseStream import BaseStream
from process_data_vicaaya.utils import is_empty, parse_episode_from_name, get_episode_number_or_range_string


class TvStream(BaseStream):
    NAME_FORMATS = [
        "{title} s{season}e{episode}",
        "{title} s{season} e{episode}",
        "{title} season{season} serie{episode}",
        "{title} season {season} serie {episode}",
        "{title} episode {episode}",
        "{title} season {season} episode {episode}"
    ]

    NAME_FORMATS_NUMBERS = [
        "{title} s{season:0=2d}e{episode:0=2d}",
        "{title} s{season:0=2d} e{episode:0=2d}",
        "{title} s{season:0=1d} e{episode:0=1d}",
        "{title} s{season:0=1d}e{episode:0=1d}",
        "{title} season{season:0=2d} episode{episode:0=2d}",
        "{title} season{season:0=1d} episode{episode:0=1d}",
        "{title} season {season:0=2d} episode {episode:0=2d}",
        "{title} season {season:0=1d} episode {episode:0=1d}",
        "{title} {season:0=1d}x{episode:0=2d}",
        "{title} {season:0=2d}x{episode:0=2d}",
        "{title} {season:0=2d}x{episode:0=1d}",
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_display_title(self):
        s_e_no_host = parse_episode_from_name(self.h_name)
        if s_e_no_host["episode"] and s_e_no_host["season"]:
            return self.h_name
        if self.s_name:
            s_e_no = parse_episode_from_name(self.s_name)
            if s_e_no["episode"] and s_e_no["season"]:
                return self.s_name
        if s_e_no_host["episode"] or s_e_no_host["season"]:
            return self.h_name
        e_s = self.get_episode_season()
        episode = e_s["episode"]
        season = e_s["season"]
        title = self.s_extracted_name
        s_e_no_title = parse_episode_from_name(title)

        if not s_e_no_title["season"]:
            title = title + " season " + str(season)
        if not s_e_no_title["episode"]:
            episode = get_episode_number_or_range_string(episode)
            title = title + f" episode {episode}"
        return title

    def get_titles(self):
        e_s = self.get_episode_season()
        episode = get_episode_number_or_range_string(e_s["episode"])
        season = e_s["season"]
        cleaned_s_name = self.get_cleaned_name(self.s_name)
        titles = []
        if self.s_name:
            titles.append(self.s_name)
        if self.h_name:
            titles.append(self.h_name)
        if cleaned_s_name:
            titles.append(cleaned_s_name)
        if is_empty(season) or is_empty(episode):
            return titles

        name_formats = [*TvStream.NAME_FORMATS]
        if isinstance(episode, int):
            name_formats = [*name_formats, *TvStream.NAME_FORMATS_NUMBERS]

        for name_format in name_formats:
            try:
                name = name_format.format(
                    title=self.s_extracted_name if self.s_extracted_name else "",
                    episode=episode if episode else "",
                    season=season if season else ""
                )
                titles.append(name)
                if cleaned_s_name:
                    cleaned_name = name_format.format(
                        title=cleaned_s_name if cleaned_s_name else "",
                        episode=episode if episode else "",
                        season=season if season else ""
                    )
                    titles.append(cleaned_name)
            except:
                pass
        return titles
