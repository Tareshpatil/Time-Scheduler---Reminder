import tkinter
import threading
from tkinter import messagebox
import sys
from time import strftime


tasks = []
timer = threading
real_timer = threading
ok_thread = True






def get_entry(event=""):
    text = todo.get()
    hour = int(time.get())*60

    todo.delete(0, tkinter.END)
    time.delete(0, tkinter.END)
    todo.focus_set()
    add_list(text, hour)
    if 0 < hour < 999:
        update_list()


def add_list(text, hour):
    tasks.append([text, hour])
    timer = threading.Timer(hour, time_passed, [text])
    timer.start()


def update_list():
    if todolist.size() > 0:
        todolist.delete(0, "end")
    for task in tasks:
        todolist.insert("end", "[" + task[0] + "] Time left : " + str(task[1]) + "seconds")

def update_label():
    current_time = strftime('%a %dth %B %Y \nTime: %I: %M: %S %p')
    clock_label.configure(text = current_time)
    clock_label.after(80, update_label)

def time_passed(task):
    tkinter.messagebox.showinfo("Notification", "It's " + strftime('%I: %M: %S %p') + "  Time for : " + task )


def real_time():
    if ok_thread:
        real_timer = threading.Timer(1.0, real_time)
        real_timer.start()
    for task in tasks:
        if task[1] == 0:
            tasks.remove(task)
        task[1] -= 1
    update_list()








if __name__ == '__main__':
    # application
    app = tkinter.Tk()

    app.geometry("1260x780")
    app.title("Task Schedular & Reminder")
    app.rowconfigure(0, weight=1)


    # fenetre
    frame = tkinter.Frame(app)
    frame.pack()

    # widgets
    label = tkinter.Label(app, text="Enter work to do:",
                          wraplength=200,
                          justify=tkinter.LEFT)
    label_hour = tkinter.Label(app, text="Enter time (Minutes):",
                               wraplength=200,
                               justify=tkinter.LEFT)
    todo = tkinter.Entry(app, width=30)
    info_head = tkinter.Label(app, text="?Steps to Use this app:-", font=("Serif", 18))
    info_points = tkinter.Label(app, text="? This app reminds user the task which is to be performed in his/her routine.\r\n? Enter the task which user wants to perform.\r\n? Enter the time interval after which the task is to be performed.\n   You can refer to the provided Digital Clock.\n\r? Click on the start button. Desired work will be visible on screen\n   along with the countdown timer.\r\n? As the timer ends, user will be notified with a pop up that will\n   indicate user the time and task.\r\n? You can add multiple tasks with same process by clicking on 'Add Task' button.", justify= 'left', font=("Serif", 13))
    top_head = tkinter.Label(app, text="Welcome to TSR Application!", font=("Serif", 25, "bold"), fg='#fc6f03')

    grp_head = tkinter.Label(app, text="Made by: Taresh patil", font=("DUBIELPLAIN", 21, "bold"))

    time = tkinter.Entry(app, width=30)
    send = tkinter.Button(app, text='Add task', fg="#ffffff", bg='#6186AC', height=3, width=30, command=get_entry)
    quit = tkinter.Button(app, text='Exit', fg="#ffffff", bg='#EB6464', height=3, width=30, command=app.destroy)
    clock_label = tkinter.Label(app, fg="black", font=("Valencia Typeface", 20), relief='flat')
    todolist = tkinter.Listbox(app)
    if tasks != "":
        real_time()




    # binding
    app.bind('<Return>', get_entry)

    # widgets placement
    label.place(x=648, y=65, width=200, height=25)
    label_hour.place(x=873, y=65, width=200, height=25)
    todo.place(x=703, y=85, width=200, height=25)
    time.place(x=918, y=85, width=150, height=25)
    send.place(x=703, y=120, width=50, height=25)
    quit.place(x=1017, y=470, width=50, height=25)
    todolist.place(x=703, y=155, width=365, height=300)
    info_head.place(x=80, y=180)
    info_points.place(x=80, y=220)
    top_head.place(x=80, y=5, width=1000)
    grp_head.place(x=80, y=550, width=1000, height=125)


    clock_label.place(x=80, y=80, height=60)
    update_label()

    app.mainloop()

    ok_thread = False
    sys.exit("FINISHED")

