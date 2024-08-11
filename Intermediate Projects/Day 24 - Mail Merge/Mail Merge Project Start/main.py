with open("./Input/Names/invited_names.txt", mode="r") as invited:
    guests = invited.readlines()

for n in range(len(guests)):
    guests[n] = guests[n].strip("\n")

with open("./Input/Letters/starting_letter.txt", mode="r") as letter:
    template = letter.read()
template = template.replace("Angela", "Colin")

for guest in guests:
    with open(f"./Output/ReadyToSend/letter_for_{guest}.txt", mode="w") as draft:
        template = template.replace("[name]", guest)
        draft.write(template)
        template = template.replace(guest, "[name]")
