from pprint import pprint
from colorama import init, Fore

class Maze:
    """Generate a size x size maze
    """

    def __init__(self, size = 5) -> None:

        self.size = size * 2 + 1
        wall = 0
        path = 1

        self.maze = [[wall] * self.size for _ in range(self.size)]

        for i in range(2, self.size):
            for j in range(2, self.size, 2):
                if i % 2 == 0:
                    self.flip(j, i)
                else:
                    if j != 2:
                        self.flip(j-1, i)    
                

    def flip(self, x, y):
        '''Flip the value of a maze cell between 1 and 0
        0 < x, y <= size
        '''
        x = x - 1
        y = y - 1
        self.maze[x][y] = int(not self.maze[x][y])

    def is_wall(self, x, y):
        '''Check if a cell if a wall'''
        x = x - 1
        y = y - 1
        return not self.maze[x][y]

    def display(self):
        '''Print the maze in color'''
        init()
        for i in range(self.size):
            for j in range(self.size):
                if self.maze[j][i]:
                    print(Fore.WHITE, f'{self.maze[j][i]}', end="")
                elif not self.maze[j][i]:
                    print(Fore.RED, f'{self.maze[j][i]}', end="")
                else:
                    print(Fore.BLUE, f'{self.maze[j][i]}', end="")
            print('\n')

if __name__ == "__main__":

    m = Maze()
    m.display()

