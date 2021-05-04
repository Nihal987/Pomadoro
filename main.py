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
timer = None
count = 0
pause = True
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global pause
    global reps
    global count 

    window.after_cancel(timer)
    pause = True
    reps = 0
    count = 0
    pause_btn['text'] = "Pause"
    title.config(text="Title",fg=GREEN)
    check_marks.config(text="")
    canvas.itemconfig(timer_text, text="00:00")

# ---------------------------- PAUSE TIMER ------------------------------- # 
def pause_timer():
    global pause
    global count
    global timer
    if not timer:
        return
    if pause:
        pause = False
        window.after_cancel(timer)
        pause_btn['text'] = "Resume"
    else:
        pause = True
        pause_btn['text'] = "Pause"
        timer = window.after(1000,count_down)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    global count

    work_time = WORK_MIN*60
    short_break = SHORT_BREAK_MIN*60
    long_break = LONG_BREAK_MIN*60

    reps += 1

    if reps%2 !=0:
        # count_down(work_time)
        count = work_time
        title.config(text="Work",fg=GREEN)
    elif reps %8==0:
        title.config(text="Break",fg=RED)
        # count_down(long_break)
        count = long_break
    else:
        title.config(text="Break",fg=PINK)
        # count_down(short_break)
        count = short_break
    count_down()
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down():
    global count
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds<10:
        seconds = "0"+str(seconds)
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    
    if count>0:
        global timer
        count -= 1
        timer = window.after(1000,count_down)
    elif count==0:
        start_timer()
        no_ticks = math.floor(reps/2)
        ticks = "🍅" * no_ticks
        check_marks.config(text=ticks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomadoro")
window.config(padx=100,pady=50, bg=YELLOW)

#Canvas
canvas = Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato)
timer_text = canvas.create_text(103,130,text="00:00",fill="white",font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2,row=2)

#Title
title = Label(text="Timer",font=(FONT_NAME,50,"bold"),fg=GREEN,bg=YELLOW)
title.config(pady=5)
title.grid(column=2,row=1)

#Buttons
start = Button(text="Start",font=(FONT_NAME,12,"bold"),command=start_timer)
start.grid(column=1,row=5)

reset = Button(text="Reset",font=(FONT_NAME,12,"bold"),command=reset_timer)
reset.grid(column=3,row=5)

pause_btn = Button(text="Pause",font=(FONT_NAME,12,"bold"),command=pause_timer)
pause_btn.grid(column=2,row=5)

#Checkmark
check_marks = Label(text="",font=(FONT_NAME,12,"bold"),bg=YELLOW,fg=RED,pady=10)
check_marks.grid(column=2,row=4)

window.mainloop()