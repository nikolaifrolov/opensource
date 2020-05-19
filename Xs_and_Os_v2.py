LIST = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]


class Games:

    def __init__(self):
        self.player = 0
        self.Player1 = 'Player 1'
        self.Player2 = 'Player 2'
        self.act1 = []

    def play(self):
        while True:
            act = input(f'{self.Player1 if self.player == 0 else self.Player2}: ')
            act1 = ' '.join(act).split()
            self.act1 = act1
            checking = self.check_round()
            if checking != None:
                continue
            LIST[int(act1[1]) - 1].insert(int(act1[0]) - 1, ('X' if self.player == 0 else 'O'))
            LIST[int(act1[1]) - 1].pop(int(act1[0]))
            print(' | '.join(LIST[0]))
            print(' | '.join(LIST[1]))
            print(' | '.join(LIST[2]))
            _checking = self.check()
            if _checking != None:
                break
            self.player = 0 if self.player == 1 else 1

    def check_round(self):
        if 1 > int(self.act1[0]) or int(self.act1[0]) > 3:
            print('Неверный ход')
            return 'x'
        if 1 > int(self.act1[1]) or int(self.act1[1]) > 3:
            print('Неверный ход')
            return 'x'
        if LIST[int(self.act1[1]) - 1][int(self.act1[0]) - 1] != '-':
            print('Неверный ход')
            return 'x'

    def check(self):
        if LIST[0][0] == LIST[1][0] == LIST[2][0] != '-':
            print(f'Победил {self.Player1 if self.player == 0 else self.Player2}')
            return 'x'
        elif LIST[0][1] == LIST[1][1] == LIST[2][1] != '-':
            print(f'Победил {self.Player1 if self.player == 0 else self.Player2}')
            return 'x'
        elif LIST[0][2] == LIST[1][2] == LIST[2][2] != '-':
            print(f'Победил {self.Player1 if self.player == 0 else self.Player2}')
            return 'x'
        elif LIST[0][0] == LIST[0][1] == LIST[0][2] != '-':
            print(f'Победил {self.Player1 if self.player == 0 else self.Player2}')
            return 'x'
        elif LIST[1][0] == LIST[1][1] == LIST[1][2] != '-':
            print(f'Победил {self.Player1 if self.player == 0 else self.Player2}')
            return 'x'
        elif LIST[2][0] == LIST[2][1] == LIST[2][2] != '-':
            print(f'Победил {self.Player1 if self.player == 0 else self.Player2}')
            return 'x'
        elif LIST[0][0] == LIST[1][1] == LIST[2][2] != '-':
            print(f'Победил {self.Player1 if self.player == 0 else self.Player2}')
            return 'x'
        elif LIST[0][2] == LIST[1][1] == LIST[2][0] != '-':
            print(f'Победил {self.Player1 if self.player == 0 else self.Player2}')
            return 'x'


game = Games()
print(
    'The game started! You must enter 2 numbers from 1 to 3 corresponding to the coordinates of the cell.' 
    'The first coordinate from left to right, the second from top to bottom!')
game.play()
