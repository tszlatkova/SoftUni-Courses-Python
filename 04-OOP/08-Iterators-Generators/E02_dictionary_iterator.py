# Create a class called dictionary_iter. Upon initialization, it should receive a
# dictionary object. Implement the iterator to return each key-value pair of the
# dictionary as a tuple of two elements (the key and the value).

from typing import Dict


class dictionary_iter:

    def __init__(self, dict: Dict):
        self.dict = dict
        self.dict_items = list(self.dict.items())
        self.idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.idx += 1
        if self.idx < len(self.dict):
            return self.dict_items[self.idx][0], self.dict_items[self.idx][1]
        raise StopIteration


# Test code 1

result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)


# Test code 2

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
