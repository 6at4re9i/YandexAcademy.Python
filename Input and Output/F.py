name = input()
value = int(input())
weight = int(input())
money = int(input())
cost = value * weight
change = money - cost
print("Чек")
print(f"{name} - {weight}кг - {value}руб/кг")
print(f"Итого: {cost}руб")
print(f"Внесено: {money}руб")
print(f"Сдача: {change}руб")