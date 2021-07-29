import tkinter as tk

class Root(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Radio Buttons')
        self.geometry('400x300')

        self.frame = tk.Frame()
        self.frame.pack(expand=True)

        self.label = tk.Label(self.frame, pady=10)
        self.label.pack()

        rb = tk.IntVar()
        choices = (('False', 1), ('True', 2))
        for choice, idx in choices:
            tk.Radiobutton(self.frame, text=choice, value=idx, variable=rb,
                           command=lambda: self.label.config(text=rb.get()),
                          ).pack(anchor=tk.W)

if __name__ == '__main__':
    root = Root()
    root.mainloop()
