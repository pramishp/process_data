import json

from process_data_vicaaya.Stream.MovieStream import MovieStream
from process_data_vicaaya.Stream.TvStream import TvStream
from process_data_vicaaya.constants import mapper
from process_data_vicaaya.utils import dict_2_default_dict, map_dict_fields

#
# path = r"D:\Codes\Vicaaya\vicaaya_spiders\datas.json"
# with open(path, 'r') as file:
#     json_str = file.read()
#     stream_list = json.loads(json_str)

single_data = {
    "unique_key": "2f310e7a-2a9c-5604-839b-f3668b7da32e",
    "s_id": "cmovies.video",
    "host_id": "gcloud.live",
    "embed_link": "https://gcloud.live/v/4lv0yklwxoq",
    "search_titles": [
        "City Hunter",
        "Video city-hunter-episode-19-a-beach-to-remember-an-audition-full-of-danger.mp4",
        "City Hunter"
    ],
    "completion_suggestions": {
        "input": [
            "Video city hunter episode 19 a beach to remember",
            "Video city hunter episode 19 a",
            "Video city hunter episode 19",
            "Video city",
            "City",
            "Video city hunter episode",
            "Video city hunter episode 19 a beach to remember an audition full of danger",
            "Video city hunter episode 19 a beach",
            "City Hunter",
            "Video city hunter episode 19 a beach to remember an audition",
            "Video city hunter episode 19 a beach to remember an",
            "Video city hunter episode 19 a beach to remember an audition full of danger mp4",
            "Video city hunter episode 19 a beach to remember an audition full of",
            "Video",
            "Video city hunter episode 19 a beach to remember an audition full",
            "Video city hunter episode 19 a beach to",
            "Video city hunter"
        ]
    },
    "title": "City Hunter season None episode",
    "s_name": "City Hunter",
    "h_name": "Video city-hunter-episode-19-a-beach-to-remember-an-audition-full-of-danger.mp4",
    "poster": "https://cdn.watch-series.co/cover/city-hunter-large.png",
    "stream_type": "tv-show",
    "stream_type_id": 1,
    "imdb_id": "_None_",
    "s_e_no": {
        "season": None,
        "episode": None
    },
    "episode_in_range": False,
    "quality": "_None_",
    "tags": [],
    "ads_frequency": 0,
    "views": 0,
    "report_count": 0,
    "reported": False,
    "report_verified": False,
    "site_link": "https://www.cmovies.video/film/city-hunter/watching.html?ep=19",
    "created_at": "2019-10-02 21:11:28"
}

single_movie = dict_2_default_dict(map_dict_fields(single_data, mapper))
# single_stream = dict_2_default_dict(map_dict_fields(stream_list[0], mapper))
# tv_stream = MovieStream(single_stream)
movie_stream = TvStream(single_movie)
print(json.dumps(movie_stream.get_display_title()))
