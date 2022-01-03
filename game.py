# first we need to create a class for the game
class tictactoe:
    # for a game we need a game board
    # we need two players, represented by letter "O" and "X"
    def __init__(self, letter,board): # board should be a list storing the data for each spot
        self.letter = letter
        self.board = board

    @staticmethod
    def gameboard():
        #since the board is 3*3, create a 9-element list
        emptyboard = ['' for _ in range(9)]
        # divid the list into 3 rows
        emptyboard = [[' ' for _ in range(3)] for _ in range(3)]
        for row in emptyboard:
            print('| ' + ' | '.join(row) + ' |')


    # define a gameboard with choice number on it. It will be used to input position
    @staticmethod
    def gameboard_num():
        board_num = [[str(i) for i in range(3*j,3*j+3)] for j in range(3)]
        for row in board_num:
            print('| ' + ' | '.join(row) + ' |')

    
    # create a method for available spot on the board
    def available_spot(self):
        #available spot should be a list
        available_spot = [i for i in range(9) if self.board[i] == " "]
        return available_spot

    
    # create a method for take a move. parameter should be self.board , self.letter , player

    def take_a_move(self,player):





    # create a method to check if the move leads to a win
    def win(self,letter):

        # check rows 
        for i in range(3):
            if all(self.board[j] == letter for j in range(3*i,3*(i+1))):
                print('player ' + letter + ' wins!' )
        
        # check columns

        for i in range(3):
            if all(self.board[j] == letter for j in [i,3*(i+1),3*(i+2)])
                

        # check diagonals

        if all(self.board[i] == letter for i in [0,4,8]):

        if all(self.board[i] == letter for i in [2,4,6]):
                




# Let's initiate a game

def play("some variables",letter, print_board = True):


    if print_borad == True:

        letter = "X"
    # humanplayer take a move


    
