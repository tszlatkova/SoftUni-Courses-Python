# Create a generator function called reverse_text that receives a string and yields all
# string characters on one line in reversed order.

def reverse_text(text: str):

    current_idx = len(text)-1
    while current_idx >= 0:
        yield text[current_idx]
        current_idx -= 1


for char in reverse_text("step"):
    print(char, end='')
