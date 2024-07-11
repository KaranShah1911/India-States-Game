import turtle
import pandas

screen = turtle.Screen()
screen.title("India States Game")

image = "india_map.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("states.csv")
all_states = data["state"].to_list()

guessed_states =[]


while len(guessed_states) < 29:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/29 Guess the State",
                                    prompt="What's another state's name??").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    for state in data["state"]:
        if answer_state == state:
            if answer_state not in guessed_states:
                guessed_states.append(answer_state)
                t = turtle.Turtle()
                t.hideturtle()
                t.penup()
                state_data = data[data.state == answer_state]
                t.goto(int(state_data.x), int(state_data.y))
                t.write(arg=answer_state, font=("Arial", 10, "normal"), align="left")

    if len(guessed_states) == 29:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(0, 300)
        t.write("You've done it 👍👍", align="center", font=('Courier', 24, 'bold'))
        screen.exitonclick()


