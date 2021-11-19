def seqCheck(array, amountNum):
    arithPass = amountNum - 2

    for i in range(0, amountNum - 2):
        if (int(array[i+1]) - int(array[i]) == int(array[i + 2]) - int(array[i + 1])):
            arithPass -= 1

    return arithPass

def main():
    numSeq = int(input())
    count = 0
    failArith = False
    while (count != numSeq):
        line = input().split()
        print(line)
        amountNum = int(line[0])
        array = line[1:]
        arithPass = seqCheck(array, amountNum)

        if arithPass == 0:
            print("arithmetic")
            failArith = True
            count += 1
            continue

        array.sort()
        arithPass = seqCheck(array, amountNum)
        print(arithPass)
        if (arithPass == 0):
            print("permuted arithmetic")
            failArith = True
            count +=1
            continue

        if failArith == False :
            print("non-arithmetic")
            count += 1
            continue

main()
        
        