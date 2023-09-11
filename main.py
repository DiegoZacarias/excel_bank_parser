# import sys
# import parse_excel_file
import os

def create_folder():
    month = str(input("Enter the month: "))
    year = int(input("Enter the year: "))

    project_dir = os.getcwd() + "/bank_files/"

    new_folder_name = str(month) + "_" + str(year)
    path = os.path.join(project_dir, new_folder_name)

    if not os.path.exists(path):
        os.makedirs(path)
    else:
        print(f"{new_folder_name} already exists at {project_dir}")

    # creating subfolders
    subfolders = ['original', 'parsed', 'before_import', 'spendee']

    for subfolder in subfolders:
        subfolder_path = os.path.join(path, subfolder)

        if not os.path.exists(subfolder_path):
            os.makedirs(subfolder_path)


def main():
    # path = sys.argv[1]
    # print(f'hola this is the path: {path}')
    # parse_excel_file.test()

    create_folder()

main()
