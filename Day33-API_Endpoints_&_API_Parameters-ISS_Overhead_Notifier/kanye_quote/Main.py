# import requests
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
#
# response.raise_for_status()
# print(response.json())
# print(type(response))
# # if response.status_code == 404:
# #     raise Exception("Error Not found")
# ------------------------------------------------------------------------#
from tkinter import *
import requests


# -------------------Method----------------
def get_quote():
    response = requests.get(url="https://api.kanye.rest/")
    # if response.status_code == 200:
    #     data = response.json()
    #     canvas.itemconfig(quote_text, text=data["quote"])
    response.raise_for_status()
    data = response.json()
    canvas.itemconfig(quote_text, text=data["quote"])


# -------------------- UI -----------------
window = Tk()
window.title("Kanye says ... ")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
bg_img = PhotoImage(file="img/background.png")
canvas.create_image(150, 207, image=bg_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes Here", width=250, font=("Arial", 20, "bold"),
                                fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="img/kanye.png")
kanye_btn = Button(image=kanye_img, highlightthickness=0, border=0, command=get_quote)
kanye_btn.grid(row=1, column=0)
window.mainloop()