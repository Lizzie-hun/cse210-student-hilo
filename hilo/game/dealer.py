#file for dealer

#Draw Cards and Get Points, class = Dealer, 
import random

class Dealer():

    def __init__(self):
        self.flipped_card = 0
        self.current_card = 0
        self.next_card = 0
        self.guess = ""
    
    def get_guess(self):
        self.guess = input("Higher or lower? [h/l] ")
        


    def flip_card(self):
        self.current_card = random.randint(1, 13)
