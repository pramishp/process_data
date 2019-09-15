import json

from process_data_vicaaya.Stream.TvStream import TvStream
from process_data_vicaaya.constants import mapper
from process_data_vicaaya.utils import map_dict_fields, dict_2_default_dict

path = r"D:\Codes\Vicaaya\vicaaya_spiders\datas.json"
with open(path, 'r') as file:
    json_str = file.read()
    stream_list = json.loads(json_str)

single_stream = dict_2_default_dict(map_dict_fields(stream_list[0], mapper))
tv_stream = TvStream(single_stream)
print(tv_stream.s_name)
print(tv_stream.poster)
print(tv_stream.site_id)
print(tv_stream.embed_link)
print(tv_stream.imdb_id)
print(tv_stream.get_release_year())
print(tv_stream.get_suggestions())
