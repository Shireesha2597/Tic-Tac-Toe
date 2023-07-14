import tkinter as tk
from tkinter import messagebox

# Create the main window
window = tk.Tk()
window.title("Tic Tac Toe")
# Define player constants
PLAYER_X = "X"
PLAYER_O = "O"

# Define an empty board
board = [["", "", ""],
         ["", "", ""],
         ["", "", ""]]

# Define the current player
current_player = PLAYER_X

def reset_board():
    global board, current_player
    board = [["", "", ""],
             ["", "", ""],
             ["", "", ""]]
    current_player = PLAYER_X
    clear_buttons()

def clear_buttons():
    for i in range(3):
        for j in range(3):
            buttons[i][j].configure(text="")

def check_winner():
    # Check rows
    for i in range(3):
        if (board[i][0] == board[i][1] == board[i][2]) and (board[i][0] != ""):
            return True

    # Check columns
    for j in range(3):
        if (board[0][j] == board[1][j] == board[2][j]) and (board[0][j] != ""):
            return True

    # Check diagonals
    if (board[0][0] == board[1][1] == board[2][2] != "") or (board[0][2] == board[1][1] == board[2][0] != ""):
        return True

    return False

def make_move(row, col):
    global current_player

    if board[row][col] == "":
        board[row][col] = current_player
        buttons[row][col].configure(text=current_player)

        if check_winner():
            messagebox.showinfo("Winner", f"Player {current_player} wins!")
            reset_board()
        elif all(board[i][j] != "" for i in range(3) for j in range(3)):
            messagebox.showinfo("Draw", "It's a draw!")
            reset_board()
        else:
            current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X

def create_button(row, col):
    return tk.Button(
        window,
        text="",
        width=10,
        height=5,
        command=lambda: make_move(row, col)
    )

# Create buttons for the Tic Tac Toe board
buttons = []
for i in range(3):
    row_buttons = []
    for j in range(3):
        button = create_button(i, j)
        button.grid(row=i, column=j)
        row_buttons.append(button)
    buttons.append(row_buttons)

# Create a reset button
reset_button = tk.Button(
    window,
    text="Reset",
    width=10,
    height=2,
    command=reset_board
)
reset_button.grid(row=3, column=1, pady=10)
# Call the reset_board function to initialize the game
reset_board()

# Start the GUI event loop
window.mainloop()
