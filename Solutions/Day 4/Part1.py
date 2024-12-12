# iterate through the input
# Find X and set loop ready to go in all directions
# if the next letter found in one of the directions repeat process in same direction
# If all letters found increment count

directions = [[-1,0],[1,0],[0,1],[0,-1]]

def dfs(r,c,):
    for x,y in directions:
        new_r = r + x
        new_c = c + y
        if 0 <= new_c < len(matrix_puzz[0]) and 0 <= new_r < len(matrix_puzz):
            print(matrix_puzz[new_r][new_c])
with open('input.txt','r') as f:
    puzz = f.readlines()
matrix_puzz = []
for i in puzz:
    matrix_puzz.append(list(i[:-1]))
for r in range(len(matrix_puzz)):
    for c in range(len(matrix_puzz[0])):
        if matrix_puzz[r][c] == 'X':
            print(r,c)
            dfs(r,c)