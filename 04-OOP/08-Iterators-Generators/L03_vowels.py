# Create a class called vowels, which should receive a string. Implement the
# __iter__ and __next__ methods, so the iterator returns only the vowels from the string.


class vowels:
    VOWELS = ['a', 'e', 'i', 'u', 'y', 'o']

    def __init__(self, text: str) -> None:
        self.text = text
        self.string_vowels = [char for char in text if char.lower() in vowels.VOWELS]
        self.current_index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.current_index += 1
        if self.current_index < len(self.string_vowels):
            return self.string_vowels[self.current_index]
        raise StopIteration


# Test code

my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
