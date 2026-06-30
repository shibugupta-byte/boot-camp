import tkinter as tk


# Calculator Functions

def click(value):
    current = display_var.get()
    display_var.set(current + str(value))

def clear():
    display_var.set("")

def backspace():
    current = display_var.get()
    display_var.set(current[:-1])

def calculate():
    try:
        result = eval(display_var.get())
        display_var.set(str(result))
    except:
        display_var.set("Error")


# Main Window

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("340x470")
root.resizable(False, False)
root.configure(bg="#f2f2f2")

display_var = tk.StringVar()

display = tk.Entry(
    root,
    textvariable=display_var,
    font=("Arial", 22),
    justify="right",
    bd=8,
    relief="sunken"
)
display.pack(fill="both", padx=10, pady=10, ipady=10)


# Buttons
buttons = [
    ["C", "⌫", "/", "*"],
    ["7", "8", "9", "-"],
    ["4", "5", "6", "+"],
    ["1", "2", "3", "="],
    ["0", ".", "", ""]
]

frame = tk.Frame(root, bg="#f2f2f2")
frame.pack(expand=True, fill="both")

for r, row in enumerate(buttons):
    for c, text in enumerate(row):

        if text == "":
            continue

        if text == "=":
            cmd = calculate
        elif text == "C":
            cmd = clear
        elif text == "⌫":
            cmd = backspace
        else:
            cmd = lambda x=text: click(x)

        btn = tk.Button(
            frame,
            text=text,
            font=("Arial", 18),
            command=cmd,
            width=5,
            height=2,
            bg="white"
        )

        btn.grid(row=r, column=c, padx=5, pady=5, sticky="nsew")

for i in range(5):
    frame.grid_rowconfigure(i, weight=1)

for i in range(4):
    frame.grid_columnconfigure(i, weight=1)

root.mainloop()