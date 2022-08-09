from find_value_operation import find_value_without

def decoding_operation(): #Декодирует список кодов до элементов
    data = find_value_without()

    data_1 = []
    for i in data:
        data_1.append(i.split("_"))

    return data_1