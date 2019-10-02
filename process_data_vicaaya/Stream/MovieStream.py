from process_data_vicaaya import strip_strings, remove_empty_items
from process_data_vicaaya.Stream.BaseStream import BaseStream


class MovieStream(BaseStream):
    NAME_FORMATS = [
        "{title} {year}",
        "{title} {quality}",
        "{title} {year} {quality}",
        "{title} {quality} {year}"
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_display_title(self):
        if self.h_name and self.s_extracted_name:
            if len(self.h_name) > len(self.s_extracted_name) and not self.is_host_name_invalid():
                return self.h_name
        if self.s_name:
            return self.s_name
        return self.get_title()

    def get_titles(self):
        release_year = self.get_release_year()
        quality = self.get_quality()
        cleaned_s_name = self.get_cleaned_name(self.s_name)
        titles = []
        if self.s_name:
            titles.append(self.s_name)
        if self.h_name and not self.is_host_name_invalid():
            titles.append(self.h_name)
        if cleaned_s_name:
            titles.append(cleaned_s_name)
        for name_format in MovieStream.NAME_FORMATS:
            name = name_format.format(
                title=self.s_extracted_name if self.s_extracted_name else "",
                year=release_year if release_year else "",
                quality=quality if quality else ""
            )
            titles.append(name)
            if cleaned_s_name:
                cleaned_name = name_format.format(
                    title=cleaned_s_name if cleaned_s_name else "",
                    year=release_year if release_year else "",
                    quality=quality if quality else ""
                )
                titles.append(cleaned_name)
        stripped_titles = strip_strings(titles)
        stripped_titles = remove_empty_items(stripped_titles)

        return list(set(stripped_titles))
