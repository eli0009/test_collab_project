from sqlite3 import connect
from colorama import init, Fore
from random import randint, choice

class Maze:
    """Generate a size x size maze
    """

    def __init__(self, size = 5) -> None:

        self.size = size * 2 + 1
        self.visited = []
        wall = 0
        path = 1

        self.maze = [[wall] * self.size for _ in range(self.size)] # to fill the whole maze with walls

        for i in range(2, self.size):
            for j in range(2, self.size, 2):
                if i % 2 == 0:
                    self.flip(j, i)
                else:
                    if j != 2:
                        self.flip(j-1, i)    

        self.generate()

    def generate(self):
        '''Generate a maze'''
        cell = self.first_cell()

        def remove_wall(cell1):
            cell2 = self.get_neighbour(*cell1)
            if cell2:
                self.connect_neighbour(cell1, cell2)
                self.display()
                print('=================')
                remove_wall(cell2)
            else:
                return

        remove_wall(cell)

    def first_cell(self):
        '''Get a random cell that is not a wall'''

        x = randint(2, self.size - 1)
        y = randint(2, self.size - 1)

        while self.is_wall(x, y):
            x = randint(2, self.size - 1)
            y = randint(2, self.size - 1)
        
        return (x, y)

    def get_neighbour(self, x, y):
        '''Get the NWES neighours of a cell'''
        adj = [(x - 2, y),
               (x + 2, y),
               (x, y + 2),
               (x, y - 2),
               ]
        neighbours = [
            cell for cell in adj
            if not self.is_wall(*cell) and cell not in self.visited
        ]
        if neighbours:
            cell = choice(neighbours)
            self.visited.append(cell)
            return cell
        else:
            return None

    def connect_neighbour(self, cell1, cell2):
        '''Connect 2 cells separated by a wall'''
        if cell1[0] == cell2[0]:
            if cell1[1] > cell2[1]:
                self.flip(cell1[0], cell1[1] - 1)
            else:
                self.flip(cell1[0], cell1[1] + 1)
        else:
            if cell1[0] > cell2[0]:
                self.flip(cell1[0] - 1, cell1[1])
            else:
                self.flip(cell1[0] + 1, cell1[1])

    def flip(self, x, y, type=None):
        '''Flip the value of a maze cell between 1 and 0
        0 < x, y <= size
        '''
        # we need to consider the case when x,y = 0 because then x = x  - 1 = -1
        x = x - 1 # list starts at index 0 so we subtract 1 
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

