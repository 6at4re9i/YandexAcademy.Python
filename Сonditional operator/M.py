a, b, c = int(input()), int(input()), int(input())
digits1, digits2, digits3 = [], [], []
digits1.append(int(a / 10))
digits1.append(a % 10)
digits2.append(int(b / 10))
digits2.append(b % 10)
digits3.append(int(c / 10))
digits3.append(c % 10)

if digits1[0] == digits2[0] == digits3[0]:
    print(digits1[0])
elif digits1[1] == digits2[1] == digits3[1]:
    print(digits1[1])
else:
    print('ERROR')

