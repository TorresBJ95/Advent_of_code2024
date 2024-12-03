from Problem_1 import comp_two_number_list
import os

def send_txt(txt_paths: list):
    problem = input("What problem do you want to running?: Just write ej: Problem1.txt \n")
    file_path = ''
    for path in txt_paths:
        name = path.split('/')[-1]
        if name.lower() == problem.lower():
            file_path = path
            break
    return file_path


if __name__ == '__main__':
    path = os.getcwd()
    files = os.listdir(path)
    txt_path = list()
    for file in files:
        if file.endswith(".txt"):
            to_save = os.path.join(path, file)
            txt_path.append(to_save)

    file_path = send_txt(txt_path)
    comp_two_number_list(file_path)


