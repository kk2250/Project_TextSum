#!/usr/bin/env python3

import spacy
import glob

nlp = spacy.load('en')


all_files = glob.glob("data/DUC2001/Summaries/*.txt")

word_dict = []
word_count = {}

for _ in range(len(all_files)):
    with open(all_files[_],'rt') as dd:
        txt_file = nlp(dd.read())
        for word in txt_file:
            if word.text not in word_count:
                word_count.update({word.text:1})
            else:
                word_count[word.text] += 1
            if word.text not in word_dict:
                word_dict.append(word.text)

with open("dictionary.txt", "w") as dictionary:
    dictionary.write("{}".format(word_dict))

with open("dictionary_count.txt", "w") as dictionary1:
    dictionary1.write("{}".format(word_count))

aff

#if __name__ == '__main__':
#   print(word_dict)
