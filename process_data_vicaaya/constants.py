NULL_KEY = "_NULL_"

stream_types_2_id = {
    "movie": 0,
    "movies": 0,
    "tv-show": 1,
    "tv-shows": 1,
    "anime": 2,
    "animes": 2,
    "anime-movie": 3,
    "anime-movies": 3
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
    "s_e_no": "s_e_no"
}

NAME_CLEANER_PATTERNS = [
    r"Watch\s(.*)\sOnline",
    r"Watch (.*) Full Movie Online Free",

]

HOST_NAME_EXCEPTION_PATTERNS = [
    r"movie_[0-9]+\.mp4"
]

DOMAIN_NAMES_WHITELIST = [
    "watchonlinemovies.com.pk"
]


HOST_ADS_FREQUENCY = {
    "idtbox.com": 8,
    "vidlox.tv": 6,
    "vidlox.me": 6,
    "vshare.eu": 4,
    "clipwatching.com": 10, # ads blocker not allowed
    "openload.co": 15, # (openload.vip) offensive ads - no ads with adblocker
    "loadvid.online": 6,
    "oload.life": 15,
    "streamango.com": 6,
    "vidlocker.xyz": 0,
    "vidcloud.co": 4
}