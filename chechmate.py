import sys

# Movement patterns for each piece
DIRECTIONS = {
    'K': [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)],  # King
    'Q': [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)],  # Queen
    'R': [(-1, 0), (1, 0), (0, -1), (0, 1)],  # Rook
    'B': [(-1, -1), (-1, 1), (1, -1), (1, 1)],  # Bishop
    'N': [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)],  # Knight
    'P': [(-1, -1), (-1, 1)],  # Pawn attack directions (white)
    'p': [(1, -1), (1, 1)]  # Pawn attack directions (black)
}

# Function to check if a position is within the chessboard bounds
def is_within_board(row, col):
    return 0 <= row < 8 and 0 <= col < 8

# Function to find the king of a given color
def find_king(board, color):
    king_symbol = 'K' if color == 'white' else 'k'
    for r in range(8):
        for c in range(8):
            if board[r][c] == king_symbol:
                return r, c
    return None

# Function to check if a king is in check
def is_king_in_check(board, king_pos, color):
    opponent_pieces = "prnbqk" if color == "white" else "PRNBQK"
    
    # Check opponent piece attacks
    for r in range(8):
        for c in range(8):
            piece = board[r][c]
            if piece in opponent_pieces:
                if threatens_king(board, r, c, king_pos, piece):
                    return True
    return False

# Function to check if a given piece at (r, c) threatens the king at king_pos
def threatens_king(board, r, c, king_pos, piece):
    kr, kc = king_pos
    piece = piece.upper()
    
    if piece == 'N':  # Knight moves
        return (abs(kr - r), abs(kc - c)) in [(2, 1), (1, 2)]
    
    if piece == 'P':  # Pawn attacks (already handled via movement definitions)
        return (kr - r, kc - c) in DIRECTIONS[piece]

    # Sliding pieces: Rook, Bishop, Queen
    if piece in "RBQ":
        for dr, dc in DIRECTIONS[piece]:
            nr, nc = r + dr, c + dc
            while is_within_board(nr, nc):
                if (nr, nc) == (kr, kc):
                    return True
                if board[nr][nc] != '.':  # Blocked by a piece
                    break
                nr += dr
                nc += dc
    
    # King: one-step moves
    if piece == 'K':
        return max(abs(kr - r), abs(kc - c)) == 1
    
    return False

# Function to generate all legal moves for a given king
def generate_king_moves(board, king_pos, color):
    valid_moves = []
    kr, kc = king_pos
    
    for dr, dc in DIRECTIONS['K']:
        nr, nc = kr + dr, kc + dc
        if is_within_board(nr, nc) and (board[nr][nc] == '.' or board[nr][nc].isupper() != (color == 'white')):
            # Simulate the move
            temp = board[nr][nc]
            board[kr][kc], board[nr][nc] = '.', board[kr][kc]
            if not is_king_in_check(board, (nr, nc), color):
                valid_moves.append((nr, nc))
            # Undo the move
            board[kr][kc], board[nr][nc] = board[nr][nc], temp

    return valid_moves

# Function to determine if the player is in checkmate
def is_checkmate(board, color):
    king_pos = find_king(board, color)
    
    if not is_king_in_check(board, king_pos, color):
        return False
    
    # Check if the king can move
    if generate_king_moves(board, king_pos, color):
        return False
    
    return True  # No escape = Checkmate


for _ in range(int(input())):
    board = [list(sys.stdin.readline().strip()) for _ in range(8)]
    
    # Determine whose turn it is by checking who is in check
    if is_checkmate(board, "white"):
        print("CHECKMATE BLACK")
    elif is_checkmate(board, "black"):
        print("CHECKMATE WHITE")
    else:
        print("NO CHECKMATE")
