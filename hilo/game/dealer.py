#file for dealer

#Draw Cards and Get Points, class = Dealer, 
import random
from game.director import Director

class Dealer():

    def __init__(self, playing):
        self.playing = playing
        self.score = 300
        self.flipped_card = 0
        self.current_card = 0
        self.flip = []
        self.director = Director()

    def get_points(self):
        while self.score > 0:
            if self.flipped_card > self.current_card and self.director.guess == "l" or self.flipped_card < self.current_card and self.dealer.guess == "h":
                self.score = self.score + 100
            else:
                self.score = self.score - 75
        

        #This needs to add 100 points to the total score and subtract 75 for each wrong guess
        #Once the score reaches 0 the game is over

def flip_card(self):
        self.card.clear()
        for i in range(13):
            result = random.randint(1, 13)
            self.card.append(result)
        flipped_card = {self.current_card}