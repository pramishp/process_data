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

single_data = {"_id": "5d809423dee01c6e956a2528", "s_id": "vumoo.life", "host_id": "gomostream.com",
     "embed_link": "https://gomostream.com/show/a-place-to-call-home/01-03",
     "search_titles": ["A Place To Call Home - PutStream", "A Place To Call Home - PutStream",
                       "A Place To Call Home - PutStream s1e3", "A Place To Call Home - PutStream s1e3",
                       "A Place To Call Home - PutStream s1 e3", "A Place To Call Home - PutStream s1 e3",
                       "A Place To Call Home - PutStream season1 serie3",
                       "A Place To Call Home - PutStream season1 serie3",
                       "A Place To Call Home - PutStream season 1 serie 3",
                       "A Place To Call Home - PutStream season 1 serie 3",
                       "A Place To Call Home - PutStream episode 3", "A Place To Call Home - PutStream episode 3",
                       "A Place To Call Home - PutStream season 1 episode 3",
                       "A Place To Call Home - PutStream season 1 episode 3", "A Place To Call Home - PutStream s01e03",
                       "A Place To Call Home - PutStream s01e03", "A Place To Call Home - PutStream s01 e03",
                       "A Place To Call Home - PutStream s01 e03", "A Place To Call Home - PutStream s1 e3",
                       "A Place To Call Home - PutStream s1 e3", "A Place To Call Home - PutStream s1e3",
                       "A Place To Call Home - PutStream s1e3", "A Place To Call Home - PutStream season01 episode03",
                       "A Place To Call Home - PutStream season01 episode03",
                       "A Place To Call Home - PutStream season1 episode3",
                       "A Place To Call Home - PutStream season1 episode3",
                       "A Place To Call Home - PutStream season 01 episode 03",
                       "A Place To Call Home - PutStream season 01 episode 03",
                       "A Place To Call Home - PutStream season 1 episode 3",
                       "A Place To Call Home - PutStream season 1 episode 3", "A Place To Call Home - PutStream 1x03",
                       "A Place To Call Home - PutStream 1x03", "A Place To Call Home - PutStream 01x03",
                       "A Place To Call Home - PutStream 01x03", "A Place To Call Home - PutStream 01x3",
                       "A Place To Call Home - PutStream 01x3"],
     "title": "A Place To Call Home - PutStream season 1 episode 3", "h_name": "A Place To Call Home - PutStream",
     "stream_type": "tv-shows", "stream_type_id": 1, "s_e_no": {"season": "1", "episode": "3"},
     "episode_in_range": False, "tags": [], "ads_frequency": 0, "views": 0,
     "site_link": "https://vumoo.life/episodes/a-place-to-call-home-1x3/", "created_at": "2019-09-20 02:48:10",
     "scrapy-mongodb": {"ts": "2019-09-19T21:04:00.112Z"}}


single_movie = dict_2_default_dict(map_dict_fields(single_data, mapper))
# single_stream = dict_2_default_dict(map_dict_fields(stream_list[0], mapper))
# tv_stream = MovieStream(single_stream)
movie_stream = TvStream(single_movie)
print(json.dumps(movie_stream.get_poster()))
