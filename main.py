from tkinter import *
import random


# _____________________________________password generator_______________________________________#

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(6, 10)
    nr_numbers = random.randint(4, 6)
    nr_symbols = random.randint(3, 6)

    rand_letters = [random.choice(letters) for char in range(nr_letters)]
    rand_numbers = [random.choice(numbers) for num in range(nr_numbers)]
    rand_symbols = [random.choice(symbols) for sym in range(nr_symbols)]

    password_list = rand_letters + rand_numbers + rand_symbols
    random.shuffle(password_list)

    password = "".join(password_list)

# ______________________________________UI SETUP ________________________________________________#

window = Tk()
window.title("Password Generator")

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="img.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

window.mainloop()

