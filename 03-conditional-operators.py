#!/usr/local/bin/python3

# Relational operators
print("2 equals 2: %s" % (2 == 2))
print("2 does not equal 5: %s" % (2 != 5))
print("2 is greater than 5: %s" % (2 > 5))
print("2 is greater than or equal to 5: %s" % (2 >= 5))
print("2 is less than 5: %s" % (2 < 5))
print("2 is less than or equal to 2: %s\n" % (2 <= 2))

# is checks identity (same object), == checks equality
a = [1, 2, 3]
b = [1, 2, 3]
print("Is one in the list? %s" % (1 in a))
print("a is b: %s" % (a is b))
print("a is not b: %s" % (a is not b))
print("a equals b: %s" % (a == b))

# Order of precedence
# not is evaluated first
# and is evaluated second
# or is evaluated last

# and both must be true
print("\n1 is less than 2 AND 2 is less than 3: %s" % (1 < 2 and 2 < 3))

# or one must be true, if first is true there is no check of the second
print("1 is greater than 2 OR 2 is less than 3: %s" % (1 > 2 or 2 < 3))
print("\nThe 'not' operator reverses the statements return value:")
print("2 is equal to 2: %s" % (not 2 == 2))
print("41 is greater than 40: %s\n" % (not 41 > 40))

# Boolean values
b = True
c = False
d = None
print(type(b))
print(bool(1))
print (d is False)
