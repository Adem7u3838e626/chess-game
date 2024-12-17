import numpy as np

# Initialize the chess table
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

# Function to print the board
def print_table():
    print("    " + "   ".join(columns))
    for i in range(8):
        row_number = 8 - i
        print(f"{row_number}  " + "  ".join(table[i]))

# Function to start a new game
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

# Main game loop
def game(players):
    print('Game started')
    i = 0  # 0 for white's turn, 1 for black's turn
    while True:
        turn = players[i]
        color = "White" if i == 0 else "Black"
        print(f"\n{color} Player's turn: {turn}")
        print_table()  # Show the chessboard at the start of each turn
        move_piece(turn, color)
        i = (i + 1) % 2  # Toggle turns between players

# Function to move a piece
def move_piece(player, color):
    print(f"{color} player's move")
    
    while True:
        move = select_piece(color)  # Get the selected piece's position
        
        piece = table[move[1], move[0]]  # Get the selected piece
        if (color == "White" and piece in ["♙", "♖", "♘", "♗", "♕", "♔"]) or \
           (color == "Black" and piece in ["♟", "♜", "♞", "♝", "♛", "♚"]):
            break
        else:
            print(f"Invalid piece selection. You must select a {color} piece.")
    
    # Player selects where to move the piece
    destination = select_destination(color)
    
    # Get the piece at the destination
    destination_piece = table[destination[1], destination[0]]
    
    # If the destination is occupied by an opponent's piece, it will be captured
    if destination_piece != "":
        print(f"Captured {destination_piece}!")
    
    # Move the piece and update the board
    table[destination[1], destination[0]] = piece
    table[move[1], move[0]] = ""  # Empty the original position
    
    print(f"Moved {piece} from {columns[move[0]]}{8 - move[1]} to {columns[destination[0]]}{8 - destination[1]}")

# Function to select the piece to move (column and row)
def select_piece(color):
    print(f"Select a {color} piece to move.")
    while True:
        move = select()  # Get the move input (column and row)
        column_index = columns.index(move[0])  # Get the column index (a-h)
        row_index = 8 - int(move[1])  # Convert row to correct index (1-8)
        
        if table[row_index, column_index] != "":
            return (column_index, row_index)  # Return the piece's position if it's not empty
        else:
            print("No piece at that position. Please select a valid piece.")

# Function to select the destination to move the piece to
def select_destination(color):
    print(f"Select the destination square for the {color} piece.")
    while True:
        destination = select()  # Get the destination input (column and row)
        column_index = columns.index(destination[0])  # Get the column index (a-h)
        row_index = 8 - int(destination[1])  # Convert row to correct index (1-8)
        
        destination_piece = table[row_index, column_index]
        
        # Ensure destination is empty or occupied by an opponent's piece
        if destination_piece == "":  # Ensure the destination is empty
            return (column_index, row_index)
        elif (color == "White" and destination_piece in ["♟", "♜", "♞", "♝", "♛", "♚"]) or \
             (color == "Black" and destination_piece in ["♙", "♖", "♘", "♗", "♕", "♔"]):
            print("You can't move to a square occupied by your own piece. Please select an empty square.")
        else:
            return (column_index, row_index)  # If it's an opponent's piece, we allow the capture

# Function to select a move (column and row)
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

# Start the game
new()
