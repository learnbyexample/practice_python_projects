import tkinter as tk
import random

class Root(tk.Tk):
    def __init__(self, question_blocks):
        super().__init__()

        self.question_blocks = question_blocks
        self.q_total = len(self.question_blocks)
        self.q_count = 1
        self.a_count = 0
        self.title('Multiple Choice Questions')
        self.geometry('400x300')
        self.create_frame()

    def create_frame(self):
        self.frame = tk.Frame()
        self.frame.pack(expand=True)

        self.l_ask = tk.Label(self.frame, wraplength=300, justify='left',
                              fg='brown', pady=10, font='TkFixedFont')
        self.l_ask.pack()

        self.create_radio()

        self.l_info = tk.Label(self.frame, pady=10)
        self.l_info.pack()

        self.b_submit = tk.Button(self.frame, text='Submit',
                                  state='disabled', command=self.submit)
        self.b_submit.pack(side=tk.LEFT)
        self.submit_clicked = False

        self.b_next = tk.Button(self.frame, text='Next',
                                state='disabled', command=self.next)
        self.b_next.pack(side=tk.RIGHT)

    def create_radio(self):
        self.radio_choice = tk.IntVar()
        self.radio_choice.set(0)
        question, *choices = self.question_blocks[self.q_count-1].split('\n')
        random.shuffle(choices)
        self.l_ask['text'] = f'{self.q_count}) {question[question.find(" ")+1:]}'
        for idx, self.choice in enumerate(choices, 1):
            if self.choice.startswith('--> '):
                self.choice = self.choice[4:]
                self.answer = idx
            self.choice = self.choice[self.choice.find(" ")+1:]
            tk.Radiobutton(self.frame, text=self.choice, font='TkFixedFont',
                           padx=20, variable=self.radio_choice, value=idx,
                           command=self.radio).pack(anchor=tk.W)

    def radio(self):
        if not self.submit_clicked:
            self.b_submit['state'] = 'normal'

    def submit(self):
        self.submit_clicked = True
        usr_ip = self.radio_choice.get()
        if usr_ip == self.answer:
            self.a_count += 1
            self.l_info['fg'] = 'green'
            self.l_info['text'] = 'Correct answer! \U0001F44D'
        else:
            self.l_info['fg'] = 'red'
            self.l_info['text'] = ('\u274E Oops! '
                                   f'The right choice is: {self.answer}')
        self.b_submit['state'] = 'disabled'
        self.b_next['state'] = 'normal'

    def next(self):
        self.frame.destroy()
        self.q_count += 1
        if self.q_count <= self.q_total:
            self.create_frame()
        else:
            self.frame = tk.Frame()
            self.frame.pack(expand=True)
            report = f'You answered {self.a_count}/{self.q_total} correctly'
            self.l_report = tk.Label(self.frame, fg='blue', text=report)
            self.l_report.pack()

if __name__ == '__main__':
    ip_file = 'question_and_answers.txt'
    question_blocks = open(ip_file).read().rstrip().split('\n\n')
    random.shuffle(question_blocks)

    root = Root(question_blocks)
    root.mainloop()

