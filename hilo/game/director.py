from game.dealer import Dealer

class Director:


    #gets inputs at the beginning of each round. for this that would be the guess
    def get_inputs(self):
        self.dealer.guess_card()
    
    #updates score
    def do_updates(self):
        points = self.dealer.get_points()
        self.score += points
    
    #outputs information for the game to the user
    def do_outputs(self):
        print(f"/nThe care is: {self.dealer.current_card}")
        self.guess = input("Higher or lower? [h/l] ")
        print(f"Next card was: {self.dealer.next_card}")
        print(f"Your score is: {self.score}")
        if self.dealer.can_continue():
            choice = input("Roll again? [y/n] ")
            self.keep_playing = (choice == "y")
        else:
            self.keep_playing = False