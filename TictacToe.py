class TicTacToe:
    def __init__(self):
        self.board = [" "] * 9

    def display_board(self):
        for i in self.board:
            print(i, end="|")

    class Person:
        pass


    class Robot:
        pass

game = TicTacToe()
game.display_board()