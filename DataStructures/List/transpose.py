# -*- coding: utf-8 -*-
'''List Transpose'''

grid = [['.', '.', '.', '.', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['O', 'O', 'O', 'O', 'O', '.'],
['.', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['.', '.', '.', '.', '.', '.']]

#   转置三种方法
grid_T =map(list,zip(*grid))
#grid_T = list(list(i) for i in zip(*grid))
#grid_T = [[row[i] for row in grid] for i in range(len(grid[0]))]


for line in grid_T:
    dots = ''
    for dot in line:
        dots += dot
    print(dots,end='\n')