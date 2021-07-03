"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

# global variable
lst = []
dic = []


def main():
	"""
	TODO: find all the vocabularies in the lst
	"""
	start = time.time()
	####################
	for i in range(1, 5):
		line = input(f"{i} row of letters: ")
		line = line.lower()
		if test_input(line) is False:
			print("Illegal input")
			line = None
			break
		else:
			lst.append(line)
	if len(lst) != 0:
		read_dictionary()
		ans = []
		for x in range(len(lst)):
			for y in range(0, len(lst[x]), 2):
				for z in range(4, 17):
					test_words(lst[x][y], x, y, [(x, y)], ans, [], z)
		print(f"There are {len(ans)} words in total.")
	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, "r", encoding="utf-8") as f:
		for line in f:
			a = line.strip()
			dic.append(a)


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dic:
		if word.startswith(sub_s) is True:
			return True


def test_input(line):
	"""
	:param line: (str) the input for finding words in dic
	:return: (bool) make sure the input corresponds to the format
	"""
	if 6 >= len(line) or len(line) > 9:
		return False
	for j in range(0, len(line), 2):
		if not line[j].isalpha() or len(line[j]) != 1:
			return False
	for k in range(1, len(line), 2):
		if line[k] != " ":
			return False


def test_words(current_word, x, y, tup, count, check_lst, length):
	if has_prefix(current_word) is True:
		if len(current_word) == length:
			if current_word in dic:
				if current_word not in check_lst:
					print(f"Print: {current_word}")
					count.append(1)
					check_lst.append(current_word)
		else:
			# for row to switch
			for i in range(-1, 2, 1):
				# for index in lst to switch
				for j in range(-2, 4, 2):
					# choose
					x = x + i
					y = y + j
					data = (x, y)
					if 0 <= x < len(lst):
						if 0 <= y < len(lst[x]):
							if data not in tup:
								tup.append(data)
								# explore
								test_words(current_word+lst[x][y], x, y, tup, count, check_lst, length)
								# un-choose
								tup.pop()
					x = x - i
					y = y - j


if __name__ == '__main__':
	main()
