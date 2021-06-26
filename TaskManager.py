import random, tkinter as tk
import tkinter.ttk as ttk

# Counter for IDs when inserting into table
thisDict = {}

firstClick = True
secondClick = True
thirdClick = True
fourthClick = True
fifthClick = True
sixthClick = True

def on_Entry_Click_taskName(event):
	global firstClick
	if firstClick:
		firstClick = False
		taskNameInput.delete('1.0', "end")
		taskNameInput.config(fg='black')

def on_Entry_Click_timeTaken(event):
	global secondClick
	secondClick = True
	if secondClick:
		secondClick = False
		timeTakenInput.delete('1.0', "end")
		timeTakenInput.config(fg='black')

def on_Entry_Click_idInput(event):
	global thirdClick
	thirdClick = True
	if thirdClick:
		thirdClick = False
		idInput.delete('1.0', "end")
		idInput.config(fg='black')

def on_Entry_Click_idSecondaryInput(event):
	global fifthClick
	fifthClick = True
	if fifthClick:
		fifthClick = False
		second_idInput.delete('1.0', "end")
		second_idInput.config(fg='black')


def on_Entry_Click_secondaryTaskName(event):
	global fourthClick
	if fourthClick:
		fourthClick = False
		secondaryNameInput.delete('1.0', "end")
		secondaryNameInput.config(fg='black')

def on_Entry_Click_timeSecondTaken(event):
	global sixthClick
	sixthClick = True
	if sixthClick:
		sixthClick = False
		second_timeTakenInput.delete('1.0', "end")
		second_timeTakenInput.config(fg='black')

def insertPrimaryTask():
	taskName = taskNameInput.get("1.0", "end")
	expectedTime = timeTakenInput.get("1.0", "end")
	iidAllowed = idInput.get("1.0", "end")
	primary_tree.insert(parent='', index='end', iid=iidAllowed, text="Primary", values=(taskName, iidAllowed, expectedTime))

def insertSecondaryTask():
	global thisDict
	taskName = secondaryNameInput.get("1.0", "end")
	expectedTime = second_timeTakenInput.get("1.0", "end")
	parentID = second_idInput.get("1.0", "end")
	if parentID in thisDict: 
		thisDict[parentID] += 1
	else:
		thisDict[parentID] = 97
	iidAllowed = parentID[:-1] + chr(thisDict[parentID])
	primary_tree.insert(parent=parentID, index='end', iid=iidAllowed, text='Sub-task', values=(taskName, iidAllowed, expectedTime))

root = tk.Tk()
root.geometry("800x500")
root.title("Task Manager")

primary_tree = ttk.Treeview(root)

# Defining columns
primary_tree['columns'] = ("Task", "ID", "Expected Time")

# Format Columns
primary_tree.column("#0", width=120, minwidth=25)
primary_tree.column("Task", anchor="w", width=200, minwidth=120)
primary_tree.column("ID", anchor="center", width=80)
primary_tree.column("Expected Time", anchor="center", width=100)

# Create headings
primary_tree.heading("#0", text="Label", anchor="w")
primary_tree.heading("Task", text="Task Name", anchor="w")
primary_tree.heading("ID", text="ID", anchor='center')
primary_tree.heading("Expected Time", text="Expected Time", anchor="w")

primary_tree.pack(pady=20)

# Insert parent record in table function

taskNameInput = tk.Text(root, height=1, width=25)
taskNameInput.place(x="175", y="275")
taskNameInput.insert('1.0', 'Enter your task name here...')
taskNameInput.bind('<FocusIn>', on_Entry_Click_taskName)
taskNameInput.config(fg='grey')

idInput = tk.Text(root, height=1, width=25)
idInput.place(x="410", y="275")
idInput.insert('1.0', "Enter unused id here...")
idInput.bind('<FocusIn>', on_Entry_Click_idInput)
idInput.config(fg='grey')

timeTakenInput = tk.Text(root, height=1, width=25)
timeTakenInput.place(x="410", y="300")
timeTakenInput.insert('1.0', "Enter estimated time here...")
timeTakenInput.bind('<FocusIn>', on_Entry_Click_timeTaken)
timeTakenInput.config(fg='grey')


button_insertTask = tk.Button(root, text="Insert Primary Task", command=insertPrimaryTask)
button_insertTask.place(x="330", y="330")

# Insert child record in table function

secondaryNameInput = tk.Text(root, height=1, width=25)
secondaryNameInput.place(x="175", y="375")
secondaryNameInput.insert('1.0', 'Enter your secondary task name here...')
secondaryNameInput.bind('<FocusIn>', on_Entry_Click_secondaryTaskName)
secondaryNameInput.config(fg='grey')

second_idInput = tk.Text(root, height=1, width=25)
second_idInput.place(x="410", y="375")
second_idInput.insert('1.0', "Enter id of primary task here...")
second_idInput.bind('<FocusIn>', on_Entry_Click_idSecondaryInput)
second_idInput.config(fg='grey')

second_timeTakenInput = tk.Text(root, height=1, width=25)
second_timeTakenInput.place(x="410", y="400")
second_timeTakenInput.insert('1.0', "Enter estimated time here...")
second_timeTakenInput.bind('<FocusIn>', on_Entry_Click_timeSecondTaken)
second_timeTakenInput.config(fg='grey')

button_insertSecondaryTask = tk.Button(root, text="Insert Secondary Task", command=insertSecondaryTask)
button_insertSecondaryTask.place(x="330", y="430")


root.mainloop()
