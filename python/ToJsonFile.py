import os,re
import json


file_name = 'res'

def init_table(init_path):

    dict = get_valuename_value_dict(init_path)


    with open("C:/Users/76585/Desktop/res.json", 'w') as f:
        json.dump(dict, f, sort_keys=True,indent =4,ensure_ascii=False)
    f.close()

def get_valuename_value_dict(file_path):
    dict = {}
    # dict_min = {}

    f = open(file_path)
    line = f.readline()

    while line:
        tmp = line[:2]
        if tmp == '//' :
            line = f.readline()
            continue

        if line.find('*') != -1:
            line = f.readline()
            continue

        if line.find('#') != -1:
            line = f.readline()
            continue

        new_line = re.split(r'[;,\t,\s,=,\n]\s*', str(line))

        for i in new_line:
            if i == '':
                new_line.remove(i)
            if len(new_line) >= 3:
                print new_line[0]
                print new_line[1]
                print new_line[3]
                dict[new_line[1]] = new_line[3]
                # print new_line[2]
                break
        line = f.readline()
    f.close()
    return dict

if __name__ == '__main__':
    file_path = 'C:/Users/76585/Desktop/ceshi/cfd_para_self.hypara'
    # dict = get_valuename_value_dict(file_path)
    init_table(file_path)