number = int(input())
sot = int(number / 100)
des = int(number / 10 - sot * 10)
ed = int(number - sot * 100 - des * 10)
sum1 = ed + des
sum2 = sot + des
if sum1 > sum2:
    print(f"{sum1}{sum2}")
else:
    print(f"{sum2}{sum1}")