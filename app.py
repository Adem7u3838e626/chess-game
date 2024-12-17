import numpy as np

table = np.array([
    ["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"],
    ["♙", "♙", "♙", "♙", "♙", "♙", "♙", "♙"],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["♟", "♟", "♟", "♟", "♟", "♟", "♟", "♟"],
    ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"]
])
columns = ["a", "b", "c", "d", "e", "f", "g", "h"]
def print_table():
    print("    " + "   ".join(columns))
    for i in range(8):
        row_number = 8 - i
        print(f"{row_number}  " + "  ".join(table[i]))
def new():
    game_started = False
    while not game_started:
        player1 = input('Enter name of Player 1 (White): ')
        player2 = input('Enter name of Player 2 (Black): ')
        verify = input('Do you want to resume? (y/n): ')
        if verify.lower() == "y" or verify.lower() == "yes":
            players = [player1, player2]
            game_started = True
            game(players)
def game(players):
    print('Game started')
    i = 0 
    while True:
        turn = players[i]
        color = "White" if i == 0 else "Black"
        print(f"\n{color} Player's turn: {turn}")
        print_table() 
        move_piece(turn, color)
        i = (i + 1) % 2 
def move_piece(player, color):
    print(f"{color} player's move")
    while True:
        move = select_piece(color) 
        
        piece = table[move[1], move[0]] 
        if (color == "White" and piece in ["♙", "♖", "♘", "♗", "♕", "♔"]) or \
           (color == "Black" and piece in ["♟", "♜", "♞", "♝", "♛", "♚"]):
            break
        else:
            print(f"Invalid piece selection. You must select a {color} piece.")
    destination = select_destination(color)
    destination_piece = table[destination[1], destination[0]]
    if destination_piece != "":
        print(f"Captured {destination_piece}!")
    table[destination[1], destination[0]] = piece
    table[move[1], move[0]] = ""
    print(f"Moved {piece} from {columns[move[0]]}{8 - move[1]} to {columns[destination[0]]}{8 - destination[1]}")
def select_piece(color):
    print(f"Select a {color} piece to move.")
    while True:
        move = select()
        column_index = columns.index(move[0])
        row_index = 8 - int(move[1]) 
        if table[row_index, column_index] != "":
            return (column_index, row_index) 
        else:
            print("No piece at that position. Please select a valid piece.")
def select_destination(color):
    print(f"Select the destination square for the {color} piece.")
    while True:
        destination = select() 
        column_index = columns.index(destination[0])
        row_index = 8 - int(destination[1]) 
        destination_piece = table[row_index, column_index]
        if destination_piece == "": 
            return (column_index, row_index)
        elif (color == "White" and destination_piece in ["♟", "♜", "♞", "♝", "♛", "♚"]) or \
             (color == "Black" and destination_piece in ["♙", "♖", "♘", "♗", "♕", "♔"]):
            print("You can't move to a square occupied by your own piece. Please select an empty square.")
        else:
            return (column_index, row_index) 
def select():
    result = ['', '']
    while result[0] not in columns:
        result[0] = input('Choose the column (a-h): ').lower()
        if result[0] not in columns:
            print("Invalid column. Please choose between a-h.")

    while result[1] not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        result[1] = input('Choose the row (1-8): ')
        if result[1] not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            print("Invalid row. Please choose between 1-8.")

    return result

new()
