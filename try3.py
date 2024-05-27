import tkinter as tk
import random

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")

        self.current_player = "X"
        self.board = [" "]*9

        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(master, text="", font=("Arial", 20), width=5, height=2,
                                   command=lambda i=i, j=j: self.make_move(i, j))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

    def make_move(self, i, j):
        if self.board[i*3 + j] == " ":
            self.buttons[i][j].config(text=self.current_player, state="disabled")
            self.board[i*3 + j] = self.current_player
            if self.check_winner(self.current_player):
                tk.messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_board()
            elif " " not in self.board:
                tk.messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                if self.current_player == "O":
                    self.computer_move()

    def computer_move(self):
        empty_indices = [i for i, val in enumerate(self.board) if val == " "]
        index = random.choice(empty_indices)
        i, j = divmod(index, 3)
        self.buttons[i][j].config(text=self.current_player, state="disabled")
        self.board[index] = self.current_player
        if self.check_winner(self.current_player):
            tk.messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
            self.reset_board()
        elif " " not in self.board:
            tk.messagebox.showinfo("Tic Tac Toe", "It's a tie!")
            self.reset_board()
        else:
            self.current_player = "X"

    def check_winner(self, player):
        winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        for combo in winning_combinations:
            if all(self.board[i] == player for i in combo):
                return True
        return False

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="", state="normal")
        self.current_player = "X"
        self.board = [" "]*9

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
