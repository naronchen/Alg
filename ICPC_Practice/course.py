
number = int(input())
count = 0
name_couse_list = []
Dict = {}
while (count != number):
    line = input()
    if line not in name_couse_list:
        name_couse_list.append(line)
        courseName = (line.split())[2]
        if courseName in Dict.keys():
            Dict[courseName] += 1
        else:
            Dict[courseName] = 1
    count += 1

key_list = list(Dict.keys()) #course list
val_list = list(Dict.values()) #course Number
key_list.sort()
val_list.sort()
val_prev = val_list[0]

arr_whole=[]
arr_part =[]

for val in val_list:
    if val_prev == val:
        index = key_list.index(val)
        arr_part.append(key_list.pop(index))
    else:
        arr_whole.append(arr_part.sort())
        arr_part = []

for i in arr_whole:
    for j in arr_part:
        print(j)

    

    
