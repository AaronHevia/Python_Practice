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
timer = None
reps = 0


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    reps = 0
    title_label.config(text='Timer', fg=GREEN)
    relay_label.config(text='')
    canvas.itemconfig(timer_text, text='00:00')


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    work_time = WORK_MIN * 60
    break_time = SHORT_BREAK_MIN * 60
    long_break_time = LONG_BREAK_MIN * 60
    global reps
    reps += 1
    print(reps)
    if reps % 8 == 0:
        count_down(long_break_time)
        title_label.config(text='Break', fg=RED)
    elif reps % 2 == 0:
        count_down(break_time)
        title_label.config(text='Break', fg=PINK)
    else:
        count_down(work_time)
        title_label.config(text='Work', fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minutes = math.floor(count / 60)
    minutes = '{:02d}'.format(minutes)
    seconds = count % 60
    seconds = '{:02d}'.format(seconds)

    canvas.itemconfig(timer_text, text=f'{minutes}:{seconds}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ''
        sessions = math.floor(reps / 2)
        for _ in range(sessions):
            marks += '✔'
        relay_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text='Timer', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, 'bold'))
title_label.grid(column=1, row=0)

start_button = Button(text='Start', font=(FONT_NAME, 18), command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', font=(FONT_NAME, 18), command=reset_timer)
reset_button.grid(column=2, row=2)

relay_label = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, 'bold'))
relay_label.grid(column=1, row=3)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

window.mainloop()
