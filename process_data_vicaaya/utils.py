import re
from collections import defaultdict

import PTN
import anitopy


def map_dict_fields(dict_a, mapper):
    new_item = {}
    for key in dict_a.keys():
        if mapper.__contains__(key):
            new_item[mapper[key]] = dict_a[key]
        else:
            new_item[key] = dict_a[key]
    return new_item


def get_matching_pattern(patterns, text):
    matcher = lambda pattern: len(re.findall(pattern, text)) > 0
    matches = list(map(matcher, patterns))
    try:
        single_match_index = matches.index(True)
        return patterns[single_match_index]
    except ValueError as e:
        return None


def dict_2_default_dict(original_dict, dtype=bool):
    new_dict = defaultdict(dtype)
    for key in original_dict:
        new_dict[key] = original_dict[key]
    return new_dict


def make_num_2_digits(number):
    return "%02d" % int(number)


def make_num_1_digit(number):
    return "%1d" % int(number)


def is_empty(data):
    if data is None:
        return True
    if isinstance(data, str) and data.strip() == "":
        return True
    if isinstance(data, list) and len(data) == 0:
        return True
    if data is False:
        return True
    return False


def parse_episode_from_name(name):
    episode, season = None, None
    if name and not is_empty(name) and isinstance(name, str):
        try:
            info = dict_2_default_dict(anitopy.parse(name))
            episode = info["episode_number"]
            season = info["anime_season"]
        except:
            print("anitopy error")
            pass
        if not episode or not season:
            ptn_info = dict_2_default_dict(PTN.parse(name))
            episode = ptn_info["episode"] if not episode else episode
            season = ptn_info["season"] if not season else season
        try:
            return {"episode": parse_episode(episode) if episode else None,
                    "season": get_number_from_string(season) if season else None}
        except ValueError or AttributeError:
            return {"episode": None, 'season': None}
    return {"episode": None, 'season': None}


def get_episode_number_or_range_string(episode):
    if isinstance(episode, int):
        return episode
    elif isinstance(episode, str):
        return get_number_from_string(episode)
    elif isinstance(episode, list):
        assert len(episode) == 2
        return f"{episode[0]}-{episode[1]}"
    else:
        return ""


def parse_episode(text):
    if text is None:
        return None
    if isinstance(text, int):
        return text
    if isinstance(text, str):
        return get_number_from_string(text)
    elif isinstance(text, list) and len(text) == 2:
        return text
    else:
        raise Exception("episode not in list format or string format : ", text)


def get_title_from_name(name):
    if not is_empty(name) and isinstance(name, str):
        try:
            info = dict_2_default_dict(anitopy.parse(name))
            extracted_name = info["anime_title"]
            if extracted_name:
                return extracted_name
            ptn_info = dict_2_default_dict(PTN.parse(name))
            if ptn_info["title"]:
                return ptn_info["title"]
            return None
        except TypeError:
            return None
    return None


def get_domain_from_url(url):
    if not is_string(url):
        return None
    pattern = r"^(?:https?:\/\/)?(?:[^@\n]+@)?(?:www\.)?([^:\/\n?]+)"
    matched = re.findall(pattern, url)
    if not is_empty(matched):
        # check if whitelisted
        from process_data_vicaaya import DOMAIN_NAMES_WHITELIST
        domain_white_list = list(filter(lambda domain: domain in matched, DOMAIN_NAMES_WHITELIST))
        if len(domain_white_list) > 0:
            return domain_white_list[0]

        splited_match = matched[0].split(".")
        if len(splited_match) > 2:
            return '.'.join(splited_match[1:])
        return matched[0]
    return None


def is_string(string):
    if not string: return False
    if isinstance(string, str):  return True
    return False


def get_number_from_string(text):
    if is_empty(text) and not isinstance(text, str):
        return None
    number = None
    try:
        number = int(float(text))
        return number
    except:
        pass
    pattern = r"\d+"
    number_list = re.findall(pattern, text)
    if not is_empty(number_list):
        try:
            number = int(float(number_list[0]))
        except:
            pass
    return number


def shingle_transform(text, min_shingle=2, max_shingle=3, split_by=" "):
    word_list = text.split(split_by)
    if len(word_list) == 0:
        raise Exception('Invalid text')
    if min_shingle > len(word_list):
        return word_list

    list_of_shingles_list = []
    for w in range(min_shingle, max_shingle + 1):
        list_of_shingles_list.append([' '.join(word_list[i:i + w]) for i in range(len(word_list) - w + 1)])
    final_list = [shingle for shingles in list_of_shingles_list for shingle in shingles]
    return final_list
