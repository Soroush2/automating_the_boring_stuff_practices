import sys

def initialize_board():
    return {
        "top-L": " ", "top-M": " ", "top-R": " ",
        "mid-L": " ", "mid-M": " ", "mid-R": " ",
        "low-L": " ", "low-M": " ", "low-R": " "
    }

def print_board(board):
    print(board["top-L"] + "|" + board["top-M"] + "|" + board["top-R"])
    print("-+-+-")
    print(board["mid-L"] + "|" + board["mid-M"] + "|" + board["mid-R"])
    print("-+-+-")
    print(board["low-L"] + "|" + board["low-M"] + "|" + board["low-R"])

def get_valid_move(board, current_player):
    """Prompt the current player for a valid move and return the chosen key."""
    while True:
        # Display available positions
        available_positions = [key for key, value in board.items() if value == " "]
        print("Available positions:", " | ".join(available_positions))
        move = input(f"Player {current_player}, enter the location you want to play: ").strip()
        
        if move not in board:
            print("Wrong input. Please choose from the available positions.")
        elif board[move] != " ":
            print("That location is already occupied. Choose another.")
        else:
            return move

def update_board(board, move, player):
    board[move] = player
    return board

def check_winner(board, players):
    # Define winning combinations
    winning_combinations = [
        ("top-L", "top-M", "top-R"),
        ("mid-L", "mid-M", "mid-R"),
        ("low-L", "low-M", "low-R"),
        ("top-L", "mid-L", "low-L"),
        ("top-M", "mid-M", "low-M"),
        ("top-R", "mid-R", "low-R"),
        ("top-L", "mid-M", "low-R"),
        ("top-R", "mid-M", "low-L")
    ]
    
    for combo in winning_combinations:
        a, b, c = combo
        if board[a] == board[b] == board[c] != " ":
            winner = board[a]
            print(f'Player {winner} won!')
            players[winner] += 1
            return True
    return False

def play_game():
    players = {'O': 0, 'X': 0}
    current_player = "O"
    
    while True:
        board = initialize_board()
        game_over = False
        
        while not game_over:
            print_board(board)
            move = get_valid_move(board, current_player)
            board = update_board(board, move, current_player)
            
            if check_winner(board, players):
                print_board(board)
                print("Current Scores:")
                for player, score in players.items():
                    print(f"Player {player}: {score}")
                game_over = True
            else:
                # Swap players
                current_player = "X" if current_player == "O" else "O"
        
        play_again = input("Play again? (y/n): ").strip().lower()
        if play_again != 'y':
            break

if __name__ == '__main__':
    try:
        play_game()
    except KeyboardInterrupt:
        sys.exit()
