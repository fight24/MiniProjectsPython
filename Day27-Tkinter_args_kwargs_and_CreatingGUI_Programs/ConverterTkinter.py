from tkinter import *
ONE_MILE_TO_KM = 1.609344
window = Tk()
# window.minsize(width=300, height=100)
window.config(padx=20, pady=20)
window.title("Mile to Km Converter")


def button_clicked():
    mile_value = input_entry_mile.get()
    global value_km
    if mile_value != '':
        value_km = round(float(mile_value)*ONE_MILE_TO_KM)
    label_value_km["text"] = value_km
    print(value_km)


# entry
value_km = 0
value_mile_default = StringVar()
value_mile_default.set("0")
input_entry_mile = Entry(border=1, textvariable=value_mile_default)
input_entry_mile.grid(column=1, row=0)

# input_entry_km = Entry(border=1)
# input_entry_km.grid(column=1, row=1)
# label
label_equal = Label(text="is equal to", font=("Arial", 14, "normal"))
label_equal.grid(column=0, row=1)

label_mile = Label(text="Miles", font=("Arial", 14, "normal"))
label_mile.config(padx=10)
label_mile.grid(column=2, row=0)

label_value_km = Label(text="0", font=("Arial", 14, "normal"))
label_value_km.grid(column=1, row=1)

label_km = Label(text="Km", font=("Arial", 14, "normal"))
label_km.grid(column=2, row=1)

# Button
button = Button(text="Calculate", border=1, bg="white", fg="black", command=button_clicked)
button.grid(column=1, row=2)
window.mainloop()
