N = int(input())
M = int(input())
T = int(input())

hours = N + int(T / 60)
minutes = M + int(T - (hours - N) * 60)

if minutes >= 60:
    hours += 1
    minutes -= 60

if hours >= 24:
    trash = int(hours / 24)
    hours -= trash * 24

if hours < 10 and minutes < 10:
    print(f"{0}{hours}:{0}{minutes}")

elif hours > 10 and minutes > 10:
    print(f"{hours}:{minutes}")

elif hours < 10 < minutes:
    print(f"{0}{hours}:{minutes}")

elif hours > 10 > minutes:
    print(f"{hours}:{0}{minutes}")
