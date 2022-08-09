import openpyxl
from find_all_value import find_value
from decoding_data import decoding_operation

data = find_value()
data_1 = decoding_operation()

print(data_1)
book = openpyxl.Workbook()
sheet = book.active

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
sheet['K1'] = 'Тпз'
sheet['L1'] = 'Тшт'
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
        sheet[row][10] = i[3]
        sheet[row][11] = i[4]
        sheet[row][12] = i[5]
    elif len(i) <= 3:
        sheet[row][10] = i[1]
        sheet[row][11] = i[2]
        sheet[row][7] = i[0]
    elif len(i) > 3 and len(i) <= 6:
        sheet[row][10] = i[1]
        sheet[row][11] = i[2]
        sheet[row][7] = i[0]
        sheet[row+1][10] = i[4]
        sheet[row+1][11] = i[5]
        sheet[row+1][7] = i[3]
    row += 1
# sheet['K2'].value =
# sheet['L2'].value =
# sheet['M2'].value =

book.save("technology.xlsx")
book.close()
