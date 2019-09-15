import datetime
import re

import PTN
import anitopy
import copy
# from searchengine.data_post_processing import get_domain_from_url, get_number_from_string

pattern = r"^(?:https?:\/\/)?(?:[^@\n]+@)?(?:www\.)?([^:\/\n?]+)"
text = r"https://www3.googlevideo.com/videoplayback?id=3483b202494dde45&itag=22&source=picasa&begin=0&requiressl=yes&mm=30&mn=sn-25ge7nse&ms=nxu&mv=m&pl=20&sc=yes&ttl=transient&ei=I1qdXLiXHYW8hAfo7K-oBA&susc=ph&app=fife&mime=video/mp4&cnr=14&dur=7435.122&lmt=1552141631034970&mt=1553816013&ipbits=0&cms_redirect=yes&keepalive=yes&ratebypass=yes&ip=51.15.88.50&expire=1553823299&sparams=ip,ipbits,expire,id,itag,source,requiressl,mm,mn,ms,mv,pl,sc,ttl,ei,susc,app,mime,cnr,dur,lmt&signature=CF84CD4E96BAF9B112AF57C224566090DBB7E820F8B79026E6C79C8D72E6393B.16663899069D7A1EC0E1102B0ED0CA4A23BB8D9ADFF0EDFFCEED73D23443AFB1&key=us0"
url = "wwe.watchonlinemovies.com.pk/embed/adsf"


# print(get_domain_from_url(url))
def shingle_transform(text, min=2, max=3, split_by=" "):
    word_list = text.split(split_by)
    if len(word_list) == 0:
        raise Exception('Invalid text')
    if min > len(word_list):
        return word_list

    list_of_shingles_list = []
    for w in range(min, max + 1):
        list_of_shingles_list.append([' '.join(word_list[i:i + w]) for i in range(len(word_list) - w + 1)])
    final_list = [shingle for shingles in list_of_shingles_list for shingle in shingles]
    return final_list


result = anitopy.parse("Season 1 Episode 5-8")
ptn_result = PTN.parse("Season 1 Episode 5-8")
item = {"a": 2}
s_item = copy.deepcopy(item)
item["a"] = 3
print(s_item)