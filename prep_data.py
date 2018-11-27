#!/usr/bin/env python3

import glob
import gensim

all_files = glob.glob('data/DUC2001/Summaries/*.txt')

def read_input(input_file):
    with open(input_file,'rt') as f:
        for line in f:
            yield gensim.utils.simple_preprocess(line)

documents2 = []
for _ in range(len(all_files)):
    documents1 = []
    documents = list(read_input('{}'.format(all_files[_])))
    for __ in range(len(documents)):
        for ___ in range(len(documents[__])):
            documents1.append(documents[__][___])

    for __ in range(len(documents1)):
        if documents1[__] == 'introduction':
            documents2.append(documents1[__+1:])

with open('list_word.txt','w') as file:
    file.write('{}'.format(documents2))

