######################################################
# Functions for various string manipulation methods. #
#                                                    #
# Written by Lewis Kim.                              #
######################################################


"""Remove all duplicate characters from any arbitrary STRING.
The returned string must maintain its order (i.e. "aaabccdee" becomes "abcde").

Notes: You're ordering the the unordered items of {} with the character order (i.e. index)
of STRING."""
def remove_duplicate_chars(string):
	return "".join(sorted({c for c in list(string)}, key=string.index))


"""Reverse a string input, STRING.

   e.g. input: 'hello, world'
        output: 'dlrow ,olleh'"""
def reverse_string(string):
	# "easy way": return string[::-1]
	if len(string) == 1:
		return string

	return string[-1] + reverse_string(string[:-1])

	# Iteratively:
	# reversed_str = ""
	# i = len(string)-1
	# while i >= 0:
	# 	reversed_str += string[i]
	# 	i -= 1

	# return reversed_str


"""Given an input string STRING, reverse the string word by word.

   e.g. input: 'the sky is blue'
        output: 'blue is sky the'"""
def reverse_str_words(string):
	words = string.split(" ")

	# Without using built-in methods:
	reversed_input = words[len(words)-1]
	i = len(words) - 2
	while i >= 0:
		reversed_input += " " + words[i]
		i -= 1

	return reversed_input

	# Better way using built-in methods:
	# reversed_words = words[-1::-1]
	# output = ' '.join(reversed_words)

	# return output


"""Check if a given string STRING is a palindrome.
   Treats upper and lowercase characters the same.

   Runtime:"""
def check_palindrome(string):
	# # Using built-in slicing:
	# return string == string[::-1]

	# Using pointers:
	string = string.lower()
	i = 0
	j = len(string)-1

	while i < j:
		if string[i] == string[j]:
			i += 1
			j -= 1

		else:
			return False

	return True


"""Given a string STRING, return the longest palindromic substring in STRING.

   e.g. input: 'babad'
        output: 'bab'"""
def longest_palindrome_substring(string):
	longest_substring = ""

	for i in range(len(string)):
		j = i + 1

		while j <= len(string) and len(longest_substring) <= len(string[i:]):
			if check_palindrome(string[i:j]) and len(string[i:j]) > len(longest_substring):
				longest_substring = string[i:j]
			j += 1

	return longest_substring


"""Check if the string STRING has any duplicate characters

   e.g. 'helo' - True
        'hello' - False"""
def has_no_duplicates(string):
	if len(set([char for char in string])) == len(string):
		return True

	return False


"""Given a string STRING, return the longest substring with no duplicate characters.

   e.g. input - "zzzhelzz"
        output - 'zhel'"""
def longest_no_duplicate_substring(string):
	longest_substring = ""

	for i in range(len(string)):
		j = i + 1

		while j <= len(string) and len(longest_substring) <= len(string[i:]):
			if has_no_duplicates(string[i:j]) and len(string[i:j]) > len(longest_substring):
				longest_substring = string[i:j]
			j += 1

	return longest_substring


