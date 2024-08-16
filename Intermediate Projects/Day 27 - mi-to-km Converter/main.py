from tkinter import *


def convert_to_km():
    input_miles = float(entry.get())
    converted_km = round(input_miles * 1.60934, 3)
    converted.config(text=converted_km)


window = Tk()
window.title("Mile-to-Kilometer Converter")
window.config(padx=30, pady=20)

# Labels
miles = Label(text="mi.")
miles.grid(column=2, row=0)
equal_to = Label(text="is equal to")
equal_to.grid(column=0, row=1)
converted = Label(text=0)
converted.grid(column=1, row=1)
kilom = Label(text="km.")
kilom.grid(column=2, row=1)

# Entry
entry = Entry(width=7)
entry.grid(column=1, row=0)
entry.focus()

# Button
button = Button(text="Convert", command=convert_to_km)
button.grid(column=1, row=2)

window.mainloop()
