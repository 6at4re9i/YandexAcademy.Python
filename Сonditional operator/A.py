print("Как Вас зовут?")
answer1 = input()
print(f"Здравствуйте, {answer1}!")
print("Как дела?")
answer2 = input()
if answer2 == "хорошо":
    print("Я за вас рада!")
elif answer2 != "хорошо":
    print("Всё наладится!")