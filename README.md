# Conways-Game-of-Life

Conway’s Game of Life is a simple simulation that creates artificial “life” on a grid, 
each cell of which is either live or not. Each generation (turn), the following rules are applied:

Any live cell with fewer than two or more than three live neighbors dies.

Any live cell with two or three live neighbors lives on to the next generation.

Any dead cell with exactly three live neighbors becomes a live cell.

A neighbor is defined as any adjacent cell, including diagonally adjacent ones.

Note that these rules are applied to the whole grid at once, not one square at a time. 
That means the counting of neighbors is based on the situation at the start of the generation, 
and changes happening to neighbor cells during this generation should not influence the new 
state of a given cell.

A live cell is represented by an "O" character and a dead cell is represented as an empty space on the board.
