a, b, c = int(input()), int(input()), int(input())
if a < b + c and b < a + c and c < b + a:
    print('YES')
else:
    print("NO")
