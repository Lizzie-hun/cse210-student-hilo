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
        self.score = self.get_points()
        self.guess = ""
        self.dealer = Dealer()

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.keep_playing:
            self.do_outputs()
            self.is_game_over()

    def is_game_over(self):
        """
        Determines if game is over or not. Criteria, if total points equal 0

        Args: 
            self (Director): an instance of Director.
            score: Total score
        """
        if self.total_score == 0:
            print('Game over')
            self.keep_playing == False

    def get_points(self):
        if self.dealer.flipped_card > self.dealer.next_card and self.dealer.guess == "l" or self.dealer.flipped_card < self.dealer.next_card and self.dealer.guess == "h":
            return 100
        else:
            return -75
    
    #updates score
    def do_updates(self):
        points = self.score
        self.total_score += points
    
    #outputs information for the game to the user
    def do_outputs(self):
        self.dealer.flip_card()
        print(f"\nThe card is: {self.dealer.current_card}")
        self.dealer.get_guess()
        print(f"Next card was: {self.dealer.next_card}")
        if self.total_score > 0:
            self.do_updates()
            print(f"Your score is: {self.total_score}")
            if self.keep_playing:
                choice = input("Draw again? [y/n] ")
                if choice == "n":
                    self.keep_playing = False
                print(f"Your score is: {self.total_score}")
                print("Thanks for playing!")
                

