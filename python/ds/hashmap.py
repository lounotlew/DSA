######################################################################
# Implementation of a hashmap using Python dictionaries and lists.   #
#                                                                    #
# Written by Lewis Kim.                                              #
######################################################################

from hashlib import sha256


# A HashMap that uses chaining for collision and SHA256 for hashing.
class HashMap:

	"""."""
	def __init__(self):
		self.data = {}
		self.keys = []


	"""Add a KEY, VALUE pair to this HashMap."""
	def put(self, key, value):
		hashed_key = sha256(bytes(key, encoding='utf-8')).hexdigest()

		# Collision chaining
		if hashed_key in self.keys:
			self.data[hashed_key].append(value)
			print("There was a collision. Successfully added " + key + ":" + value + ".")

		else:
			self.keys.append(hashed_key)
			self.data[hashed_key] = [value]
			print("Successfully added " + key + ":" + value + ".")

		return


	"""Look up all values whose key is KEY in this HashMap."""
	def lookup(self, key):
		hashed_key = sha256(bytes(key, encoding='utf-8')).hexdigest()

		if hashed_key not in self.keys:
			print("That key does not exist in this HashMap.")
			return

		else:
			return self.data[hashed_key]


	"""Remove all items whose key is KEY from this HashMap."""
	def remove(self, key):
		hashed_key = sha256(bytes(key, encoding='utf-8')).hexdigest()

		if hashed_key not in self.keys:
			print("That key does not exist in this HashMap.")
			return

		else:
			del self.data[hashed_key]

