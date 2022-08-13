import openpyxl
from find_all_value import find_value
from decoding_data import decoding_operation
from find_description_operation import find_description

data = find_value()
data_1 = decoding_operation()
my_dict = find_description()

book = openpyxl.Workbook()
sheet = book.active
book_1 = openpyxl.open("ValueStreamMapping.xlsx", read_only=True)
sheet_4 = book_1.worksheets[4]

# Заполнение шапки документа
sheet['A1'] = 'ОБОЗНАЧЕНИЕ'
sheet['B1'] = 'НАИМЕНОВАНИЕ'
sheet['C1'] = 'МАРШРУТ'
sheet['D1'] = 'ВХОДИМОСТЬ'
sheet['E1'] = 'ПАРТИЯ'
sheet['F1'] = 'ЦЕНА за шт.'
sheet['G1'] = 'ЦЕНА за комплект'
sheet['H1'] = '№ ОПЕРАЦИИ'
sheet['I1'] = 'НАИМЕНОВАНИЕ ОПЕРАЦИИ'
sheet['J1'] = 'ОБОРУДОВАНИЕ'
sheet['K1'] = 'Тпз, мин'
sheet['L1'] = 'Тшт, мин'
sheet['M1'] = 'КОИД'

#Заполнение общей части информации о детали
sheet['A2'].value = data[2]
sheet['B2'].value = data[1]
sheet['C2'].value = data[8]
if data[1] == 'Ролик РВП':
    sheet['D2'].value = 7
elif data[1] == 'Сепаратор РВП':
    sheet['D2'].value = 2
else:
    sheet['D2'].value = 1
sheet['E2'].value = 50 * sheet['D2'].value

#Заполнение данных о каждой операции
row = 2
for i in data_1:
    if len(i) > 6:
        sheet[row][10].value = i[3]
        sheet[row][11].value = i[4]
        sheet[row][12].value = i[5]
    elif len(i) <= 3:
        sheet[row][10].value = i[1]
        sheet[row][11].value = i[2]
        sheet[row][7].value = i[0]
    elif len(i) > 3 and len(i) <= 6:
        sheet[row][10].value = i[1]
        sheet[row][11].value = i[2]
        sheet[row][7].value = i[0]
        sheet[row+1][10].value = i[4]
        sheet[row+1][11].value = i[5]
        sheet[row+1][7].value = i[3]
        row += 1
    row += 1

# Заполнение описания операций
column = []
for key in my_dict:
    column.append(my_dict[key])
column_operation = column [10:]

new_row = 2
for val in column_operation:
    for all_val in val:
        if all_val < 47:
            sheet[new_row][7].value = sheet_4[19][all_val].value
        sheet[new_row][8].value = sheet_4[17][all_val].value
        if all_val > 46:
            sheet[new_row][9].value = sheet_4[5][all_val].value
            new_row += 1
        else:
            sheet[new_row][9].value = sheet_4[5][all_val].value
    new_row += 1

book.save("technology.xlsx")
book.close()

print("Файл technology.xlsx записан")
