# Rope

# to do
# insert
# delete
# substring
# concatenation

# API
def to_rope(string):
    return Rope(string)


class Rope:
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string

    def substring(self,start,length):
        return Substring()

class Substring:
    def __str__(self):
        return "bcd"

assert str(to_rope("abc")) == "abc"
assert str(to_rope("abcde").substring(1, 3)) == "bcd"