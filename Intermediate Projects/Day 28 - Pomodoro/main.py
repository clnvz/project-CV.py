from tkinter import *
from math import floor

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25  # 1,3,5,7
SHORT_BREAK_MIN = 5  # 2,4,6
LONG_BREAK_MIN = 20  # 8
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_txt, text="00:00")
    top_text.config(text="Timer")
    progress.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:  # Long Break
        count_down(LONG_BREAK_MIN * 60)
        top_text.config(text="Break", fg=RED, font=(FONT_NAME, 35, "bold"))
    elif reps % 2 == 0:  # Short Break
        count_down(SHORT_BREAK_MIN * 60)
        top_text.config(text="Break", fg=PINK, font=(FONT_NAME, 35, "bold"))
    else:  # Work
        count_down(WORK_MIN * 60)
        top_text.config(text="Work", fg=GREEN, font=(FONT_NAME, 35, "bold"))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    min_left = floor(count / 60)
    sec_left = count % 60
    if sec_left < 10:
        sec_left = f"0{sec_left}"
    canvas.itemconfig(timer_txt, text=f"{min_left}:{sec_left}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        checkmarks = ""
        cycles = floor(reps / 2)
        for _ in range(cycles):
            checkmarks += "✔"
        progress.config(text=checkmarks)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_txt = canvas.create_text(100, 133, text="00:00", font=(FONT_NAME, 27, "bold"), fill="white")
canvas.grid(column=1, row=1)

# Labels
top_text = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
top_text.grid(column=1, row=0)
progress = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
progress.grid(column=1, row=3)

# Buttons
start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)
reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=2)

window.mainloop()
