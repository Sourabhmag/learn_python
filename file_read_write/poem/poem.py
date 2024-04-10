import re
from collections import Counter


def find_occurrences(data):
    split_data = re.split(r'\s+|\n', data)
    word_count = Counter(split_data)
    max_count: int = max(word_count.values())
    max_occurrence_words = [word for word, count in word_count.items() if count == max_count]
    print(max_occurrence_words, "=>", max_count)


with open("poem.txt", "r") as file:
    content = file.read()
    find_occurrences(content)
    # print(content)
