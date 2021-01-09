# Rope

# to do
# reorder Rope

# API
def to_rope(string):
    return String(string)


class Rope:
    def __add__(self, addend):
        return Concatenation(self, addend)

    def __getitem__(self, index):
        if type(index) == int:
            return self.__get_single_item__(index)
        return Substring(self, index.start, index.stop - index.start)

    def delete(self, start, length):
        left = self[0:start]
        right = self[start + length : len(self)]
        return left + right

    def insert(self, rope, start):
        left = self[0:start]
        right = self[start : len(self)]
        return left + rope + right

    def __len__(self):
        raise Exception("Should have been overriden")

    def __get_single_item__(self, index):
        raise Exception("Should have been overriden")


class String(Rope):
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string

    def __len__(self):
        return len(self.string)

    def __get_single_item__(self, index):
        return self.string[index]
    
class Substring(Rope):
    def __init__(self, rope, start, length):
        self.rope = rope
        self.start = start
        self.leng = length

    def __str__(self):
        return str(self.rope)[self.start : self.start + self.leng]

    def __len__(self):
        return self.leng

class Concatenation(Rope):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.left) + str(self.right)

    def __len__(self):
        return len(self.left) + len(self.right)

    def __get_single_item__(self, index):
        return self.right[index - len(self.left)]


# Testing Framework
def equals(rope, expected):
    actual = str(rope)
    if actual == expected:
        return
    print(actual, "didn't equal", expected)
    raise Exception()


equals(to_rope("abc"), "abc")
equals(to_rope("abcde")[1:4], "bcd")
equals(to_rope("abcde")[1:4][1:2], "c")
equals(to_rope("abc") + to_rope("de"), "abcde")
equals(to_rope("abcde").delete(1, 3), "ae")

assert len(to_rope("abcde")[1:4]) == 3
assert len(to_rope("abc") + to_rope("de")) == 5

equals(to_rope("abe").insert(to_rope("cd"), 2), "abcde")

equals(to_rope("abcde")[3], "d")
equals((to_rope("abc") + to_rope("de"))[3], "d")