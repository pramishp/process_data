from process_data_vicaaya.Stream.BaseStream import BaseStream
from process_data_vicaaya.utils import is_empty


class TvStream(BaseStream):
    NAME_FORMATS = [
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
        "{title} s{season}e{episode}",
        "{title} season{season} serie{episode}",
        "{title} season {season} serie {episode}",
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_titles(self):
        e_s = self.get_episode_season()
        episode = e_s["episode"]
        season = e_s["season"]
        cleaned_s_name = self.get_cleaned_name(self.s_name)
        titles = [self.s_name, self.h_name]
        if cleaned_s_name:
            titles.append(cleaned_s_name)
        if is_empty(episode) or is_empty(episode):
            return titles

        for name_format in TvStream.NAME_FORMATS:
            name = name_format.format(
                title=self.s_name if self.s_name else "",
                episode=int(episode) if episode else "",
                season=int(season) if season else ""
            )
            titles.append(name)
            if cleaned_s_name:
                cleaned_name = name_format.format(
                    title=self.s_name if self.s_name else "",
                    episode=int(episode) if episode else "",
                    season=int(season) if season else ""
                )
                titles.append(cleaned_name)
        return titles
