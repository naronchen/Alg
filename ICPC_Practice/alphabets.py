import string

T = int(input())
alphabet = {
        'A' : '1', 
        'B' : '2', 
        'C' : '3', 
        'D' : '4', 
        'E' : '5', 
        'F' : '6', 
        'G' : '7', 
        'H' : '8', 
        'I' : '9', 
        'J' : '10', 
        'K' : '11', 
        'L' : '12', 
        'M' : '13', 
        'N' : '14', 
        'O' : '15', 
        'P' : '16', 
        'Q' : '17', 
        'R' : '18', 
        'S' : '19', 
        'T' : '20', 
        'U' : '21', 
        'V' : '22', 
        'W' : '23', 
        'X' : '24', 
        'Y' : '25', 
        'Z' : '26'
    }

for i in range(T):
    N = int(input())
    S = str(input())
    L = ""
    count = 0
    prev = S[0]
    for s in S:
        if int(alphabet[s]) > int(alphabet[prev]):
            count = count + 1
        else:
            count = 1
        prev = s
        L = L + " "+ str(count)
    t = i+1
    print ("Case #"+str(t)+":"+L)


    

