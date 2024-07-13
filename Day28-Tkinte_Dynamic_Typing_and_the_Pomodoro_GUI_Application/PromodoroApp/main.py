from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = ''


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    # timer_text 00:00
    canvas.itemconfig(timer_text, text="00:00")
    # title_label "Timer"
    label_timer.config(text="Timer")
    label_check_mark.config(text="")
    # reset check_marks
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_bread_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1
    if reps % 2 != 0:
        # if it's the 1st/3rd/5th/7th rep:
        count_down(work_sec)
        label_timer.config(text="Work", fg=GREEN)
    elif reps % 8 == 0:
        # if it's the 8th rep:
        count_down(long_break_sec)
        label_timer.config(text="Break", fg=RED)
    else:
        # if it's 2nd/4th/6th
        count_down(short_bread_sec)
        label_timer.config(text="Break", fg=PINK)
    print(reps)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    print(count)
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if int(count_sec) < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        label_check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# label
label_timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
label_timer.grid(column=1, row=0)

label_check_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 18, "bold"))
label_check_mark.grid(column=1, row=3)

# button
start_btn = Button(text="Start", fg="black", bg="white", font=(FONT_NAME, 12, "bold"),
                   highlightthickness=0, command=start_timer)
reset_btn = Button(text="Reset", fg="black", bg="white",
                   font=(FONT_NAME, 12, "bold"), highlightthickness=0, command=reset_timer)
start_btn.grid(column=0, row=2)
reset_btn.grid(column=2, row=2)
window.mainloop()
