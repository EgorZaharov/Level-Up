from find_value_operation import find_value_without

def decoding_operation():
    data = find_value_without()

    data_1 = []
    for i in data:
        data_1.append(i.split("_"))


    #return data_1, name, number_to, number_tool, time_pz, time_sht, qoid, btk_control, rm_control, name_ctr, time_pz_ctr, time_sht_ctr, name_ctr_1, time_pz_ctr_1, time_sht_ctr_1, name_ctr_2, time_pz_ctr_2, time_sht_ctr_2
    return data_1