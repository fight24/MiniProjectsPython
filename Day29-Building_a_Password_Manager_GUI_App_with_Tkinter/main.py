import random
import pyperclip
from tkinter import Tk, Canvas, PhotoImage, Label, Entry, Button, constants, messagebox

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
           'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A',
           'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
           'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
FONT_NAME = "Arial"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generator_pass():
    pass_entry.delete(0, constants.END)
    # nr_letters = random.randint(8, 10)
    # nr_symbols = random.randint(2, 4)
    # nr_numbers = random.randint(2, 4)
    # for _ in range(1, nr_letters + 1):
    #     password_list.append(random.choice(letters))
    # for _ in range(1, nr_symbols + 1):
    #     password_list.append(random.choice(symbols))
    # for _ in range(1, nr_numbers + 1):
    #     password_list.append(random.choice(numbers))
    password_list = ([random.choice(letters) for _ in range(random.randint(8, 10))] +
                     [random.choice(symbols) for _ in range(random.randint(2, 4))] +
                     [random.choice(numbers) for _ in range(random.randint(2, 4))])
    random.shuffle(password_list)
    pass_entry.insert(0, "".join(password_list))
    print(password_list)
    pyperclip.copy("".join(password_list))


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_file_data():
    website_name = website_entry.get()
    username = username_entry.get()
    password = pass_entry.get()
    if website_name and password and username:
        is_ok = messagebox.askokcancel(title=website_name, message=f"There are the details entered:\n{username} "
                                                                   f"\n{password} \nIs it oke to save?")
        if is_ok:
            lines = [f"{website_name} | ", f"{username} | ", f"{password}"]
            with open("data.txt", mode="a") as data_file:
                data_file.writelines(lines)
            data_file.close()
            website_entry.delete(0, constants.END)
            pass_entry.delete(0, constants.END)
    else:
        messagebox.showwarning(title="Oops", message="Please don't leave any field empty!")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_pass = PhotoImage(file="logo_img_com_200x200.png")
canvas.create_image(100, 100, image=logo_pass)
timer_text = canvas.create_text(100, 148, text="My Password", fill="black", font=(FONT_NAME, 13, "bold"))
canvas.grid(column=1, row=0)

# Entry and label
# #website
website_label = Label(text="Website:", font=(FONT_NAME, 14, "bold"))
website_label.grid(column=0, row=1)
website_entry = Entry(width=60)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

# # username/email
username_label = Label(text="Email/Username:", font=(FONT_NAME, 14, "bold"))
username_label.grid(column=0, row=2)
username_entry = Entry(width=60)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "@gmail.com")
# # Password
pass_label = Label(text="Password:", font=(FONT_NAME, 14, "bold"))
pass_label.grid(column=0, row=3)
pass_entry = Entry(width=40)
pass_entry.grid(column=1, row=3)
# Button for generating password
generate_pass_btn = Button(text="Generate Password", fg="black", bg="white", command=generator_pass)
generate_pass_btn.grid(column=2, row=3)

# # btn add
btn_add = Button(text="Add", fg="black", bg="white", width=20, command=save_file_data)
btn_add.grid(column=0, row=4, columnspan=3)

window.mainloop()
