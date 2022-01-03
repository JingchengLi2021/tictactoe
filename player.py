#define a class as player (superclass)
import random

class player:
    def __init__(self,letter):
        self.letter = letter
    


    
class humanplayer(player):

    def __init__(self,letter):
        super().__init__(letter)

    def nextmove(self,game):
        
        valid_move = False
        # we need to choose a valid spot 
        # a valid spot should be a number within the available list
        spot_choose = input(self.letter + '\'s turn . Input move(0-8):')
        # need valid input, using try
        while valid_move != True:
            try:
                spot_choose = int(spot_choose) # if not integer, will raise a TypeError
                if spot_choose not in game.available_spot():
                    raise ValueError
                valid_move = True

            except ValueError:
                #print('Invalid input, please choose a number again!')
                spot_choose = input('Invalid input,please choose a number again')

        return spot_choose        



class computerplayer(player):

    def __init__(self,letter):
        super().__init__(letter)

    def nextmove(self,game):
        # take a random available spot
        spot_choose = random.choice(game.available_spot())
        return spot_choose




