# Rope

# to do
# insert
# delete
# substring
# concatenation

# API
def to_rope(string):
    return String(string)


class Rope:
    def substring(self, start, length):
        return Substring(self, start, length)

    def concatenate(self, string):
        return "abcde"

class String(Rope):
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string

    
class Substring(Rope):
    def __init__(self, rope, start, length):
        self.rope = rope
        self.start = start
        self.length = length

    def __str__(self):
        return str(self.rope)[self.start : self.start + self.length]

assert str(to_rope("abc")) == "abc"
assert str(to_rope("abcde").substring(1, 3)) == "bcd"
assert str(to_rope("abcde").substring(1, 3).substring(1,1)) == "c"
assert str(to_rope("abc").concatenate(to_rope("de"))) == "abcde"