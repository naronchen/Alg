
line = input().strip()
count = [0]*10

for n in line:
   n = int(n)
   if n == 0:
      n = 10
   count[n-1]+=1
   
if 0 in count:
   print(count.index(0)+1)
# first occurance of the missing number


else: 
   ans = min(count)
   ans = count.index(ans)
   if ans == 9:
      print("1" + "0" * (count[ans] + 1)) # if zero has the smallest count
   else: 
      print(str(ans+1)*(count[ans]+1)) 

