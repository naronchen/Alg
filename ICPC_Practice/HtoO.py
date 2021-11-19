import collections
import re

def add_ones(formula):
    listA = []
    for i,c in enumerate(formula, start=0):
        listA.append(c)
        if not c.isdigit() and (i == len(formula) - 1 or not formula[i+1].isnumeric()):
            listA.append('1')
    return ''.join(listA)

def source(formula):
    c = collections.Counter()
    for a, b in re.findall(r"([A-Z]+)([0-9]+)", add_ones(formula)):
        c[a] += int(b)
    return c

def create_from(f1,f2,n):
    total = float('inf')
    for k,v in f2.items():
        total = min(total, (f1[k]*n) // v)
    return total

def main():
    (f1, n), f2 = input().split(), input()
    print(create_from(source(f1), source(f2), int(n)))

if __name__ == "__main__":
    main()