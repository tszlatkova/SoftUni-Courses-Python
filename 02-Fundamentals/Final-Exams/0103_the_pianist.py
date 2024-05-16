# You are a pianist, and you like to keep a list of your favorite piano pieces. Create a program to help you
# organize it and add, change, remove pieces from it!
# On the first line of the standard input, you will receive an integer n – the number of pieces you will initially have.
# On the next n lines, the pieces themselves will follow with their composer and key, separated by "|" in the following
# format: "{piece}|{composer}|{key}".
# Then, you will be receiving different commands, each on a new line, separated by "|", until the "Stop" command is
# given:
# •	"Add|{piece}|{composer}|{key}":
# o	You need to add the given piece with the information about it to the other pieces and print:
# "{piece} by {composer} in {key} added to the collection!"
# o	If the piece is already in the collection, print:
# "{piece} is already in the collection!"
# •	"Remove|{piece}":
# o	If the piece is in the collection, remove it and print:
# "Successfully removed {piece}!"
# o	Otherwise, print:
# "Invalid operation! {piece} does not exist in the collection."
# •	"ChangeKey|{piece}|{new key}":
# o	If the piece is in the collection, change its key with the given one and print:
# "Changed the key of {piece} to {new key}!"
# o	Otherwise, print:
# "Invalid operation! {piece} does not exist in the collection."
# Upon receiving the "Stop" command, you need to print all pieces in your collection in the following format:
# "{Piece} -> Composer: {composer}, Key: {key}"

# Input/Constraints
# •	You will receive a single integer at first – the initial number of pieces in the collection.
# •	For each piece, you will receive a single line of text with information about it.
# •	Then you will receive multiple commands in the way described above until the command "Stop".

# Output
# •	All the output messages with the appropriate formats are described in the problem description.

number_of_pieces = int(input())

pieces_info = {}

for _ in range(number_of_pieces):
    piece, composer, key = input().split('|')

    pieces_info[piece] = {'composer': composer, 'key': key}

while True:
    command = input()

    if command == 'Stop':
        break
    else:
        command = command.split('|')
        action = command[0]
        piece = command[1]

    if action == 'Add':
        composer, key = command[2], command[3]

        if piece in pieces_info.keys():
            print(f'{piece} is already in the collection!')
        else:
            pieces_info[piece] = {'composer': composer, 'key': key}
            print(f'{piece} by {composer} in {key} added to the collection!')

    elif action == 'Remove':
        if piece in pieces_info.keys():
            del(pieces_info[piece])
            print(f'Successfully removed {piece}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')

    elif action == 'ChangeKey':
        new_key = command[2]
        if piece in pieces_info.keys():
            pieces_info[piece]['key'] = new_key
            print(f'Changed the key of {piece} to {new_key}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')

for piece in pieces_info:
    composer = pieces_info[piece]['composer']
    key = pieces_info[piece]['key']
    print(f'{piece} -> Composer: {composer}, Key: {key}')
