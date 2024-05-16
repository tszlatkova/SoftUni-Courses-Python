shelf_of_books = input().split('&')

command = input()

while command != 'Done':

    command = command.split(' | ')
    action = command[0]

    if action == 'Add Book':
        if command[1] not in shelf_of_books:
            shelf_of_books.insert(0, command[1])

    elif action == 'Take Book':

        if command[1] in shelf_of_books:
            shelf_of_books.remove(command[1])

    elif action == 'Swap Books':

        if command[1] in shelf_of_books and command[2] in shelf_of_books:
            index1 = shelf_of_books.index(command[1])
            index2 = shelf_of_books.index(command[2])

            shelf_of_books[index1], shelf_of_books[index2] = shelf_of_books[index2], shelf_of_books[index1]

    elif action == 'Insert Book':

        if command[1] not in shelf_of_books:
            shelf_of_books.append(command[1])

    elif action == 'Check Book':

        index = int(command[1])
        if 0 <= index < len(shelf_of_books):
            print(shelf_of_books[index])

    command = input()

print(*shelf_of_books, sep = ', ')