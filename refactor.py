import subprocess
import os

dictionary1 = "dict.txt.gz"
bat_path = os.getcwd() + "\hashcat.exe"
hash_list = "hash.txt"


def split_values(line):
    """
    Функция для разделения значений в строке через символ ":"
    :param line: строка, содержащая значения, разделенные символом ":"
    :return: список значений, разделенных символом ":"
    """
    values = line.strip().split(":")
    values_split = values.pop()
    return values

def split_values_pass(line):
    """
    Функция для разделения значений в строке через символ ":"
    :param line: строка, содержащая значения, разделенные символом ":"
    :return: список значений, разделенных символом ":"
    """
    values = line.strip().split(":")
    return values

def read_file(filename):
    """
    Функция для чтения многострочного файла
    :param filename: имя файла
    :return: список списков значений, разделенных символом ":"
    """
    with open(filename, "r") as file:
        lines = file.readlines()
        
        values_list = [split_values(line) for line in lines]
        
    return values_list

def read_file_pass(filename):
    """
    Функция для чтения многострочного файла
    :param filename: имя файла
    :return: список списков значений, разделенных символом ":"
    """
    with open(filename, "r") as file:
        lines = file.readlines()
        
        values_list = [split_values_pass(line) for line in lines]
        
    return values_list

def save_hash(values):
    with open("hash.txt", 'a') as f: 
        
        f.write(values + '\n')

def save_password(values):
    with open("valid.txt", 'a') as f: 
        
        f.write(str(values) + '\n')

values_list = read_file(os.getcwd() + "/db.txt")

def find_common_lines(file1, file2):

    db = read_file(file1)
    password = read_file_pass(file2)

    for db_list in db:
        hash = db_list
        for password_list in password:
            if password_list[0] == hash[4]:
                valid = hash[1], password_list[1]
                save_password(valid)

    


print("--------------------")  # разделитель между списками значений
for values in values_list:
    # subprocess.call([bat_path, "-m", "1400","--show", values[4], ">", "pass.txt"], shell=True)
    # print(values[4])  # выводим только последнее значение
    save_hash(values[4])
print("--------------------")  # разделитель между списками значений
for values in values_list:
    # subprocess.call([bat_path, "-m", "1400","--show", values[4], ">", "pass.txt"], shell=True)
    # print(values[4])  # выводим только последнее значение
    save_hash(values[4])
subprocess.call([bat_path, "-m", "1400", "-w", "3", "-a", "0", hash_list, dictionary1], shell=True)    
subprocess.call([bat_path, "-m", "1400","--show", hash_list, ">", "pass.txt"], shell=True)

find_common_lines("db.txt", "pass.txt")

