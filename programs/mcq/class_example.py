import tkinter as tk

class Root(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Buttons and Labels')
        self.geometry('400x300')

        self.label = tk.Label(text='Click the button', pady=10)
        self.label.pack()

        self.button = tk.Button(text='Click this', command=self.button_click)
        self.button.pack(side=tk.LEFT)

        self.quit = tk.Button(text='Quit', command=self.quit_program)
        self.quit.pack(side=tk.RIGHT)

    def button_click(self):
        self.label['text'] = 'Button clicked!'
        self.label['fg'] = 'blue'

    def quit_program(self):
        self.destroy()

root = Root()
root.mainloop()
