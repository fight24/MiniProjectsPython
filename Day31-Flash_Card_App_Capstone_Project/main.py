from tkinter import *
import pandas
import random
import time
dataFrame = pandas.read_csv(r"E:\down\python_100days\practice_py_100days\100DaysPython\Day31"
                            r"-Flash_Card_App_Capstone_Project\data\french_words.csv")
to_learn = dataFrame.to_dict(orient="records")
BACKGROUND_COLOR = "#B1DDC6"
FONT_BOLD = ("Ariel", 60, "bold")
FONT_ITALIC = ("Ariel", 40, "italic")
c = 0


# ---------------------------- Pick a random French word/translation ------------------------------- #
def next_card():
    global c
    print(random.choice(to_learn))
    random_data = random.choice(to_learn)
    title_name = "French"
    random_word = random_data[title_name]
    canvas.itemconfig(title, text=f"{title_name}")
    canvas.itemconfig(word, text=f"{random_word}")
    if c > 0:
        time.sleep(3)
        back_card(random_data)
    c += 1


def back_card(r):
    canvas.itemconfig(img_card, image=card_back)
    canvas.itemconfig(title, fill="white", text="English")
    canvas.itemconfig(word, fill="white", text=f"{r['English']}")
    print("Back card")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_back = PhotoImage(file="./images/card_back.png")
card_font = PhotoImage(file="./images/card_front.png")
img_button_w = PhotoImage(file="./images/wrong.png")
img_button_r = PhotoImage(file="./images/right.png")

canvas = Canvas(window, width=800, height=526, highlightthickness=0, bd=0, bg=BACKGROUND_COLOR)
img_card = canvas.create_image(400, 263, image=card_font)
title = canvas.create_text(400, 150, text="Title", font=FONT_ITALIC)
word = canvas.create_text(400, 263, text="Word", font=FONT_BOLD)
canvas.grid(column=0, row=0, columnspan=2)
next_card()
btn_w = Button(image=img_button_w, highlightthickness=0, bg=BACKGROUND_COLOR, bd=0, relief="flat", command=next_card)
btn_w.grid(column=0, row=1)

btn_r = Button(image=img_button_r, highlightthickness=0, bg=BACKGROUND_COLOR, bd=0, relief="flat", command=next_card)
btn_r.grid(column=1, row=1)

window.mainloop()

