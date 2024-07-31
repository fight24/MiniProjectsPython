from tkinter import *
import pandas
import random
to_learn = {}
try:
    dataFrame = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError as e:
    dataFrame = pandas.read_csv("./data/french_words.csv")
    to_learn = dataFrame.to_dict(orient="records")
else:
    to_learn = dataFrame.to_dict(orient="records")
BACKGROUND_COLOR = "#B1DDC6"
FONT_BOLD = ("Ariel", 60, "bold")
FONT_ITALIC = ("Ariel", 40, "italic")
current_card = {}


# ---------------------------- Pick a random French word/translation ------------------------------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    print(current_card)
    title_name = "French"
    random_word = current_card[title_name]
    canvas.itemconfig(img_card, image=card_font)
    canvas.itemconfig(title, text=f"{title_name}", fill="black")
    canvas.itemconfig(word, text=f"{random_word}", fill="black")
    flip_timer = window.after(3000, flip_card)

#
#
# def eng_card(r):
#     canvas.itemconfig(img_card, image=card_back)
#     canvas.itemconfig(title, fill="white", text="English")
#     canvas.itemconfig(word, fill="white", text=f"{r['English']}")
#     print("Back card")


def flip_card():
    canvas.itemconfig(img_card, image=card_back)
    canvas.itemconfig(title, fill="white", text="English")
    canvas.itemconfig(word, fill="white", text=f"{current_card['English']}")
    print("English card")


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    save_file(to_learn)
    next_card()


def save_file(works_to_learn):
    words_to_learn_df = pandas.DataFrame(works_to_learn)
    words_to_learn_df.to_csv("./data/words_to_learn.csv", index=False)


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
# data_list = next_card()
# window.after(3000, eng_card, data_list)
btn_w = Button(image=img_button_w, highlightthickness=0, bg=BACKGROUND_COLOR, bd=0, relief="flat", command=next_card)
btn_w.grid(column=0, row=1)

btn_r = Button(image=img_button_r, highlightthickness=0, bg=BACKGROUND_COLOR, bd=0, relief="flat", command=is_known)
btn_r.grid(column=1, row=1)
flip_timer = window.after(3000, flip_card)
next_card()
window.mainloop()

