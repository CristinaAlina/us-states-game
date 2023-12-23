from turtle import Screen
import turtle
import keyboard
from counter import Counter
from scoreboard import Scoreboard
from states import States

TOTAL_NUM_STATES = 50

screen = Screen()
screen.title("U.S. States Game")
screen.setup(width=725, height=491)

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)

scoreboard = Scoreboard()
states = States()
counter = Counter()
screen.update()
keyboard.wait("Enter")

time_is_up = False
all_states_are_guesses = False


def run_counter():
    if counter.seconds >= 0 and not all_states_are_guesses:
        counter.show_left_counter()
        screen.ontimer(fun=run_counter, t=1000)


run_counter()

while not time_is_up and not all_states_are_guesses:
    screen.update()
    if counter.seconds >= 0 and counter.minutes >= 0:
        answer_state = screen.textinput(title=f"{scoreboard.num_correct_guesses()}/{TOTAL_NUM_STATES} States Correct",
                                        prompt="Enter a state name:").title()
        if answer_state == "Exit":
            states.export_states_to_learn(scoreboard.correct_guesses)
            scoreboard.exit()
            break
        if answer_state not in scoreboard.correct_guesses:
            if states.locate_guessed_state(answer_state):
                scoreboard.add_guessed_state(answer_state)
        if scoreboard.num_correct_guesses() == TOTAL_NUM_STATES:
            all_states_are_guesses = True
            scoreboard.all_states_guessed()
            screen.title(f"{scoreboard.num_correct_guesses()}/{TOTAL_NUM_STATES} States Correct")
    else:
        time_is_up = True
        screen.title(f"{scoreboard.num_correct_guesses()}/{TOTAL_NUM_STATES} States Correct")
        states.show_left_states(scoreboard.correct_guesses)
        counter.time_is_up(scoreboard.num_correct_guesses(), TOTAL_NUM_STATES)


screen.exitonclick()
