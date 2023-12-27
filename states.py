import pandas
from turtle import Turtle
CONTENT_FILE = "50_states.csv"
EXPORT_FILE = "states_to_learn.csv"


class States:
    def __init__(self):
        self.all_data = pandas.read_csv(CONTENT_FILE)

    def get_state_location(self, state_name):
        """Searches through all the content from csv file and returns the x and y coordinates of the state,
        or None if the state is not found in the list"""
        state_data = self.all_data[self.all_data.state == state_name]
        if len(state_data) > 0:
            state_x = int(state_data.x.iloc[0])
            state_y = int(state_data.y.iloc[0])
            return state_x, state_y
        else:
            return None

    def locate_guessed_state(self, state_name):
        """Writes the state on the specific location on the map if state is found in the csv content"""
        state = Turtle()
        state.penup()
        state.hideturtle()
        position = self.get_state_location(state_name)
        if position is not None:
            state.goto(position)
            state.write(f"{state_name}", align="center", font=("Courier", 7, "normal"))
            return True
        else:
            return False

    def show_left_states(self, guessed_list):
        """Writes all the not guessed states on the map"""
        for state_name in self.all_data.state:
            if state_name not in guessed_list:
                state = Turtle()
                state.penup()
                state.hideturtle()
                state.color("red")
                position = self.get_state_location(state_name)
                state.goto(position)
                state.write(f"{state_name}", align="center", font=("Courier", 7, "normal"))

    def export_states_to_learn(self, guessed_list):
        """Generates an export with all the states that are not guessed till the calling of this function"""
        states_to_learn = [state_name for state_name in self.all_data.state if state_name not in guessed_list]
        data_to_csv = pandas.DataFrame(states_to_learn)
        data_to_csv.to_csv(EXPORT_FILE)
