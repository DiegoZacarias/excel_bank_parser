import os
from file_operations import create_folder, import_file, get_file_path

def prepare_process(project_dir, file_path, month, year):
    path = create_folder(project_dir, month, year)
    import_file(file_path, path)

def get_month_and_year_input():
    month = str(input("Enter the month: "))
    year = int(input("Enter the year: "))

    return month, year

def main():
    project_dir = os.getcwd()
    file_path = get_file_path(project_dir)
    month, year = get_month_and_year_input()
    prepare_process(project_dir, file_path, month, year)
    print('listo')

if __name__ == "__main__":
    main()
