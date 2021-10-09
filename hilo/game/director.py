from game.dealer import Dealer

class Director:
    
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to keep track of the score and control the 
    sequence of play.
    
    Attributes:
        keep_playing (boolean): Whether or not the player wants to keep playing.
        score (number): The total number of points earned.
        dealer (Dealer): An instance of the class of objects known as Dealer.
        guess (string): Record and hold their guess.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.keep_playing = True
        self.total_score = 300
        self.score = 0
        self.guess = ""
        self.dealer = Dealer()
        self.previous_card = 0

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.keep_playing:
            self.output_first_card()
            self.dealer.get_guess()
            self.dealer.flip_card()
            self.do_outputs()
            self.is_game_over()
            self.draw_again()
            

    def is_game_over(self):
        """
        Determines if game is over or not. Criteria, if total points equal 0

        Args: 
            self (Director): an instance of Director.
            score: Total score
        """
        if self.total_score <= 0:
            print("Better luck next time!")
            print("Game over")
            self.keep_playing = False

    def get_points(self):
        while self.total_score > 0:
            if self.dealer.current_card > self.previous_card and self.dealer.guess == "h" or self.dealer.current_card < self.previous_card and self.dealer.guess == "l":
                self.score = 100
            else:
                self.score = -75
            return self.score
    
    #updates score
    def do_updates(self):
        points = self.get_points()
        self.total_score += points
    
    #outputs first card for the game to the user
    def output_first_card(self):
        self.dealer.flip_card()
        if self.previous_card == 0:
            print("Welcome! Are you ready to play Hilo?")
            print(f"\nThe card is: {self.dealer.current_card}")
            self.transfer_card()
        elif self.previous_card != 0:
            print(f"\nThe card is: {self.previous_card}")

    #changes the card
    def transfer_card(self):
        self.previous_card = int(self.dealer.current_card)

    #asks whether the user wants to draw again
    def draw_again(self):
        if self.keep_playing:
            choice = input("Do you want to draw again? [y/n] ")
            if choice == "n":
                self.keep_playing = False
                print(f"Your score is: {self.total_score}")

    #outputs the next card and score
    def do_outputs(self):
        print(f"Next card was: {self.dealer.current_card}")
        self.get_points()
        self.do_updates()
        self.transfer_card()
        print(f"Your score is: {self.total_score}")
                

