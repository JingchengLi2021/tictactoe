# first we need to create a class for the game
import player
class tictactoe:
    # for a game we need a game board
    # we need two players, represented by letter "O" and "X"
    # board is not a input(attribute) so I should not make it inside of __init__()
    # Instead, I should define below (the original status of the board, every spot is empty)
    # We don't need to input letter in the game. So the class game is like a game current status, letter is a attribute for the player.
    def __init__(self): # board should be a list storing the data for each spot
        self.board = [' ' for _ in range(9)]
        self.winner = None # Initial status of the game , no winner

    def print_currentboard(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
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

    def take_a_move(self,square,letter):
        # take_a_move is to update the self.board. The parameter required is letter --- the symbol which will fill the spot
        # and square which is the spot gonna be filled
        # For this method , we don't need return anything for taking a move. It just updates the board
        # In this case, we can return a boolean for checking if the take_a_move did happen
        if self.board[square] == ' ':    
            self.board[square] = letter
            if self.win(square,letter):
                self.winner = letter
            return True
        else:
            return False    





    # create a method to check if the move leads to a win
    def win(self,square,letter):

        # check rows, we only check the row where the square locates
        row_ind = square // 3
        row_list = self.board[3 * row_ind: 3 * (row_ind + 1)]
        if all([spot == letter for spot in row_list]):
            return True
        
        # check columns
        column_ind = square % 3
        column_list = [self.board[column_ind + 3 * i] for i in range(3)]
        if all([spot == letter for spot in column_list]):
            return True
                

        # check diagonals. only if square in spot [0,2,4,6,8] will lead to a win.
        if square in [0,2,4,6,8]:
            if all([self.board[i] == letter for i in [0,4,8]]):
                return True
            
            if all([self.board[i] == letter for i in [2,4,6]]):
                return True

        return False




# Let's initiate a game

def play(game,x_player,o_player, print_board = True):
    if print_board == True:
        game.gameboard_num()

    # the game class need a initial parameter letter.
    letter = "X" # starting letter

    while not game.win or len(game.available_spot) != 0:
        if letter == 'X':
            square = x_player.nextmove(game)
        else:
            square = o_player.nextmove(game)
        
        # In stead directly call take_a_move, I can call a condition 
        if game.take_a_move(square,letter): # check if the take_a_move is valid, and 
                                    # meantime calling the method triggering update the board

            if print_board:
                print(letter + f' makes a move to spot {square}')
                game.print_currentboard()
                print(' ')
        # after take a moving we should check if the game is over. check current winner
            if game.winner: # winner is not None
                print('The winner is '+ letter)
                return letter # exit the function means end the game
        #after one player take a move, we need to switch the player
        letter = 'X' if letter == 'O' else 'O'      
    

    # need a while loop
    if print_board:
        print('It\'s a tie game')



    
