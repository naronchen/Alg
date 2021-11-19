n = int(input())
for i in range(n):
    a = input()
    longestbin = 0
    b = ""
    for k in a:
        b += k
        c = str(bin(int(b)))
        #print(c)
        d = c.count('1')
        if d > longestbin:
            longestbin = d
    print(longestbin)

