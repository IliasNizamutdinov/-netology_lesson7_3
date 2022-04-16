import os

def get_file_path(dir_name, file_name):
    return os.path.join(os.getcwd(),dir_name,file_name)

def get_dict_file(f_name, f_path,coding,dict_file):
    with open(f_path, 'r', encoding=coding) as file:
        count = sum(1 for line in file) #получаем количество строк
        dict_file.setdefault(count, [f_name,f_path]) #в значении будем хранить имя файла и длинный путь

def uninon_files(dict_file,all_path,coding):
    with open(all_path, 'w', encoding=coding) as file:
        for key, val in sorted(dict_file.items()):
            file.write(str(key) + '\n')  # записываем размер строк
            file.write(val[0] + '\n')  # Записываем название файла
            with open(val[1], 'r', encoding=coding) as file_list:
                line = file_list.readline()
                while line:
                    file.write(line)
                    line = file_list.readline()
                file.write('\n')

def main():

    dir_name = 'files'
    all_name = 'all.txt'
    file1_name = '1.txt'
    file2_name = '2.txt'
    file3_name = '3.txt'

    coding = 'utf-8'

    all_path = get_file_path(dir_name,all_name)
    f_path_1 = get_file_path(dir_name,file1_name)
    f_path_2 = get_file_path(dir_name,file2_name)
    f_path_3 = get_file_path(dir_name,file3_name)


    dict_file = {}

    get_dict_file(file1_name,f_path_1,coding,dict_file)
    get_dict_file(file2_name,f_path_2,coding,dict_file)
    get_dict_file(file3_name,f_path_3,coding,dict_file)

    uninon_files(dict_file,all_path,coding)


main()