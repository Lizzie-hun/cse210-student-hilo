#Draw Cards and Get Points, class = Dealer, 
import random


class Dealer():

    def __init__(self, playing):
        self.playing = playing
        self.score = 300
        self.card = []
        self.flip = []
<<<<<<< HEAD
        self.guess = []

    #def can_flip(self):
        #return(self.flip.count(300)>= 0)
            #if yes continue playing and flip a card, if no, end the game.

=======
        
>>>>>>> ed26b1f85cab66d6f7f87daedcc0bd33f2c402f0

def get_points(self):

        #This needs to add 100 points to the total score and subtract 75 for each wrong guess
        #Once the score reaches 0 the game is over

    pass


def flip_card(self):
    self.card.clear()
    for i in range(13):
        result = random.randint(1, 13)
        self.card.append(result)

    
>>>>>>> ed26b1f85cab66d6f7f87daedcc0bd33f2c402f0
