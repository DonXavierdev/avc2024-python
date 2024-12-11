# iterate through the input
# Find X and set loop ready to go in all directions
# if the next letter found in one of the directions repeat process in same direction
# If all letters found increment count


with open('input.txt','r') as f:
    puzz = f.readlines()
matrix_puzz = []
for i in puzz:
    matrix_puzz.append(list(i[:-1]))
