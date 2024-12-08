def safe(array):
    array = list(map(int, array))
    safe_sort = (array == sorted(array)) or (array == sorted(array, reverse=True))
    for i in range(len(array) - 1):
        diff = abs(array[i] - array[i + 1])
        if not 1 <= diff <= 3:
            return False
    
    return safe_sort

def can_be_made_safe(array):
    for i in range(len(array)):
        new_array = array[:i] + array[i + 1:] 
        if safe(new_array):
            return True
    return False

with open('input.txt') as f:
    arr = f.readlines()

count = 0

for line in arr:
    levels = line.split()
    if safe(levels): 
        count += 1
    elif can_be_made_safe(levels):
        count += 1

print(count)
