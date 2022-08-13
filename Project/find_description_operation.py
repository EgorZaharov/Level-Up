from find_all_value import find_value


def find_description():  # нахождение всех значений в строке необходимых для расшифровки

    data = find_value()
    my_dict = {}
    index = 0
    for i in data:
        if i in my_dict:
            my_dict[i].append(index)
        else:
            my_dict[i] = [index]
        index += 1

    return my_dict
