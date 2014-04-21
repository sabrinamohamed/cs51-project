
# Initial code and style inspired by:
# https://github.com/apresta/tagger/blob/master/tagger.py#L133

from __future__ import division

import collections
import re
import nltk

mystemmer = Stemmer(nltk.stem.LancasterStemmer)

class Emotion:

	# Class for emotional signifiers

	# Note to self: explanation of underscores in Python method names
	# http://igorsobreira.com/2010/09/16/difference-between-one-underline-and-two-underlines-in-python.html

	def __init__(self, string, stem=None, rating=1.0, hashtag=False):

		# We initialize with the following variables:

		# @param string:		the string representation of emotional signifier
		# @param stem:			the stemmed representation
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

	def __init__(self, tail, head=None):

		# @param tail:		TODO DESCRIPTION
		# @param head:		TODO DESCRIPTION

		if not head:
			# TODO
		else:
			# TODO

	def combined_rating(self):

		# Method for combining ratings for multiple emotional signifiers
		# Default should be geometric mean

		# TODO


class Reader:

	# Class for parsing a tweet into emotional signifiers

	match_apostrophes = re.compile(r'`|’')
    match_paragraphs = re.compile(r'[\.\?!\t\n\r\f\v]+')
    match_phrases = re.compile(r'[,;:\(\)\[\]\{\}<>]+')
    match_words = re.compile(r'[\w\-\'_/&]+')

    # TODO: Create functionality for emoticons, such as :)  :*  :D

	def __call__(self, text):

		# @param text:		the string of text (tweets) to be analyzed
		# @returns:			list of tweets ranked by positivity of emotion;
		# 					range (0, 1: most negative to most positive)

		text = self.preprocess(text)

		# TODO: Figure out how to split blocks of tweets

		tweets = []

		# TODO: Interate through tweets

		for tweet in tweets:
			# TODO:
			# Iterate through phrases (every few words) in tweet
			# Create map of emotional signifiers (Emotions) for each tweet

	def preprocess(self, text):

		# @param:		string containing original document
		# @param:		processed text

		# TODO: Decide how we want to preprocess, if this is necessary




