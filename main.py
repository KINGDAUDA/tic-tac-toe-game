import random
import time

def print_board(b):
    print(f"\n{b[0]}  | {b[1]}  | {b[2]}")
    print("---|----|---")
    print(f"{b[3]}  | {b[4]}  | {b[5]}")
    print("---|----|---")
    print(f"{b[6]}  | {b[7]}  | {b[8]} \n")


def check_win(b, player):
    wins = [[0, 1, 2],
            [3, 4, 5],
            [6, 7, 8], #Rows
            [0, 4, 8],
            [2, 4, 6], #Diagonals
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8]] #Columns

    for condition in wins:
        if b[condition[0]] == b[condition[1]] == b[condition[2]] == player:
            return True
    return False

def get_ai_move(b, ai_symbol='O', human_symbol='X'):
    available_moves = [i for i, spot in enumerate(b) if spot not in ["X", "O"]]
    #Priority 1: Check for an immediate win
    for move in available_moves:
        temp_board = b.copy()
        temp_board[move] = ai_symbol
        if check_win(temp_board, ai_symbol):
            return move
    #Priority 2: Block human player from winning
    for move in available_moves:
        temp_board = b.copy()
        temp_board[move] = human_symbol
        if check_win(temp_board, human_symbol):
            return move
    #Priority 3: Pick center if available (strategic advantage)
    if 4 in available_moves:
        return 4
    return random.choice(available_moves)

def play_game():
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    current_player = "X"
    moves_left = 9

    print("WELCOME TO THE TIC-TAC-TOE GAME!\n\n")
    mode = input(
        "Choose Mode: \n1. Play against Human\n2. Play against AI\nEnter 1 or 2: "
    ).strip()

    while mode not in ["1", "2"]:
        print(f"{mode} is an invalid input. Choose again.\n")
        mode = input(
            "Choose Mode: \n1. Play against Human\n2. Play against AI\nEnter 1 or 2: "
        ).strip()

    vs_ai = mode == "2"

    while moves_left > 0:
        print_board(board)

        #AI Turn
        if vs_ai and current_player == "O":
            print("AI is making a move...")
            time.sleep(1)
            index = get_ai_move(board)

        else:
            choice = input(f"\nPlayer {current_player}, choose a position on the board\n")

            #Validate input
            if not choice.isdigit() or int(choice) < 1 or int(choice) > 9:
                print("Invalid input. Pick a number between 1 and 9.")
                continue

            index = int(choice) -1

            #check if choice is already taken
            if board[index] in ["X", "O"]:
                print("That spot has already been taken! Pick another.")
                continue

        #place player mark
        board[index] = current_player
        moves_left -= 1

        #Check for victory
        if check_win(board, current_player):
            print_board(board)
            winner = "AI" if (vs_ai and current_player == "O") else f"Player {current_player}"
            print(f"{winner} wins!")
            return

        #switch turns
        current_player = "O" if current_player == "X" else "X"

    print_board(board)
    print("It's a draw!")

# Start the game
if __name__ == "__main__":
    play_game()