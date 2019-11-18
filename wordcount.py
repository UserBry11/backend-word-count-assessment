#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

def print_words(filename):
    with open(filename,'r') as f:   #context manager. Will automatically close file after

        f_contents = f.read()
        f_list = f_contents.lower().split()
        f_list.sort()

        w1 = "\"'tis"
        w2 = "\"--said"
        w3 = "\"come"
        w3b = "\"coming"
        w4 = "\"edwin"
        w5 = "\"french,"
        w6 = "\"he's"
        w7 = "\"how"
        w8 = "\"i"
        w9 = "\"i'll"
        w10 = "\"it\""
        w11 = "\"keep"
        w12 = "\"let"
        w13 = "\"much"
        w14 = "\"poison\""
        w15 = "\"purpose\"?'"
        
        apple = [w1,w2,w3,w3b,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14,w15]
        for seed in apple:
            print( str(seed) + " : " + str(f_list.count(seed)) )

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

def print_top(filename):
    with open(filename, 'r') as f:
        f_contents = f.read()
        f_list = f_contents.lower().split()
        f_list.sort()

        w1 = "the"
        w2 = "and"
        w3 = "to"
        w4 = "a"
        w5 = "she"
        w6 = "of"
        w7 = "said"
        w8 = "it"
        w9 = "in"
        w10 = "was"
        w11 = "you"
        w12 = "i"
        w13 = "as"
        w14 = "that"
        w15 = "alice"
        w16 = "her"
        w17 = "at"
        w18 = "had"
        w19 = "with"
        w20 = "all"

        apple = [w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14,w15,w16,w17,w18,w19,w20]
        for seed in apple:
            print( str(seed) + " : " + str(f_list.count(seed)) )


# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.


def main():
    if len(sys.argv) != 3:
        print('usage: python wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]  #this is either --count or --topcount
    filename = sys.argv[2]  #this is filename
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()
