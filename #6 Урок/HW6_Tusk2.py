with open("data/questions", mode="w", encoding="utf8") as questions:
    lines = ["Вопрос 1: Третья планета от Солнца?\n", "Варианты ответа: 1. Венера 2. Меркурий 3. Земля 4. Марс\n", "Вопрос 2: Самая яркая звезда?\n", "Варианты ответа: 1. Бетельгейзе 2. Сириус 3. Солнце 4. UY Щита\n", "Вопрос 3: Планета с кольцами?\n", "Варианты ответа: 1. Сатурн 2. Земля 3. Юпитер 4. Меркурий\n"]
    questions.writelines(lines)

with open("data/right answers", mode="w", encoding="utf8") as right_answers:
    lines_answ = ["Земля\n", "Сириус\n", "Сатурн\n"]
    right_answers.writelines(lines_answ)

with open("data/questions", mode="r", encoding="utf8") as q:
    for index, line in enumerate(q):
        if index == 0:
            a = line
            print(a)
        elif index == 1:
            b = line
            print (b)
    answer_1 = input()
    with open("data/right answers", mode="r", encoding="utf8") as w:
        for index_answ, line in enumerate(w):
            if index_answ == 0:
                c = line.strip()
                if answer_1 == c:
                    print("Это правильный ответ")
                    sum_right_1 = 1
                    print("Вы получаете 1 бал")
                else:
                    sum_right_1 = 0
                    print("Это неправильный ответ. Вы не получаете баллов")

with open("data/questions", mode="r", encoding="utf8") as q:
    for index, line in enumerate(q):
        if index == 2:
            a = line
            print(a)
        elif index == 3:
            b = line
            print (b)
    answer_2 = input()
    with open("data/right answers", mode="r", encoding="utf8") as w:
        for index_answ, line in enumerate(w):
            if index_answ == 1:
                c = line.strip()
                if answer_2 == c:
                    print("Это правильный ответ")
                    sum_right_2 = 1
                    print("Вы получаете 1 бал")
                else:
                    sum_right_2 = 0
                    print("Это неправильный ответ. Вы не получаете баллов")

with open("data/questions", mode="r", encoding="utf8") as q:
    for index, line in enumerate(q):
        if index == 4:
            a = line
            print(a)
        elif index == 5:
            b = line
            print (b)
    answer_3 = input()
    with open("data/right answers", mode="r", encoding="utf8") as w:
        for index_answ, line in enumerate(w):
            if index_answ == 2:
                c = line.strip()
                if answer_3 == c:
                    print("Это правильный ответ")
                    sum_right_3 = 1
                    print("Вы получаете 1 бал")
                else:
                    sum_right_3 = 0
                    print("Это неправильный ответ. Вы не получаете баллов")
sum_all=sum_right_1+sum_right_2+sum_right_3
print(f"Вы набрали:",sum_all,"балла")

