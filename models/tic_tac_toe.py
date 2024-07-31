import numpy as np

class TicTacToe:
    def __init__(self):
        # initialize the 3x3 board with zeros
        self.board = np.zeros((3, 3), dtype=int)
        # player 1 starts the game
        self.current_player = 1

    def reset(self):
        # reset the board to its initial state and set the starting player
        self.board = np.zeros((3, 3), dtype=int)
        self.current_player = 1
        return self.board

    def step(self, action):
        # calculate row and column from the action index
        row, col = action // 3, action % 3
        if self.board[row, col] != 0:
            raise ValueError("Invalid action!")
        # place the player's marker on the board
        self.board[row, col] = self.current_player
        # check if there is a winner or if the game is a draw
        reward, done = self.check_winner()
        # switch to the other player
        self.current_player = 3 - self.current_player
        return self.board, reward, done

    def check_winner(self):
        for player in [1, 2]:
            # check rows and columns for a win
            for row in range(3):
                if all(self.board[row, :] == player):
                    return player, True
            for col in range(3):
                if all(self.board[:, col] == player):
                    return player, True
            # check diagonals for a win
            if all([self.board[i, i] == player for i in range(3)]) or all([self.board[i, 2 - i] == player for i in range(3)]):
                return player, True
        # check for a draw (no empty spaces left)
        if np.all(self.board != 0):
            return 0, True
        # game continues
        return 0, False

    def available_actions(self):
        # return a list of available actions (empty cells)
        return [i for i in range(9) if self.board[i // 3, i % 3] == 0]

    def render(self):
        # render the board with a more readable format
        symbols = {0: " ", 1: "X", 2: "O"}
        board_str = "\n".join(["|".join([symbols[cell] for cell in row]) for row in self.board])
        print(board_str.replace("0", " "))
