a = float(input())
b = float(input())
speed = float(input())
length = b - a
time = length / speed
result = "%.2f" % round(time, 2)
print(result)