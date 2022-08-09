import openpyxl

def find_value():  # нахождение всех значений в строке
    id_route = input("Введите ID маршрута: ")
    book = openpyxl.open("ValueStreamMapping.xlsx", read_only=True)
    sheet_4 = book.worksheets[4]

    for row in range(20, sheet_4.max_row + 1):
        ID_way = sheet_4[row][8].value
        if ID_way == id_route:
            number_stroke = row
            break

    my_list = []
    for cell in sheet_4[number_stroke]:
        my_list.append(cell.value)
    book.close()
    return my_list
