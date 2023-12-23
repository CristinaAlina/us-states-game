from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.correct_guesses = []

    def add_guessed_state(self, state_name):
        """Adds the guessed state on the list of correct guessed states"""
        self.correct_guesses.append(state_name)

    def num_correct_guesses(self):
        """Returns the length of the list of correct guessed states"""
        return len(self.correct_guesses)

    def all_states_guessed(self):
        """Displays a congrats message if the user has completed all the states on the map"""
        self.goto(0, 15)
        self.write("Congratulations! 🎉", align="center", font=("Courier", 15, "bold"))

    def exit(self):
        """Display an info message for the user that a file has been generated and to click for exit"""
        self.goto(0, 15)
        self.write("The file states_to_learn.csv has been generated.\n                 Click for Exit...",
                   align="center", font=("Courier", 15, "bold"))
