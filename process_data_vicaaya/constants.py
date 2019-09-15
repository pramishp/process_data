stream_types = {
    "movie": 0,
    "movies": 0,
    "tv-show": 1,
    "tv-shows": 1,
}

mapper = {
    's_i_type': 'stream_type',
    "s_id": "site_id",
    "s_i_id": "site_item_id",
    "s_i_title": "s_name",
    "created_date": "created_at",
    "h_i_poster": "poster",
    "i_id": "imdb_id",
    "s_i_link": "site_link",
    "s_i_images": "site_images",
    "h_i_title": "h_name",
    "s_i_quality": "quality",
    "s_e_no": "s_e_no"
}

NAME_CLEANER_PATTERNS = [
    r"Watch\s(.*)\sOnline$",
    r"Watch (.*) Full Movie Online Free"
]
