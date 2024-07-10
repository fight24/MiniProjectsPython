import turtle
import pandas
from ShowState import ShowState
data_50_states = pandas.read_csv("50_states.csv")
list_states = data_50_states.state.to_list()
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
show = ShowState()
screen.addshape(image)
turtle.shape(image)

correct_guesses = []
# TODO Use a loop to allow the user to keep guessing
while len(correct_guesses) < 50:
    # TODO Convert the guess to Title case
    answer_state = turtle.textinput(f"{len(correct_guesses)}/50 States Correct"
                                    , "What's another state name?").title()
    if answer_state == "Exit":
        break
    # TODO check if the guess is among the 50 states
    if answer_state in list_states:
        x_axis = float(data_50_states[data_50_states.state == answer_state].x.values[0])
        y_axis = float(data_50_states[data_50_states.state == answer_state].y.values[0])
        # TODO Write correct guesses onto the map
        show.show_move(answer_state, x_axis, y_axis)
        correct_guesses.append(answer_state)
        print(True)
dict_states_to_learn = {
    "states": [name for name in list_states if name not in correct_guesses]
}
print(dict_states_to_learn)
# states_to_learn.csv
save_states_to_learn = pandas.DataFrame(dict_states_to_learn)

save_states_to_learn.to_csv("states_to_learn.csv")
screen.exitonclick()
# TODO Record the correct guesses in a list
# TODO keep track of the score.
