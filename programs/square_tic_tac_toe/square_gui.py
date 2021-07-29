from square_ai import Square
import tkinter as tk

class Root(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Square Tic Tac Toe')
        self.geometry('500x450')

        self.char_x = tk.PhotoImage(file='./char_x.png')
        self.char_o = tk.PhotoImage(file='./char_o.png')
        self.empty = tk.PhotoImage()

        self.ai = {'bg': 'orange', 'image': self.char_x}
        self.user = {'bg': 'grey', 'image': self.char_o}
        self.board_bg = 'white'

        self.sq = Square()
        self.create_first_move_frame()
        self.create_difficulty_frame()
        self.create_control_frame()

    def create_first_move_frame(self):
        self.radio_frame = tk.Frame()
        self.radio_frame.pack(side=tk.TOP, pady=5)

        tk.Label(self.radio_frame, text='First Move').pack(side=tk.LEFT)
        self.move_choice = tk.IntVar()
        self.move_choice.set(self.sq.user['value'])
        tk.Radiobutton(self.radio_frame, text='Computer',
                       variable=self.move_choice, value=self.sq.ai['value']
                      ).pack(side=tk.LEFT)
        tk.Radiobutton(self.radio_frame, text='User',
                       variable=self.move_choice, value=self.sq.user['value']
                      ).pack(side=tk.RIGHT)

    def create_difficulty_frame(self):
        self.difficulty_frame = tk.Frame()
        self.difficulty_frame.pack(side=tk.TOP, pady=5)

        tk.Label(self.difficulty_frame, text='Difficulty').pack(side=tk.LEFT)
        self.difficulty_choice = tk.IntVar()
        self.difficulty_choice.set(self.sq.easy)
        tk.Radiobutton(self.difficulty_frame, text='Easy',
                       variable=self.difficulty_choice, value=self.sq.easy
                      ).pack(side=tk.LEFT)
        tk.Radiobutton(self.difficulty_frame, text='Hard',
                       variable=self.difficulty_choice, value=self.sq.hard
                      ).pack(side=tk.RIGHT)

    def create_control_frame(self):
        self.control_frame = tk.Frame()
        self.control_frame.pack(side=tk.TOP, pady=5)

        self.b_quit = tk.Button(self.control_frame, text='Quit',
                                command=self.quit)
        self.b_quit.pack(side=tk.LEFT)

        self.b_play = tk.Button(self.control_frame, text='Play',
                                command=self.play)
        self.b_play.pack(side=tk.RIGHT)

    def create_status_frame(self):
        self.status_frame = tk.Frame()
        self.status_frame.pack(expand=True)

        tk.Label(self.status_frame, text='Status: ').pack(side=tk.LEFT)
        self.l_status = tk.Label(self.status_frame)
        self.l_status.pack(side=tk.RIGHT)

    def create_board_frame(self):
        self.board_frame = tk.Frame()
        self.board_frame.pack(expand=True)

        self.sq.reset_board(self.difficulty_choice.get())
        self.cell = [None] * self.sq.total_cells
        for i in range(self.sq.total_cells):
            self.cell[i] = tk.Label(self.board_frame, highlightthickness=1,
                                    width=60, height=60, bg=self.board_bg,
                                    image=self.empty)
            self.cell[i].bind('<Button-1>',
                              lambda e, move=i: self.user_click(e, move))
            r, c = divmod(i, self.sq.corners)
            self.cell[i].grid(row=r, column=c)

    def play(self):
        self.b_play['state'] = 'disabled'
        if self.b_play['text'] == 'Play':
            self.create_status_frame()
            self.b_play['text'] = 'Play Again'
        else:
            self.board_frame.destroy()
        self.create_board_frame()
        self.l_status['text'] = self.sq.active
        self.last_click = 0
        if self.move_choice.get() == self.sq.ai['value']:
            self.ai_click()

    def quit(self):
        self.destroy()

    def user_click(self, e, user_move):
        if self.sq.board[user_move] != 0 or self.sq.state != self.sq.active:
            return
        self.sq.set_user_move(user_move)
        self.update_cell(self.user, user_move)
        if self.sq.state == self.sq.active:
            self.ai_click()

    def ai_click(self):
        ai_move = self.sq.get_ai_move()
        self.update_cell(self.ai, ai_move)

    def update_cell(self, player, move):
        self.cell[self.last_click]['bg'] = self.board_bg
        self.last_click = move
        self.cell[move]['image'] = player['image']
        self.cell[move]['bg'] = player['bg']
        self.l_status['text'] = self.sq.state
        if self.sq.state != self.sq.active:
            self.b_play['state'] = 'normal'
            if self.sq.state != 'TIE':
                self.highlight_winning_squares(player)

    def highlight_winning_squares(self, player):
        for square in self.sq.winning_squares:
            for i in square:
                self.cell[i]['bg'] = player['bg']

if __name__ == '__main__':
    root = Root()
    root.mainloop()
