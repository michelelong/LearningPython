#!/usr/local/bin/python3

# A decorator takes a function as an argument and returns a function
# The returned function performs logic or processing on the input

def decorFunc(func): # num() is func because of @decorFunc
    def returnedFunc():
        return func() * 3
        # Returned 10 from num() then multipled by 3
    return returnedFunc

@decorFunc
def num():
    return 5 * 2

print(num()) # Call the initial function

print("---")

# Three other common decorators
class User:
    base_url = 'https://example.com/api'

    def __init__(self, name):
        self._name = name

    # Does not require an instance
    @classmethod
    def query(cls, query_string):
        return cls.base_url + '?' + query_string

    # Does not require an instance
    @staticmethod
    def who():
        return "Howdy Doody"

    # Does not need to be called with ()
    @property
    def name(self):
        return self._name


print(User.query("keyword=testing"))
print(User.who())
user1 = User("Michele")
print(user1.name)
