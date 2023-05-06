n, m = int(input()), int(input())
k1, k2 = int(input()), int(input())

x = int(n * (k2 - m) / (k2 - k1))
y = (n - x)

print(x, y)