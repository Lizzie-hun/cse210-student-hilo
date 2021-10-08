<<<<<<< HEAD
#file for dealer

=======
>>>>>>> ed26b1f85cab66d6f7f87daedcc0bd33f2c402f0
#Draw Cards and Get Points, class = Dealer, 
import random
from game import director

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
        while self.score > 0:
            if self.current_card > self.next_card and self.director.guess == "l" or self.current_card < self.next_card and self.dealer.guess == "h":
                self.score = self.score + 100
            else:
                self.score = self.score - 75
        

        #This needs to add 100 points to the total score and subtract 75 for each wrong guess
        #Once the score reaches 0 the game is over

    pass


<<<<<<< HEAD
    def flip_card(self):
        #self.current_card = self.next_card
        #self.next_card = random.randint(1, 13)
        
=======
def flip_card(self):
    self.card.clear()
    for i in range(13):
        result = random.randint(1, 13)
        self.card.append(result)

<<<<<<< HEAD
        self.card.clear()
        for i in range(13):
            result = random.randint(1, 13)
            self.card.append(result)
        flipped_card = {self.current_card}
=======
    
>>>>>>> ed26b1f85cab66d6f7f87daedcc0bd33f2c402f0
