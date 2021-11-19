a = int(input())

month_diff = (a - 2018) * 12 - 3
l_window = round(month_diff/26)
months_expect_add = l_window*26 - month_diff
if months_expect_add < 12: print("yes")
else: print("no")
