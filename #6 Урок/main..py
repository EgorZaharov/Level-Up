import json

answer_1 = input("Как тебя зовут?")
answer_2 = input("Сколько тебе лет?")
answer_3 = input("Есть ли у тебя собака?")

r = [["Как тебя зовут?",answer_1], ["Сколько тебе лет?"],answer_2, ["Есть ли у тебя собака?"],answer_3]

with open('json_data.json', 'w', encoding="utf8") as outfile:
    json.dump(r, outfile)

with open('json_data.json', encoding="utf8") as json_file:
    r = json.load(json_file)
    print(r)