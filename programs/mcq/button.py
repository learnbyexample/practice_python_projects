import tkinter as tk

def button_click():
    print('Button clicked!')

root = tk.Tk()
root.title('Button Click')
root.geometry('400x300')

button = tk.Button(text='Click this', command=button_click)
button.pack()

root.mainloop()
