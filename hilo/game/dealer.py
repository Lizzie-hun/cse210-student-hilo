#file for dealer

#Draw Cards and Get Points, class = Dealer, 
import random

class Dealer():

    def __init__(self):
        self.score = 0
        self.flipped_card = 0
        self.current_card = 0
        self.next_card = 0
        self.guess = ""
    
    def get_guess(self):
        self.guess = input("Higher or lower? [h/l] ")
        

        #This needs to add 100 points to the total score and subtract 75 for each wrong guess
        #Once the score reaches 0 the game is over

    def flip_card(self):
        self.current_card = random.randint(1, 13)
        self.flipped_card = self.current_card
        self.next_card = random.randint(1, 13)
