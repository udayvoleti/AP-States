import turtle
import pandas
screen = turtle.Screen()
screen.title("Indian States")
image = "india.gif"
screen.addshape(image)
turtle.shape(image)

'''def get_coor(x, y):
    print(x, y)

screen.onscreenclick(get_coor)

turtle.mainloop()'''
data = pandas.read_csv("indian_states.csv")
all_states = data.state.to_list()
print(all_states)
guessed_states = []

while len(guessed_states) < 29:
    guess_f = screen.textinput(title=f"{len(guessed_states)}/27 States Correct", prompt="Enter the state name?").title()
    print(guess_f)

    if guess_f == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        #for state in all_states:
         #   if state not in guessed_states:
          #      missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        print(missing_states)
        break

    if guess_f in all_states:
        guessed_states.append(guess_f)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_info = data[data["state"] == guess_f]
        print(state_info)
        t.goto(float(state_info.x), float(state_info.y))
        t.write(guess_f)
