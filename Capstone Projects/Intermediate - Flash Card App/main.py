from tkinter import *
from tkinter import messagebox
import random
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

to_learn_dict = {}
try:
    saved = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    raw_data = pd.read_csv("./data/french_words.csv")
    to_learn_dict = raw_data.to_dict(orient="records")
else:
    to_learn_dict = saved.to_dict(orient="records")
finally:
    random_word = random.choice(to_learn_dict)


# ----------------------------------------------------------
def correct_translation():
    if len(to_learn_dict) == 1:
        messagebox.showinfo(title="Congratulations!", message="There's no more to flash! (  .Y.  )")
    to_learn_dict.remove(random_word)
    pd.DataFrame(to_learn_dict).to_csv("./data/words_to_learn.csv", index=False)
    next_card()


# ----------------------------------------------------------
def next_card():
    global timer, random_word
    window.after_cancel(timer)
    random_word = random.choice(to_learn_dict)
    canvas.itemconfig(flashed_card, image=front_card)
    canvas.itemconfig(flashed_title, fill="black", text="French")
    canvas.itemconfig(flashed_word, fill="black", text=f"{random_word["French"]}")
    timer = window.after(3000, flip_card)


# ----------------------------------------------------------
def flip_card():
    back_card = PhotoImage(file="./images/card_back.png")
    canvas.itemconfig(flashed_card, image=back_card)
    canvas.itemconfig(flashed_title, fill="white", text="English")
    canvas.itemconfig(flashed_word, fill="white", text=f"{random_word["English"]}")


# ----------------------------------------------------------
window = Tk()
window.title("Flash Card Game")
window.config(padx=50, pady=30, bg=BACKGROUND_COLOR)
timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_card = PhotoImage(file="./images/card_front.png")
flashed_card = canvas.create_image(400, 270, image=front_card)
flashed_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
flashed_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
red_cross = PhotoImage(file="./images/wrong.png")
red_button = Button(image=red_cross, highlightthickness=0, bd=0, command=next_card)
red_button.grid(column=0, row=1)
green_check = PhotoImage(file="./images/right.png")
green_button = Button(image=green_check, highlightthickness=0, bd=0, command=correct_translation)
green_button.grid(column=1, row=1)

next_card()
window.mainloop()
