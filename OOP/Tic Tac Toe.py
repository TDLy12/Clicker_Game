import sys
import pudb

class TicTacToe:
    def __init__(self, player1, player2, board, turn):
        self.board = board
        self.player = [player1, player2]
        self.turn = 0

    def play(self):
        flag = False

        while not flag:
            current_player = self.player[self.turn]
            self.board.print_board()

class Board(TicTacToe):
    def __init__(self):
        self.tiles = range(9)

    def print_board(self):





