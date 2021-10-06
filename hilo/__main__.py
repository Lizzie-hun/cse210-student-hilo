# TODO: Add entry point code here

#Draw Cards and Get Points, class = Dealer, 
import random


class Dealer():

    def __init__(self, playing):
        self.playing = playing
        self.score = 300
        self.card
        self.flip = []


    #def can_flip(self):
        #return(self.flip.count(300)> 0)
            #if yes continue playing and flip a card, if no, end the game.


def get_points(self):

        #This needs to add 100 points to the total score and subtract 75 for each wrong guess
        #Once the score reaches 0 the game is over

    


    def flip_card(self):

        self.card.clear()
        for i in range(13):
            result = random.randint(1, 13)
            self.card.append(result)
