n = int(input())
arr = []
max = 0
max2 = 0
count = -1
for i in range(n):
    num = int(input())
    count += 1
    if max < num :
        max = num
    else:
        if num > max2:
            max2 = num
        if num < max2:
            count += 1


print(count)

