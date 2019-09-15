from process_data_vicaaya.Stream.BaseStream import BaseStream


class MovieStream(BaseStream):
    NAME_FORMATS = [
        "{title} {year}",
        "{title} {quality}"
        "{title} {year} {quality}",
        "{title} {quality} {year}"
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_titles(self):
        release_year = self.get_release_year()
        quality = self.get_quality()
        cleaned_s_name = self.get_cleaned_name(self.s_name)
        titles = [self.s_name, self.h_name]
        if cleaned_s_name:
            titles.append(cleaned_s_name)
        for name_format in MovieStream.NAME_FORMATS:
            name = name_format.format(
                title=self.s_name if self.s_name else "",
                year=release_year if release_year else "",
                quality=quality if quality else ""
            )
            titles.append(name)
            if cleaned_s_name:
                cleaned_name = name_format.format(
                    title=self.s_name if self.s_name else "",
                    year=release_year if release_year else "",
                    quality=quality if quality else ""
                )
                titles.append(cleaned_name)
        return titles


