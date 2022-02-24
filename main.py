from tkinter import *
import math
from playsound import playsound 

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
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    timer_label.config(text='Timer')
    check_mark.config(text='')
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def starter():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break)
        timer_label.config(text='break', fg=RED)
    elif reps % 2 == 0:
        count_down(short_break)
        timer_label.config(text='break', fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text='Work', fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        #playsound('beep.mp3')
        starter()
        marks = ''
        work_session = math.floor(reps / 2)
        for _ in range(work_session):
            marks += '✔'
        check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('                                                                 pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

timer_label = Label(text='Timer', fg=GREEN, font=(FONT_NAME, 35, 'bold'), bg=YELLOW)
timer_label.grid(row=0, column=1)

start_button = Button(command=starter, text='Start', width=7)
start_button.grid(row=2, column=0)

reset_button = Button(command=reset_timer, text='Reset', width=7)
reset_button.grid(row=2, column=2)

check_mark = Label(fg=GREEN, bg=YELLOW, font='bold')
check_mark.grid(row=3, column=1)

window.mainloop()
