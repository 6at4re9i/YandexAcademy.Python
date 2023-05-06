n = int(input())
n1 = n
reverse = 0
while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10
if n1 == reverse:
    print("YES")
else:
    print("NO")