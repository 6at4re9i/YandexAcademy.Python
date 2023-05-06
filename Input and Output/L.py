x = int(input())
y = int(input())
a = int(x / 100)
b = int(int(x / 10) - a * 10)
c = int(int(x - a * 100 - b * 10))
a1 = int(y / 100)
b1 = int(int(y / 10) - a1 * 10)
c1 = int(int(y - a1 * 100 - b1 * 10))
sum1 = a + a1
sum2 = b + b1
sum3 = c + c1
if sum1 >= 10:
    sum1 -= 10
if sum2 >= 10:
    sum2 -= 10
if sum3 >= 10:
    sum3 -= 10

print(f"{sum1}{sum2}{sum3}")
