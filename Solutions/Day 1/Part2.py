arr1 = []
arr2 = []
with open('input.txt') as f:
    arr = f.readlines()
res = 0
for i in arr:
    var1 = i.split('   ')
    arr1.append(int(var1[0]))
    arr2.append(int(var1[1]))
for i in arr1:
    count = 0
    for j in arr2:
        if i == j:
            count += 1
    res+= i * count
print(res)