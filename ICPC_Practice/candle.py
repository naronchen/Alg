D = int(input())
R = int(input())
T = int(input())

R_box=0
T_box=0
i = 4

while True:
    R_box += i
    if (i - D >= 3):
        T_box += i - D
    
    if (R_box  +  T_box == R + T):
        print(R - R_box)
        break
    
    i=i+1



