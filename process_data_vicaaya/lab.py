import copy
import re
from newsplease import NewsPlease

from process_data_vicaaya import NULL_KEY, remove_empty_items
from elasticsearch import Elasticsearch


def normalizer(text):
    things_2_keep = r"[a-zA-Z0-9]+"
    normalized_text = re.findall(things_2_keep, text)
    if normalized_text:
        return ' '.join(normalized_text)
    return None


def concat_list(word_list, index=0, sentence="", sentences=None):
    if sentences is None:
        sentences = []
    sentence += word_list[index] + " "
    sentences.append(sentence.strip())
    if len(word_list) == index + 1: return sentences
    index += 1
    return concat_list(word_list, index, sentence, sentences)


def suggestion_transform(text, split_by=" "):
    normalized_text = normalizer(text)
    word_list = normalized_text.split(split_by)
    # word_list = list(filter(lambda x: x.strip() != "", word_list))
    suggestion_list = concat_list(word_list)
    return suggestion_list


suggestions = suggestion_transform("Taxing Love")

# print(remove_empty_items(["a", "  "]))

from ssl import create_default_context


# es = Elasticsearch(
#     ['167.86.85.184'],
#     http_auth=('elastic', 'elasticsearch'),
#     scheme='http',
#     port=9200
# )


# print(es.ping())

def calculate_simultaneous_connection(page_load_time, number_of_cores):
    """

    :param page_load_time:  in seconds
    :param number_of_cores:
    :return:
    """
    return number_of_cores / page_load_time


def calculate_simultaneous_user(clicks_per_minute, page_load_time, num_cores):

    return clicks_per_minute * calculate_simultaneous_connection(page_load_time, num_cores)


number_of_cores = 4
page_load_time = 0.1  # in seconds
click_per_minute = 40
print(f"{calculate_simultaneous_connection(page_load_time, number_of_cores)} connection simultaneously")
# print(f"{calculate_simultaneous_user(click_per_minute, page_load_time, number_of_cores)} users simultaneously")
