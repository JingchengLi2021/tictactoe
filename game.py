# first we need to create a class for the game
class tictactoe:
    # for a game we need a game board
    # we need two players, represented by letter "O" and "X"
    def __init__(self, letter):
        self.letter = letter

    @staticmethod
    def gameboard():
        #since the board is 3*3, create a 9-element list
        emptyboard = ['' for _ in range(9)]
        # divid the list into 3 rows
        emptyboard = [[' ' for _ in range(3)] for _ in range(3)]
        for row in emptyboard:
            print('| ' + ' | '.join(row) + ' |')


    # define a gameboard with choice number on it. It will be used to input position
    def gameboard_num():
        board_num = [[str(i) for i in range(3*j+1,3*j+4)] for j in range(3)]
        for row in board_num:
            print('| ' + ' | '.join(row) + ' |')