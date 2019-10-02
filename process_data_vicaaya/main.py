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
    "_id": "5d67d637dee01c6e955038cc",
    "s_id": "cmovieshd.bz",
    "host_id": "streamango.com",
    "s_e_no": "season 1 episode 5-8",
    "embed_link": "https://streamango.com/embed/klcfoktadtsetabs?c1_file=https://sub.movie-series.net/taxing-love/taxing-love.vtt&c1_label=English",
    "s_name": "Taxing Love", "h_name": "movie_255274.mp4",
    "poster": "https://content.fruithosted.net/splash/klcfoktadtsetabs/efnnseofpmalkcnb.jpg",
    "stream_type": "movie", "stream_type_id": 0,
    "quality": "HD 720", "tags": ["hd 720"], "ads_frequency": 0, "views": 0,
    "site_link": "https://www7.cmovieshd.bz/film/taxing-love/watching.html?ep=0",
    "created_at": "2019-08-29 19:27:14",
    "scrapy-mongodb": {"ts": "2019-08-29T13:42:15.609Z"}
}

single_movie = dict_2_default_dict(map_dict_fields(single_data, mapper))
# single_stream = dict_2_default_dict(map_dict_fields(stream_list[0], mapper))
# tv_stream = MovieStream(single_stream)
movie_stream = TvStream(single_movie)
print(json.dumps(movie_stream.get_suggestions()))
