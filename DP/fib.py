#return n-th number of Fibonacci sequence

def fib(n):
    if n <= 2: return 1
    return fib(n-2) + fib(n-1)

# print(fib(7))

def fib_dp(n, d = {}):
    if n in d: return d[n]
    if n <= 2: return 1
    d[n] = fib_dp(n-2, d) + fib_dp(n-1, d)
    return d[n]

print(fib_dp(50))