#Python
#Module 4 - Sprint 1
#Project review
#-----------------------------------------------------------
#A Chess question

def main():
    chess_board = new_chess_board()
    white_piece, white_location = ask_user_white(chess_board)
    chess_board[white_location] = white_piece

    black_pieces = ask_user_black(chess_board)

    chess_board[white_location] = white_piece

    for piece, location in black_pieces:
        chess_board[location] = piece
    
    if white_piece == "rook":
        captured_pieces = rook_captures(chess_board, white_location)
        print("Captured black pieces:")
        for location in captured_pieces:
            print(chess_board[location], location)
    elif white_piece == "pawn":
        captured_pieces = pawn_captures(chess_board, white_location)
        print("Captured black pieces:")
        for piece, location in captured_pieces:
            print(piece, location)


def new_chess_board():
    positions = {
    "a1": None, "a2": None, "a3": None, "a4": None, "a5": None, "a6": None, "a7": None, "a8": None,
    "b1": None, "b2": None, "b3": None, "b4": None, "b5": None, "b6": None, "b7": None, "b8": None,
    "c1": None, "c2": None, "c3": None, "c4": None, "c5": None, "c6": None, "c7": None, "c8": None,
    "d1": None, "d2": None, "d3": None, "d4": None, "d5": None, "d6": None, "d7": None, "d8": None,
    "e1": None, "e2": None, "e3": None, "e4": None, "e5": None, "e6": None, "e7": None, "e8": None,
    "f1": None, "f2": None, "f3": None, "f4": None, "f5": None, "f6": None, "f7": None, "f8": None,
    "g1": None, "g2": None, "g3": None, "g4": None, "g5": None, "g6": None, "g7": None, "g8": None,
    "h1": None, "h2": None, "h3": None, "h4": None, "h5": None, "h6": None, "h7": None, "h8": None
}
    return positions

def coordinate_to_notation(row, col):
    col_notation = chr(ord("a") + row)
    row_notation = str(col + 1)
    return col_notation + row_notation

def notation_to_coordinate(notation):
    col_notation = notation[0]
    row_notation = int(notation[1]) - 1
    row = ord(col_notation) - ord("a")
    col = row_notation
    return (row, col)

valid_locations = new_chess_board()

def ask_user_white(chess_board):
    valid_pieces = ["rook", "pawn"]

    asking = True
    while asking:
        user_input = input("Choose your white piece: rook or pawn, and insert location as 'piece x0': ")
        piece, location = user_input.split(" ")
        if piece in valid_pieces and location in valid_locations:
            print("Got it. White piece added!")
            print()
            return piece, location
        elif piece not in valid_pieces and location in valid_locations:
            print("Piece name not valid. Please try again.")
            print()
        elif piece in valid_pieces and location not in valid_locations:
            print("Location not valid. Please try again.")
            print()
        else:
            print("Wrong format! Follow this example: pawn a1 - Please go again: ")
            print()

def ask_user_black(chess_board):
    valid_pieces = ["pawn", "rook", "knight", "bishop", "queen", "king"]
    piece_count = {"pawn": 0, "rook": 0, "knight": 0, "bishop": 0, "queen": 0, "king": 0}

    black_pieces = []

    asking = True
    while asking:
        user_input = input("Enter a black piece and its location: ")
        if user_input == "done":
            if black_pieces != []:
                print("Thank you for your input. Processing...")
                print()
                return black_pieces
            else:
                print("You must insert at least one black piece.")
                print()
                continue

        piece, location = user_input.split(" ")

        if piece in valid_pieces and location in valid_locations:
            if chess_board[location] is not None:
                print("Location already occupied. Please try again.")
                print()
            elif piece_count[piece] > 1 and piece in ["rook", "knight", "bishop"]:
                print(f"You have two {piece}s, and they have alredy been placed. Please choose a different piece, or type 'done'.")
                print()
            elif piece_count[piece] > 7 and piece in ["pawn"]:
                print("Maximum pawns reached. Please choose a different piece, or type 'done'.")
                print()
            elif piece_count[piece] > 0 and piece in ["queen", "king"]:
                print(f"You can only place one {piece}. Please choose a different piece, or type 'done'.")
                print()
            else:
                print("Got it. Black piece added!")
                print()
                piece_count[piece] += 1
                black_pieces.append((piece, location))
        elif piece not in valid_pieces and location in valid_locations:
            print("Piece name not valid. Please try again.")
            print()
        elif piece in valid_pieces and location not in valid_locations:
            print("Location not valid. Please try again.")
            print()
        else:
            print("Wrong format! Follow the same format: pawn a1 - Please go again: ")
            print()

def rook_captures(chess_board, rook_location):
    captures = []
    row, col = notation_to_coordinate(rook_location)

    # Check horizontally (left and right)
    for i in range(col - 1, -1, -1):
        target_location = coordinate_to_notation(row, i)
        if chess_board[target_location] is not None:
            captures.append(target_location)
            break

    for i in range(col + 1, 8):
        target_location = coordinate_to_notation(row, i)
        if chess_board[target_location] is not None:
            captures.append(target_location)
            break

    # Check vertically (up and down)
    for i in range(row - 1, -1, -1):
        target_location = coordinate_to_notation(i, col)
        if chess_board[target_location] is not None:
            captures.append(target_location)
            break

    for i in range(row + 1, 8):
        target_location = coordinate_to_notation(i, col)
        if chess_board[target_location] is not None:
            captures.append(target_location)
            break

    return captures

def pawn_captures(chess_board, pawn_location):
    captures = []
    row, col = notation_to_coordinate(pawn_location)

    # Check diagonal captures (one square forward and left/right)
    left_capture = coordinate_to_notation(row - 1, col + 1)
    right_capture = coordinate_to_notation(row + 1, col - 1)

    if col > 0 and row < 7 and chess_board[left_capture] is not None:
        captures.append((chess_board[left_capture], left_capture))

    if col > 0 and row > 0 and chess_board[right_capture] is not None:
        captures.append((chess_board[right_capture], right_capture))

    return captures


main()

# Structure (part of the coding process):

# Ask the user to choose a WHITE chess piece between two options, and input location (e.g. pawn a2)
# Print confirmation or error - if error, ask again.
# Tell user that they can now input 1-16 black pieces, in the same format.
# Ask user for a black piece and location.
# Print confirmation or error - if error, ask again.
# User can write "done" whenever they want to finish, after a min. of 1 piece and max. of 16 pieces.
# Assume that "done" and piece format will be correct.
# Coords are from a-h and 1-8.
# Don't allow more than one piece in a certain location.
# Don't allow more than 2x bishop, 2x rook, 2x knight, 8x pawn, 1x king, 1x queen.
# Don't ask for more than 16 black pieces - indirectly resolved (I think!)
# After the user is done, the program should print out the black pieces, if any, that can be taken by the white piece.

# OPTIONAL: Print the board after each piece is taken