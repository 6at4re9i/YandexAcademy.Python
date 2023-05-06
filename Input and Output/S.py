item = f'{input()}'
price = int(input())
item_mass = int(input())
money = int(input())
bill = 'Чек'
how_much = f"{item_mass}кг * {price}руб/кг"
total = f'{price * item_mass}руб'
in_money = f'{money}руб'
out_money = f'{money - price * item_mass}руб'

print(f'{bill:^35}'.replace(' ', '='))
print(f'Товар: {item.rjust(35 - 7)}')
print(f'Цена:{how_much.rjust(35 - 5)}')
print(f'Итого:{total.rjust(35 - 6)}')
print(f'Внесено: {in_money.rjust(35 - 9)}')
print(f'Сдача: {out_money.rjust(35 - 7)}')
print('=' * 35)