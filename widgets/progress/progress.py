import tkinter as tk
from tkinter import ttk

app = tk.Tk()
app.title("Progress bars")

vertical = tk.DoubleVar(value = 15)
scl = ttk.Scale(
    app,
    command = lambda value: print(vertical.get()),
    from_ = 0,
    to = 30,
    length = 300,
    orient = 'vertical',
    variable = vertical
)
scl.pack()

progress = ttk.Progressbar(app, variable = vertical, maximum = 30)
progress.pack()

app.mainloop()