import openpyxl

from find_all_value import find_value


def find_value_without(): #нахождение всех значений в строке необходимых для расшифровки
    book = openpyxl.open("ValueStreamMapping.xlsx", read_only=True)
    sheet_4 = book.worksheets[4]

    my_list = find_value()
    my_list_new = my_list [10:]

    data = []
    for i in my_list_new:
        if len(i) >= 2:
            data.append(i)

    for l in data:
        if l == 'Default':
            data[data.index(l)] = sheet_4['AT18'].value
    book.close()
    return data