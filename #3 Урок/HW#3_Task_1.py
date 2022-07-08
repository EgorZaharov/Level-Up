# Задача #1
def date_input(y,z):
    x = input("Введите дату в формате xx(день).yy(мес).zzzz(год): ").split('.')
    x = list(map(int,x))
    if x[1] <= 0 or x[1] > 12:
        y = "FAILED"
        z = "Incorrect month"
    if x[1] == 2: # проверка на февраль
        if x[2] % 400 == 0: # проверка на високосный год
            if x[0] > 29 or x[0] < 0:  # условие для високсного года
                y = "FAILED"
                z = "Incorrect day"
            else:
                y = "OK"
        elif x[2] % 4 == 0 and x[2] % 100 != 0:
            if x[0] > 29 or x[0] < 0:  # условие для високсного года
                y = "FAILED"
                z = "Incorrect day"
            else:
                y = "OK"
        elif x[0] > 28 or x[0] < 0: # условие для обычного года
            y = "FAILED"
            z = "Incorrect day"
        else:
            y = "OK"
    elif x[1] > 0 and x[1] <= 7 and x[1] % 2 != 0 or x[1] > 7 and x[1] <= 12 and x[1] % 2 == 0: # проверка на месяц с 31 днем
        if x[0] > 31 or x [0] < 0:
            y = "FAILED"
            z = "Incorrect day"
        else:
            y = "OK"
    elif x[1] > 0 and x[1] <= 7 and x[1] % 2 == 0 or x[1] > 7 and x[1] <= 12 and x[1] % 2 != 0: # проверка на месяц с 30 днями
        if x[0] > 30 or x[0] < 0:
            y = "FAILED"
            z = "Incorrect day"
        else:
            y = "OK"
    return y,z


y = 0
z = 0
y,z = date_input(y,z)
print(y)
if z != 0:
    print(z)