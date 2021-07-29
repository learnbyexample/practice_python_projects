import tkinter as tk

def button_click():
    label['text'] = 'Button clicked!'
    label['fg'] = 'blue'

def quit_program():
    root.destroy()

root = tk.Tk()
root.title('Buttons and Labels')
root.geometry('400x300')

label = tk.Label(text='Click the button', pady=10)
label.pack()

button = tk.Button(text='Click this', command=button_click)
button.pack(side=tk.LEFT)

quit = tk.Button(text='Quit', command=quit_program)
quit.pack(side=tk.RIGHT)

root.mainloop()
