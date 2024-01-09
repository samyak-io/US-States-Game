import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. STATES GAME")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_data = pandas.read_csv("50_states.csv")

guessed_states = []

all_states = state_data.state.to_list()

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Correct Guesses",
                                    prompt="What's another state's name? ").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)

        state_row = state_data[state_data.state == answer_state]
        x = state_row['x'].values[0]
        y = state_row['y'].values[0]

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x, y)
        t.write(answer_state, font=("Helvetica", 10, "normal"))

    else:
        print(f"{answer_state} state doesn't exist in the U.S.")


turtle.mainloop()
