import tkinter as tk
from tkinter import messagebox

# Global expression string
expression = ""

# Button click handler
def press(key):
    global expression
    expression += str(key)
    input_text.set(expression)

# Clear the entry
def clear():
    global expression
    expression = ""
    input_text.set("")

# Backspace function
def backspace():
    global expression
    expression = expression[:-1]
    input_text.set(expression)

# Evaluate the expression
def equalpress():
    global expression
    try:
        result = str(eval(expression.replace('×', '*').replace('÷', '/')))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

# Main window
window = tk.Tk()
window.title("Advanced Calculator")
window.geometry("420x550")
window.resizable(False, False)
window.configure(bg="#1c1c1c")

# Entry field
input_text = tk.StringVar()
input_field = tk.Entry(window, textvariable=input_text, font=('Segoe UI', 24), bd=10, insertwidth=2,
                       bg="#2b2b2b", fg="white", justify='right', relief='flat')
input_field.pack(expand=True, fill='both', ipadx=8, ipady=20)

# Button configuration
btns = [
    ['C', '⌫', '%', '÷'],
    ['7', '8', '9', '×'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['0', '.', '=', '']
]

# Button click mapper
def create_button(text, row, col):
    if text == '':
        return
    action = {
        'C': clear,
        '⌫': backspace,
        '=': equalpress
    }.get(text, lambda: press(text))
    
    tk.Button(
        btn_frame, text=text, width=5, height=2,
        font=('Segoe UI', 20), bd=0,
        bg="#333", fg="white", activebackground="#555",
        command=action
    ).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# Frame for buttons
btn_frame = tk.Frame(window, bg="#1c1c1c")
btn_frame.pack(expand=True, fill='both')

# Grid configuration
for i in range(5):
    btn_frame.rowconfigure(i, weight=1)
    for j in range(4):
        btn_frame.columnconfigure(j, weight=1)
        create_button(btns[i][j], i, j)

# Run the app
window.mainloop()
