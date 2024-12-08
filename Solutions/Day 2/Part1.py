def safe(array):
    array = list(map(int, array))
    safe_sort = (array == sorted(array)) or (array == sorted(array, reverse=True))
    safe_diff = True
    for i in range(len(array) - 1):
        diff = abs(array[i] - array[i + 1])
        if not 1 <= diff <= 3:
            safe_diff = False
    
    return safe_sort and safe_diff

with open('input.txt') as f:
    arr = f.readlines()

count = 0
for line in arr:
    levels = line.split()
    if safe(levels):
        count += 1

print(count)
