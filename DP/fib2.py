def fib(pos):
    t = [None] * (pos + 1)
    t[0], t[1] = 0, 1
    for i in range(2, pos + 1):
        t[i] = t[i-1] + t[i-2]
    return t[-1]

print(fib(6))