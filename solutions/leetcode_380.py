from random import randint


class RandomizedSet:

    def __init__(self):
        self.vals = []
        self.keys = {}

    def insert(self, val: int) -> bool:
        if val not in self.keys:
            self.vals.append(val)
            self.keys[val] = len(self.vals) - 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.keys:
            index = self.keys[val]
            last = len(self.vals) - 1
            self.keys[self.vals[last]] = index
            self.vals[last], self.vals[index] = self.vals[index], self.vals[last]
            self.vals.pop()
            self.keys.pop(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        index = randint(0, len(self.vals) - 1)
        return self.vals[index]


if __name__ == '__main__':
    given_param = 1
    obj = RandomizedSet()
    result = obj.insert(given_param)
    assert result
    result = obj.insert(given_param)
    assert not result
    param = obj.getRandom()
    assert param == given_param
