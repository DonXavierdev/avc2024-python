with open('input.txt') as f:
    arr = f.readlines()
count = 0
arr1 = []
for i in arr:
    arr1.append(i.split(' '))
for i in arr1:
    inc = 0
    dec = 0
    flag = 0
    prev = int(i[0])
    if prev - int(i[1]) < 0:
        inc = 1
    else:
        dec = 1
    for j in i[1:]:
        num = int(j)
        diff = prev - num
        if inc == 1:
            if abs(diff) > 3 or abs(diff) == 0 or diff > 0:
                flag = 1
                break
        elif dec == 1:
            if abs(diff) > 3 or abs(diff) == 0 or diff < 0:
                flag = 1
                break
        else:
            flag = 1
            break
        prev = num
    if flag == 0:
        count += 1
            
print(count)


