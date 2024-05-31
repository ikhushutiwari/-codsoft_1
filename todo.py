from tkinter import *
from tkinter import messagebox

def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")

def deleteTask():
    lb.delete(ANCHOR)

def editTask():
    try:
        selected_index = lb.curselection()[0]
        selected_task = lb.get(selected_index)
        my_entry.delete(0, END)
        my_entry.insert(END, selected_task)
        lb.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to edit.")    
    
ws = Tk()
ws.geometry('500x450+500+200')
ws.title('TO DO LIST')
ws.config(bg='#0000FF')
ws.resizable(width=False, height=False)

frame = Frame(ws)
frame.pack(pady=10)

lb = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#800080',
    highlightthickness=0,
    selectbackground='#000000',
    activestyle="dotbox",
    
)
lb.pack(side=LEFT, fill=BOTH)

task_list = [
    'write software',
    'write documentation',
    'Learn something',
    ]

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    ws,
    font=('times', 22)
    )

my_entry.pack(pady=20)

button_frame = Frame(ws)
button_frame.pack(pady=20)

addTask_btn = Button(
    button_frame,
    text='Add Task',
    font=('times 14'),
    bg='#c5f776',
    padx=20,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('times 14'),
    bg='#FFFF00',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

editTask_btn = Button(
    button_frame,
    text='Edit Task',
    font=('Times', 14),
    bg='#FFFFCC', 
    padx=20,
    pady=10,
    command=editTask
)
editTask_btn.pack(fill=BOTH, expand=True, side=LEFT)


ws.mainloop()