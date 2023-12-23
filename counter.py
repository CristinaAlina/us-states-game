from turtle import Turtle

INITIAL_SECONDS = 0
INITIAL_MINUTES = 10


class Counter(Turtle):
    def __init__(self):
        super().__init__()
        self.seconds = INITIAL_SECONDS
        self.minutes = INITIAL_MINUTES
        self.hideturtle()
        self.penup()
        self.write(F"Guess all the states within {INITIAL_MINUTES} minutes!\n       Press \"Enter\" to START",
                   align="center", font=("Courier", 20, "bold"))
        self.goto(150, 200)

    def time_is_up(self):
        """Displays an info message for user if time is up"""
        self.goto(0, 15)
        self.write(f"Time is up. Game over!", align="center", font=("Courier", 15, "bold"))

    def show_left_counter(self):
        """Displays a live timer for user to see how much time has left to complete the challenge"""
        self.clear()
        if self.seconds == 0 and self.minutes != 0:
            self.seconds = 59
            self.minutes -= 1
        self.write(f"Left time: 0{self.minutes}:{self.seconds if self.seconds >= 10 else "0" + str(self.seconds)}",
                   align="left", font=("Courier", 15, "bold"))
        self.seconds -= 1
