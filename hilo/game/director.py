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
        self.score = 0
        self.dealer = Dealer()
        self.guess = ""

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.keep_playing:
            self.do_updates()
            self.do_outputs()
            self.is_game_over()

    def is_game_over(self, score):
        """
        Determines if game is over or not. Criteria, if total points equal 0

        Args: 
            self (Director): an instance of Director.
            score: Total score
        """
        if score == 0:
            print('Game over')
            self.keep_playing == False
    
    #updates score
    def do_updates(self):
        points = self.dealer.get_points()
        self.score += points
    
    #outputs information for the game to the user
    def do_outputs(self):
        print(f"/nThe card is: {self.dealer.flipped_card}")
        self.dealer.get_guess()
        print(f"Next card was: {self.dealer.current_card}")
        print(f"Your score is: {self.score}")
        if self.keep_playing():
            choice = input("Draw again? [y/n] ")
            self.keep_playing = (choice == "y")
        else:
            self.keep_playing = False

