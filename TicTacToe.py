from easyAI import TwoPlayerGame, AI_Player, Negamax

N = 4


class TicTacToe(TwoPlayerGame):
    def __init__(self, players):
        self.players = players
        self.current_player = 2
        self.board = {(0, 0): 1}
        self.moves = {(i - 1, j - 1) for i in range(3) for j in range(3)} - {(0, 0)}
        self.last_move = None
        self.new_moves = []

    def possible_moves(self):
        return list(self.moves)

    def make_move(self, move):
        self.board[move] = self.current_player
        self.moves.remove(move)
        self.last_move = move

        x, y = move
        new_moves = {(x + x_dif - 1, y + y_dif - 1) for x_dif in range(3) for y_dif in range(3)}
        new_moves = (new_moves - self.board.keys()) - self.moves
        self.new_moves.append(new_moves)
        self.moves.update(new_moves)

    def unmake_move(self, move):
        del self.board[move]
        self.last_move = None
        self.moves -= self.new_moves.pop()
        self.moves.add(move)

    def lose(self):
        if not self.last_move:
            return False
        x, y = self.last_move
        for i in range(N):
            if (
                    all(self.board.get((x - j + i, y)) == self.opponent_index for j in range(N)) or
                    all(self.board.get((x, y - j + i)) == self.opponent_index for j in range(N)) or
                    all(self.board.get((x - j + i, y - j + i)) == self.opponent_index for j in range(N)) or
                    all(self.board.get((x - j + i, y + j - i)) == self.opponent_index for j in range(N))
            ):
                return True
        return False

    def is_over(self):
        return (not self.moves) or self.lose()

    def scoring(self):
        return -100 if self.lose() else 0

    def show(self):
        min_i = min(self.board.keys(), key=lambda key: key[0])[0]
        max_i = max(self.board.keys(), key=lambda key: key[0])[0]
        min_j = min(self.board.keys(), key=lambda key: key[1])[1]
        max_j = max(self.board.keys(), key=lambda key: key[1])[1]
        for i in range(min_i, max_i + 1):
            for j in range(min_j, max_j + 1):
                print(['.', 'O', 'X'][self.board.get((i, j), 0)], end=' ')
            print()

    def ttentry(self):
        return tuple(sorted(self.board.items()))

    def ttrestore(self, entry):
        self.board = dict(entry)


game = TicTacToe([AI_Player(Negamax(4)), AI_Player(Negamax(4))])
history = game.play()
