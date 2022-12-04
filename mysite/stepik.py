import random
class Cell:
    def __init__(self, around_mines=0, mine=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False

class GamePole:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.pole = []
        # инициализируем поле
        for _ in range(self.N):
            tmp = [Cell() for _ in range(self.N)]
            self.pole.append(tmp)

    def init(self):

        # расставляем мины
        mines = random.sample(range(self.N**2), self.M)
        for mine in mines:
            x, y = mine // self.N, mine % self.N
            self.pole[x][y].mine = True
            self.pole[x][y].around_mines = 0
            for i in range(max(x - 1, 0), min(x + 2, self.N)):
                for j in range(max(y - 1, 0), min(y + 2, self.N)):
                    if not self.pole[i][j].mine:
                        self.pole[i][j].around_mines += 1

    def show(self):
        for i in range(self.N):
            for j in range(self.N):
                if self.pole[i][j].fl_open or True:
                    if self.pole[i][j].mine:
                        print('*', end=' ')
                    else:
                        print(self.pole[i][j].around_mines, end=' ')
                else:
                    print('#', end=' ')
            print()


pole_game = GamePole(10, 12)
pole_game.init()
pole_game.show()


def get_around_mines(i, j):
    n = 0
    for k in range(-1, 2):
        for l in range(-1, 2):
            ii, jj = k+i, l+j
            if ii < 0 or jj < 0 or ii >= N or jj >= N:
                continue
            if pole_game.pole[ii][jj].mine:
                n += 1
    return n

N = 10
for i in range(N):
    for j in range(N):
        if not pole_game.pole[i][j].mine:
            assert pole_game.pole[i][j].around_mines == get_around_mines(i, j), f"неверное число мин вокруг клетки с индексами {i, j}"