number = int(input())

sot = int(number / 100)
des = int(number / 10 - sot * 10)
ed = int(number - sot * 100 - des * 10)

middle = 0
maxi = max(sot, des, ed)
mini = min(sot, des, ed)

if sot != maxi and sot != mini:
    middle = sot
elif ed != maxi and ed != mini:
    middle = ed
elif des != maxi and des != mini:
    middle = des

if maxi + mini == middle * 2:
    print("YES")
else:
    print("NO")
