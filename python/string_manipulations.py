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

