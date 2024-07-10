import tkinter
import turtle

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=500)
window.config(padx=100, pady=200)
# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label.pack()
my_label.grid(column=0, row=0)
my_label["text"] = "new text"
my_label.config(text="New text")
index = 0


def button_clicked():
    global index
    index += 1
    print("I got clicked")
    my_label["text"] = input_entry.get()
    print(input_entry.get())
    # my_label.config(text=f"Clicked {index}")


# button
new_button = tkinter.Button(text="new button", fg="white", bg="black", command=button_clicked)
new_button.grid(column=2, row=0)
# Entry
input_entry = tkinter.Entry()
# input_entry.pack()
input_entry.grid(column=3, row=2)
print(input_entry.get())
# Button
button = tkinter.Button(text="Click Me", fg="white", bg="black", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)
# # text
# text = tkinter.Text(width=30, height=5)
# # # Puts cursor in textbox
# text.focus()
# # # adds some text to begin with.
# text.insert(tkinter.END, "Example of multi-line text entry.")
# # #  gets current value in textbox at line 1, character 0
# print(text.get("1.0", tkinter.END))
# text.pack()
#
#
# # spin box
# def spinbox_used():
#     print(spinbox.get())
#
#
# spinbox = tkinter.Spinbox(from_=0, to=10, width=5,command=spinbox_used)
# spinbox.pack()
#
#
# # Scale
# def scale_used(value):
#     print(value)
#
#
# scale = tkinter.Scale(from_=0, to=100, command=scale_used)
# scale.pack()
#
#
# # check button
# def checkbutton_used():
#     print(check_state.get())
#
#
# check_state = tkinter.IntVar()
# check_button = tkinter.Checkbutton(text="Is On?",variable=check_state,command=checkbutton_used)
# check_button.pack()
#
#
# # radioButton
# def radio_used():
#     print(radio_state.get())
#
#
# radio_state = tkinter.IntVar()
# radio_option1 = tkinter.Radiobutton(text="Option 1", value=1, variable=radio_state, command=radio_used)
# radio_option2 = tkinter.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radio_option1.pack()
# radio_option2.pack()
#
#
# # listbox
# def listbox_used(event):
#     print(listbox.get(listbox.curselection()))
#
#
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# listbox = tkinter.Listbox(height=4)
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()
window.mainloop()

# tim = turtle.Turtle()
# tim.write()

# # Unlimited Arguments
#
#
# def add(*args):
#     for n in args:
#         print(n)
#
#
# add(1)
# add(1, 2)
# PACK PLACE GRID

