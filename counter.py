import tkinter as tk

#function definitions
def increment():
    global count
    count += 1
    label.config(text=str(count))


def decrement():
    global count
    count -= 1
    label.config(text=str(count))


def reset():
    global count
    count = 0
    label.config(text=str(count))

#App window
app = tk.Tk()
app.title=("Counter App")
app.geometry("250x150")

count = 0

label = tk.Label(app, text="0", font=("Arial", 32))
label.pack(pady=10)

frame = tk.Frame(app)
frame.pack()

tk.Button(frame, text="Increment", command=increment).grid(row=0, column=0)
tk.Button(frame, text="Decrement", command=decrement).grid(row=0, column=1)
tk.Button(app, text="Reset", command=reset).pack(pady=5)

app.mainloop()