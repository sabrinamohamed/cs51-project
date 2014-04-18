
# Initial code and style inspired by:
# https://github.com/apresta/tagger/blob/master/tagger.py#L133

from __future__ import division

import collections
import re


class Emotion:

	# Class for emotional signifiers

	# Note to self: explanation of underscores in Python method names
	# http://igorsobreira.com/2010/09/16/difference-between-one-underline-and-two-underlines-in-python.html

	def __init__(self, string, stem=None, rating=1.0, hashtag=False):

		# This is the class for an emotional signifier
		# We initialize with the following variables:

		# @param string:		the string representation of emotional signifier
		# @param stem:		the stemmed representation
		# @param rating:		magnitude of the emotional signifier; range [0,1]
		# @param hashtag:		whether the emotional signifier is a hashtag

		self.string = string
		self.stem = stem or string
		self.rating = rating
		self.proper = proper
		self.terminal = terminal

	def __eq__(self, other):
		return self.stem == other.stem

	def __repr__(self):
		return repr(self.string)

	def __lt__(self, other):
		return self.rating > other.rating

	def __hash__ (self):
		return hash(self.stem)

class MixedEmotion(Emotion):

	# Class for combinations of emotional signifiers


