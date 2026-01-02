import tkinter as tk    #Imports tkinter module tk is an alias for easy access

def press(v):
    entry.insert(tk.END, v)     #Called when a no. or operator button is clicked, inserts the pressed value at the end of Entry widget

def clear():
    entry.delete(0, tk.END)     #Clears the character screen, deletes all characters from index 0 to END

def calc():
    try:
        result = eval(entry.get())      #entry.get() gets the expression, eval() evaluates the string as an expression

        entry.delete(0, tk.END)
        entry.insert(0, result)

    except:
        entry.delete(0, tk.END)
        entry.insert(0, "INVALID EXPRESSION")       #Handles invalid expressions display the error message instead of crashing

#Main window creation
root = tk.Tk()      #Creates the main application window
root.title("Calculator")    #Sets window title
root.configure(bg="#1e1e1e")    #Sets background color
root.resizable(False, False)    #makes window non-resizable

#Entry widget (display screen)
entry = tk.Entry(
    root,
    font=("Gothic", 20),
    bg="#2d2d2d",
    fg="white",
    bd=0,
    justify="right"
)

"""Text input field
Acts as calculator display
Right-aligned for better calculator look"""

entry.grid(row=0, column=0, columnspan=4, padx=12, pady=12, ipady=10)
"""Places entry at top columnspan=4 makes it stretch across columns"""

#Buttons labels
buttons = [
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "0",".","=","+"
]
"""Represent calculator button
stored in list to reduce repetitive code"""

#Dynamic Button Creation
r=1
c=0
"""Rows and column counters for grid layout"""

for b in buttons:
    cmd = calc if b=="=" else lambda x=b: press(x)
    """if button is "=" call calc()
    otherwise, call press() with the button value
    lambda x=b prevents late binding issue"""

    tk.Button(
        root,
        text=b,
        command=cmd,   #These 3 lines creates a button widget
        font=("Times New Roman", 15),
        width=5,
        height=3,
        bg="#3333F6" if b in "+-/*" else "#9932ee",
        fg="white",
        bd=0
    ).grid(row=r, column=c, padx=6, pady=6)
    c+=1
    if c == 4:
        r+=1
        c=0
        """moves to next row after 4 buttons"""

#Clear Button
tk.Button(
    root,
    text="C",
    command=clear,
    font=("Arial", 15),
    fg="black",
    bg="#F93333",
    bd=0,
    width=22,
    height=2
).grid(row=r, column=0, columnspan=4, pady=8)

root.mainloop()     #Keeps the window running 




