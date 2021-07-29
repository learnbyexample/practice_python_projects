import random

class Square():
    def __init__(self):
        self.active = 'GAME ACTIVE'
        self.total_cells = 16
        self.corners = 4
        self.easy, self.hard = (0, 1)
        self.ai = {'value': 1, 'win': 'AI WINS'}
        self.user = {'value': self.corners+1, 'win': 'USER WINS'}
        self.max_ai_sum = (self.corners-1) * self.ai['value']
        self.max_user_sum = (self.corners-1) * self.user['value']
        self.all_squares = ((0, 1, 4, 5), (1, 2, 5, 6), (2, 3, 6, 7),
                            (4, 5, 8, 9), (5, 6, 9, 10), (6, 7, 10, 11),
                            (8, 9, 12, 13), (9, 10, 13, 14), (10, 11, 14, 15),
                            (0, 2, 8, 10), (1, 3, 9, 11), (4, 6, 12, 14),
                            (5, 7, 13, 15), (0, 3, 12, 15), (1, 4, 6, 9),
                            (2, 5, 7, 10), (5, 8, 10, 13), (6, 9, 11, 14),
                            (1, 7, 8, 14), (2, 4, 11, 13))

    def reset_board(self, difficulty):
        self.board = [0] * self.total_cells
        self.remaining_moves = list(range(self.total_cells))
        self.state = self.active
        self.difficulty = difficulty

    def set_user_move(self, move):
        self.update_board(self.user, move)

    def get_ai_move(self):
        if self.difficulty == self.easy:
            move = random.choice(self.remaining_moves)
        else:
            move = self.ai_hard_move()
        self.update_board(self.ai, move)
        return move

    def update_board(self, player, move):
        self.board[move] = player['value']
        self.remaining_moves.remove(move)
        self.update_status(player)

    def update_status(self, player):
        winner_sum = self.corners * player['value']
        self.winning_squares = []
        for square in self.all_squares:
            if sum(self.board[i] for i in square) == winner_sum:
                self.state = player['win']
                self.winning_squares.append(square)
        if self.state == self.active and not self.remaining_moves:
            self.state = 'TIE'

    def ai_hard_move(self):
        self.update_weights()

        # making a winning move or block a winning move
        if self.ai_winning_indexes:
            return random.choice(self.ai_winning_indexes)
        elif self.user_winning_indexes:
            return random.choice(self.user_winning_indexes)

        # if there are no possible squares left, return a random move
        max_user_weight = max(self.user_weights)
        max_ai_weight = max(self.ai_weights)
        if max_user_weight == 0 and max_ai_weight == 0:
            return random.choice(self.remaining_moves)

        # there can be multiple indexes with max weight
        def max_moves(seq, val):
            return [i for i,w in enumerate(seq) if w == val]
        max_user_moves = max_moves(self.user_weights, max_user_weight)
        max_ai_moves = max_moves(self.ai_weights, max_ai_weight)

        # randomize multiple indexes and choose best move based on weights
        if max_user_weight > max_ai_weight:
            random.shuffle(max_user_moves)
            return max(max_user_moves, key=lambda x: self.ai_weights[x])
        else:
            random.shuffle(max_ai_moves)
            return max(max_ai_moves, key=lambda x: self.user_weights[x])

    def update_weights(self):
        def update(s, w, t, ot):
            for i in square:
                if self.board[i] == 0:
                    w[i] += t * t + 1
                    if ot == self.max_ai_sum:
                        self.ai_winning_indexes.append(i)
                    elif ot == self.max_user_sum:
                        self.user_winning_indexes.append(i)

        self.user_weights = [0] * self.total_cells
        self.ai_weights = [0] * self.total_cells
        self.user_winning_indexes = []
        self.ai_winning_indexes = []
        for square in self.all_squares:
            total = sum(self.board[i] for i in square)
            if total == 0:
                update(square, self.user_weights, 0, 0)
                update(square, self.ai_weights, 0, 0)
            elif total <= self.max_ai_sum:
                update(square, self.ai_weights, total, total)
            else:
                q, r = divmod(total, self.user['value'])
                if r == 0:
                    update(square, self.user_weights, q, total)
