#file for dealer

#Draw Cards and Get Points, class = Dealer, 
import random
from game import director

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
        while self.score > 0:
            if self.current_card > self.next_card and self.director.guess == "l" or self.current_card < self.next_card and self.dealer.guess == "h":
                self.score = self.score + 100
            else:
                self.score = self.score - 75
        

        #This needs to add 100 points to the total score and subtract 75 for each wrong guess
        #Once the score reaches 0 the game is over

    


    def flip_card(self):
        #self.current_card = self.next_card
        #self.next_card = random.randint(1, 13)
        