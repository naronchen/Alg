line1 = input()
while line1 != "0":
    line2 = input()
    arr = list(map(int, line1.split()))
    arrlen = arr[0]
    permutation = arr[1:]
    # print(line2)
    line2len = len(line2)
    newarr_final = ""
    for i in range(0,line2len,arrlen):
        str = line2[i:i+arrlen]
        count = 0
        newstr=""
        space_count = 0
        if len(str) < arrlen: str = str + (arrlen -len(str))*" "
        # print(str)
        while True:
            newstr = newstr + str[permutation[count]-1]
            count = count + 1
            if (count == arrlen): break
        # print(newstr)
        newarr_final = newarr_final + newstr

    print ("'" + newarr_final + "'")
    line1 = input()
    





