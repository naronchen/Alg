flipNums = set([1, 2, 5, 6, 8, 9, 0])
d = {1:1, 2:2, 5:5, 6:9, 8:8, 9:6, 0:0}
line = input().split()
n, total = int(line[0]), int(line[1])
cards = list(map(int, input().split()))

def flip(num):
    string = str(num)[::-1]
    res = ''
    for i in string:
        if int(i) in flipNums:
            res += str(d[int(i)])
        else:
            return False
    return int(res)

def possible(num):
    string = str(num)[::-1]
    for i in string:
        if int(i) not in flipNums:
            return False
    return True

b = False

for i in range(n-1):
    for j in range(i+1, n):
        if cards[i] + cards[j] == total:
            print("YES")
            b = True
            break
        if possible(cards[i]):
            if flip(cards[i]) + cards[j] == total:
                print("YES")
                b = True
                break
        if possible(cards[j]):
            if flip(cards[j]) + cards[i] == total:
                print("YES")
                b = True
                break
        if possible(cards[j]) and possible(cards[i]):
            if flip(cards[j]) + flip(cards[i]) == total:
                print("YES")
                b = True
                break
if not b:
    print("NO")