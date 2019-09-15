import collections
import json

from process_data_vicaaya.Stream.MovieStream import MovieStream
from process_data_vicaaya.Stream.TvStream import TvStream
from process_data_vicaaya.utils import dict_2_default_dict


path = r"D:\Codes\Vicaaya\vicaaya_spiders\datas.json"
with open(path, 'r') as file:
    json_str = file.read()
    stream_list = json.loads(json_str)

hosts = []
for stream in stream_list:
    if stream["s_i_type"] == "movie":
        s = MovieStream(dict_2_default_dict(stream))
    else:
        s = TvStream(dict_2_default_dict(stream))
    hosts.append(s.host_id)

print(collections.Counter(hosts))
