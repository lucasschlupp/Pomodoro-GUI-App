from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#72BF78"
LIGHT_GREEN = '#A0D683'
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
no_checks = ''
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    window.after_cancel(timer)
    text_timer.config(text='Timer')
    canvas.itemconfig(timer_text, text='00:00')
    check.config(text='')
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    global reps
    reps += 1
    work_s = WORK_MIN * 60
    short_b_s = SHORT_BREAK_MIN * 60
    long_b_s = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        timer_count(long_b_s)
        text_timer.config(text='BREAK', fg=RED)
    elif reps % 2 == 0:
        timer_count(short_b_s)
        text_timer.config(text='BREAK', fg=PINK)
    else:
        timer_count(work_s)
        text_timer.config(text='WORK', fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def timer_count(cont):
    global no_checks
    global timer
    minutes = cont // 60
    seconds = cont % 60
    if seconds < 10:
        seconds = f'0{seconds}'
    canvas.itemconfig(timer_text, text=f'{minutes}:{seconds}')
    if cont > 0:
        timer = window.after(1000, timer_count, cont - 1)
    else:
        start()
        if reps % 2 == 0:
            no_checks += '✔'
        check.config(text=no_checks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)


text_timer = Label(text='Timer', font=(FONT_NAME, 35, 'bold'), fg=GREEN, bg=YELLOW)
text_timer.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image_tomato = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=image_tomato)
timer_text = canvas.create_text(100, 130, text='00:00', fill=LIGHT_GREEN, font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

start_button = Button(text='Start', font=(FONT_NAME, 10, 'bold'), fg=RED, bg=LIGHT_GREEN, command=start)
start_button.grid(column=0, row=3)

reset_button = Button(text='Reset', font=(FONT_NAME, 10, 'bold'), fg=RED, bg=LIGHT_GREEN, command=reset_timer)
reset_button.grid(column=2, row=3)

check = Label(fg=GREEN, bg=YELLOW)
check.grid(column=1, row=3)

window.mainloop()