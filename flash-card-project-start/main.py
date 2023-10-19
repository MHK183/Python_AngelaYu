from tkinter import Tk, PhotoImage, Button, Canvas
import random
import pandas as pd


BACKGROUND_COLOR = "#B1DDC6"
random_word = {}

try:
    data = pd.read_csv('data/words_to_learn.csv').to_dict(orient="records")
except FileNotFoundError:
    data = pd.read_csv('data/french_words.csv').to_dict(orient="records")

print(len(data))


def next_card():
    global random_word, flip_timer
    window.after_cancel(flip_timer)
    random_word = random.choice(data)

    canvas.itemconfig(title_text, text='French', fill="black")
    canvas.itemconfig(word_text, text=random_word['French'], fill="black")
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, flip_card)


def is_known():
    data.remove(random_word)
    d = pd.DataFrame(data)
    d.to_csv("data/words_to_learn.csv", index=False)
    next_card()


def flip_card():
    canvas.itemconfig(title_text, text='English', fill="white")
    canvas.itemconfig(word_text, text=random_word['English'], fill="white")
    canvas.itemconfig(card_background, image=card_back_image)

# ------------- UI ------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_image)
title_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)



# Buttons
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, bd=0, command=is_known)
right_button.grid(row=1, column=1)
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, bd=0, command=next_card)
wrong_button.grid(row=1, column=0)

next_card()

window.mainloop()

