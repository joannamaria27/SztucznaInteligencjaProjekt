import generator
import Algorithms
from pprint import pprint

boards = []
boards.append(generator.board1)

new_maze = generator.maze_generator(18)
boards.append(new_maze)
#new_maze.d_dfs(new_maze.s.x, new_maze.s.y)
#a = new_maze.get_dfsLen()

# for x in range(100):
#         new_maze = generator.maze_generator(18)
#         new_maze.d_dfs(new_maze.s.x, new_maze.s.y)
#         a = new_maze.get_dfsLen()
#         if a == -1:
#                 print("caught")
#                 break

# generator.draw_maze(new_maze.GRID, new_maze.Path, new_maze.been)

# new_maze = generator.maze_generator()
# boards.append(new_maze)
# new_maze.dfs(new_maze.s.x, new_maze.s.y)
# Maze.draw_maze(new_maze.grid, new_maze.Path)

a = generator.prim_generator(18, 18)
a.d_dfs(a.s.x, a.s.y)
generator.draw_maze(a.GRID, a.Path, a.been)
