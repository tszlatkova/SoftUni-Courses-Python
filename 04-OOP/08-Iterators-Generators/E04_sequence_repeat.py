# Create a class called sequence_repeat which should receive a sequence and a number upon
# initialization. Implement an iterator to return the given elements, so they form a
# string with a length - the given number. If the number is greater than the number of
# elements, then the sequence repeats as necessary. For more clarification, see the
# examples:


class sequence_repeat:

    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.count = -1
        self.count_number = 0

    @property
    def sequence(self):
        return self.__sequence

    @sequence.setter
    def sequence(self, value):
        if len(value) == 0:
            raise IndexError("You should have at least one character in the string!")
        self.__sequence = value

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        self.count_number += 1
        if self.count_number > self.number:
            raise StopIteration
        if self.count == len(self.sequence):
            self.count = 0
        return self.sequence[self.count]


print('Test code 1')
result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')


print('\n\nTest code 2')
result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end='')
