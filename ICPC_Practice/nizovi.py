a = input()

r = ""

if a[0] == '}' and a[1] == '}': 
    print ("{\n}")
else:
    for i in range(1,len(a) - 1):
        if a[i] == ',': r = r + ",\n  "
        if a[i] == '{': r = r + "\n{  "


        
print("{\n  " + r + "\n}") 