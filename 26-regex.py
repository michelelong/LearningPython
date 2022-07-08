#!/usr/local/bin/python3
import re

# Regular Expression search patterns
# \d - digit 0-9
# \D - non-digit
# \s - whitespace
# \S - non-whitespace
# \w - alpha-numeric, a-z and 0-9
# \W - non-alpha-numeric
# \b - boundary space around words
# \A - beginning of string
# \Z - end of string
#  + - one or more
#  * - zero or more
#  ? - zero or one
# {n} - exactly n occurences
# {n, x} - min and max occurences

message = "Take up one idea. Take up one idea at a time."

# Search only returns the first match
result = re.search(r"\sT\w\w\w", message)
print(result)

# Findall returns a list of all matches
result = re.findall(r"o\w\w", message)
print(result)

# Match only checks the beginning of the string
result = re.match(r"T\w", message)
print(result)
print(result.group())

# Find and replace
result = re.sub(r"Take", "Speak", message)
print(result)

result = re.search(r"\sT\w+", message)
print(result)

result = re.search(r"\sT\w{3}", message)
print(result)

# Special Characters
#  \ - escape special characters
#  ^ - beginning of string
#  . - (dot) any character except newline
#  $ - end of string
# [...] - range of values
# [#..] - do not match range of values
# (a|b) - a or b

msg = "Tape up one idea. Take up two ideas at a time."

result = re.findall(r"Ta[pk]e", msg)
print(result)

result = re.search(r"Ta(p|k)e", msg)
print(result)
