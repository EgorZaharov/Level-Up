import json

answer_1 = input("Третья планета от Солнца?")
answer_2 = input("Самая яркая звезда?")
answer_3 = input("Планета с кольцами?")

r = [["Третья планета от Солнца?",answer_1], ["Самая яркая звезда?",answer_2], ["Планета с кольцами?",answer_3]]
t = dict(r)

# with open('json_data.json', 'w', encoding="utf8") as outfile:
#     json.dump(t, outfile)
#
# with open('json_data.json', encoding="utf8") as json_file:
#     t = json.load(json_file)
#     if answer_1 == "Земля":
#         q = 1
#     else:
#         q = 0
#     if answer_2 == "Сириус":
#         q1 = 1
#     else:
#         q1 = 0
#     if answer_3 == "Сатурн":
#         q2 = 1
#     else:
#         q2 = 0
#     q_sum = q + q1 + q2
#     print(q_sum)

import pickle

with open('answer.pickle', 'wb') as file:
    pickle.dump(t, file)

with open('answer.pickle', 'rb') as file:
    if answer_1 == "Земля":
        q = 1
    else:
        q = 0
    if answer_2 == "Сириус":
        q1 = 1
    else:
        q1 = 0
    if answer_3 == "Сатурн":
        q2 = 1
    else:
        q2 = 0
    q_sum = q + q1 + q2
    k = pickle.load(file)
    print(k, f"Ваш результат: {q_sum} бала")