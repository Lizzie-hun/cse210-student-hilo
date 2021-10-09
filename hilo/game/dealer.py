import random

class Dealer():
    """
    This does something
    """

    def __init__(self):
        self.score = 0
        self.flipped_card = 0
        self.current_card = 0
        #self.previous_card = 0
        self.guess = ""
        self.previous_card = self.flipped_card

    def get_guess(self):
        self.guess = input("Higher or lower? [h/l] ")

    def flip_card(self):
        self.current_card = random.randint(1, 13)
        #self.current_card = self.previous_card
        #self.flipped_card = self.current_card
        self.flipped_card = random.randint(1,13)
        #self.previous_card = self.flipped_card
        #return self.current_card

    #self.previous = flip_card

