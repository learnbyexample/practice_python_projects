import random
import tkinter as tk

class Root(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Image Labels')
        self.geometry('200x200')

        self.frame = tk.Frame()
        self.frame.pack(expand=True)

        self.char_x = tk.PhotoImage(file='./char_x.png')
        self.char_o = tk.PhotoImage(file='./char_o.png')
        self.empty = tk.PhotoImage()

        self.label = [None] * 9
        self.last_click = 0
        for i in range(9):
            r, c = divmod(i, 3)
            self.label[i] = tk.Label(self.frame, image=self.empty,
                                     highlightthickness=1,
                                     width=50, height=50, bg='white')
            self.label[i].bind('<Button-1>',
                               lambda e, n=i: self.button_click(e, n))
            self.label[i].grid(row=r, column=c)

    def button_click(self, e, n):
        self.label[self.last_click]['bg'] = 'white'
        self.last_click = n
        choice = random.randrange(2)
        self.label[n]['image'] = (self.char_x, self.char_o)[choice]
        self.label[n]['bg'] = ('orange', 'grey')[choice]

if __name__ == '__main__':
    root = Root()
    root.mainloop()
