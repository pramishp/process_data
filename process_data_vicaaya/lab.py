import copy
import re

from process_data_vicaaya import NULL_KEY, remove_empty_items


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

print(remove_empty_items(["a", "  "]))