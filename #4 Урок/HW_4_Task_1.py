import function_for_task_1

x1 =0
x2 =0
discriminant = 0
x1,x2, discriminant = function_for_task_1.search_values(x1, x2, discriminant)
if discriminant > 0:
    print(f"{x1 = }, {x2 = }")
elif discriminant == 0:
    print(f"{x1 = }")
else:
    print("Действительных корней нет")

