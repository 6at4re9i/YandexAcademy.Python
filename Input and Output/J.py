name = input()
number = int(input())
group = int(number / 100)
bed = int(int(number / 10) - group * 10)
issue = int(number - group * 100 - bed * 10)
print(f"Группа №{group}.")
print(f"{issue}. {name}.")
print(f"Шкафчик: {number}.")
print(f"Кроватка: {bed}.")