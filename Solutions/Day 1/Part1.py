arr1 = []
arr2 = []
with open('input.txt') as f:
    arr = f.readlines()
res = 0
for i in arr:
    var1 = i.split('   ')
    arr1.append(int(var1[0]))
    arr2.append(int(var1[1]))
arr1.sort()
arr2.sort()
for i in range(len(arr1)):
    res += abs(arr1[i] - arr2[i])
print(res)