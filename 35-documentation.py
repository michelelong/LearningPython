#!/usr/bin/python3

# Docstrings can be run as a test of how a method or function should work
# and the expected output
def docstring_testing(input):
	# The REPL prompt (>>>) will run the method with the given input
	"""
	This is how you create a docstring test.
	>>> docstring_testing("Say Hello to the world!")
	'Say Hello to the world!'
	"""
	return "Say Hello to the world!"

# Run the docstring test
# python3 -m doctest -v 35-documentation.py
