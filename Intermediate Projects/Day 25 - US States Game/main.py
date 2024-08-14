import turtle
import pandas

FONT_END = ("Arial", 20, "bold")

screen = turtle.Screen()
screen.setup(width=730, height=500)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

writer = turtle.Turtle()
writer.penup()
writer.hideturtle()

score = 0
states_raw = pandas.read_csv("50_states.csv")
all_states_list = states_raw.state.tolist()
done_guessing = []


while len(done_guessing) < 50:
    answer = []

    if score == 0:  # Starting pop-up
        answer = screen.textinput(title="Guess a state", prompt="Name a state in the U.S.").title()
    elif score == 50:  # Game over
        writer.home()
        writer.write(arg="You won! Game over", align="center", font=FONT_END)
        print("You won! Game over")
        break
    else:  # Pop-up that records number of corrected guesses
        answer = screen.textinput(title=f"[{score}/50] States correct", prompt="What's another state name?").title()

# Check if guess is correct, have already been said, or is not a state
    if answer in all_states_list:
        score += 1
        x_coor = states_raw.x[states_raw.state == answer].item()
        y_coor = states_raw.y[states_raw.state == answer].item()
        writer.goto(x_coor, y_coor)
        writer.write(answer)
        all_states_list.remove(answer)
        done_guessing.append(answer)
    elif answer == "Exit":
        not_guessed = []
        for state in all_states_list:
            if state not in done_guessing:
                not_guessed.append(state)
        pandas.DataFrame(not_guessed).to_csv("pending_guesses.csv")
        break
    elif answer in done_guessing:
        print("You've already guessed that.")
    else:
        print("That's not a state in the U.S.")
