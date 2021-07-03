"""
File: anagram.py
Name: Tony
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time  # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'  # This is the filename of an English dictionary
EXIT = '-1'  # Controls when to stop the loop

# global variable
dic = []
lst = []


def main():
    """
    TODO: find the word you are looking for in the dictionary
    """
    print("Welcome to stanCode \"Anagram Generator\" (or -1 to quit)")
    s = input("Find anagrams for: ")
    start = time.time()
    read_dictionary()
    find_anagrams(s)
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end - start} seconds.')


def read_dictionary():
    with open(FILE, "r", encoding="utf-8") as f:
        for line in f:
            a = line.strip()
            dic.append(a)


def find_anagrams(s):
    """
    :param s: the word you are looking for
    :return: all the words that include each letter in "s"
    """
    if s == -1:
        return
    else:
        s = s.lower()
        find_anagrams_helper(s, "", [])
    if len(lst) == 0:
        return
    else:
        print("Searching.....")
        print(f"{len(lst)} anagrams: {lst}")


def find_anagrams_helper(s, current_s, check_lst):
    if len(current_s) == len(s) and current_s not in lst:
        if has_prefix(sub_s=current_s[0:2]) is True:
            if current_s in dic:
                lst.append(current_s)
                print("Searching.....")
                print("Found:  ", current_s)
    else:
        for i in range(len(s)):
            if i not in check_lst:
                # choose
                check_lst.append(i)
                # explore
                find_anagrams_helper(s, current_s+s[i], check_lst)
                # un-choose
                check_lst.pop()


def has_prefix(sub_s):
    """
    :param sub_s: the word "sub_s" doesn't exist, which means that if this word comes out, it should return False
    :return: True or False
    """
    for word in dic:
        if word.startswith(sub_s) is True:
            return True


if __name__ == '__main__':
    main()
