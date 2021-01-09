# Rope

# to do
# insert
# delete

# API
def to_rope(string):
    return String(string)


class Rope:
    def substring(self, start, length):
        return Substring(self, start, length)

    def concatenate(self, right):
        return Concatenation(self, right)

    def delete(self, start, length):
        left = self.substring(0, start)
        right = self.substring(start + length, self.length() - start - length)
        return left.concatenate(right)


class String(Rope):
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string

    def length(self):
        return len(self.string)

    
class Substring(Rope):
    def __init__(self, rope, start, length):
        self.rope = rope
        self.start = start
        self.leng = length

    def __str__(self):
        return str(self.rope)[self.start : self.start + self.leng]

    def length(self):
        return self.leng

class Concatenation(Rope):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.left) + str(self.right)

    def length(self):
        return self.left.length() + self.right.length()


# Testing Framework
def equals(rope, expected):
    actual = str(rope)
    if actual == expected:
        return
    print(actual, " didn't equal ", expected)
    raise Exception()


equals(to_rope("abc"), "abc")
equals(to_rope("abcde").substring(1, 3), "bcd")
equals(to_rope("abcde").substring(1, 3).substring(1,1), "c")
equals(to_rope("abc").concatenate(to_rope("de")), "abcde")
equals(to_rope("abcde").delete(1, 3), "ae")

assert to_rope("abcde").substring(1, 3).length() == 3
assert to_rope("abc").concatenate(to_rope("de")).length() == 5