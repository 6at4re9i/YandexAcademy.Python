a, b, c = int(input()), int(input()), int(input())
if a > b > c:
    print(f"1. Петя")
    print(f"2. Вася")
    print(f"3. Толя")
elif a > c > b:
    print(f"1. Петя")
    print(f"2. Толя")
    print(f"3. Вася")
elif b > a > c:
    print(f"1. Вася")
    print(f"2. Петя")
    print(f"3. Толя")
elif b > c > a:
    print(f"1. Вася")
    print(f"2. Толя")
    print(f"3. Петя")
elif c > a > b:
    print(f"1. Толя")
    print(f"2. Петя")
    print(f"3. Вася")
else:
    print(f"1. Толя")
    print(f"2. Вася")
    print(f"3. Петя")