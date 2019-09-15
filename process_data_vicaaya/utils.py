import re
from collections import defaultdict


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
    if data.strip() == "":
        return True
    if data is None:
        return True
    if data is False:
        return True
    return False
