# Create a class called countdown_iterator. Upon initialization, it should receive a
# count. Implement the iterator to return each countdown number (from count to 0
# inclusive), separated by a single space.


class countdown_iterator:

    def __init__(self, count: int):
        self.count = count
        self.current = self.count + 1

    def __iter__(self):
        return self

    def __next__(self):
        self.current -= 1
        if self.current >= 0:
            return self.current
        raise StopIteration


print('Test code 1')
iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")

print('\n\nTest code 2')
iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")
