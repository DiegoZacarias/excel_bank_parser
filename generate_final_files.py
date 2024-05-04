import os
from file_operations import create_folder, import_file, get_file_path
from generate_expenses_csv import generate_expenses_csv
from generate_incomes_csv import generate_incomes_csv

def get_month_and_year_input():
    month = str(input("Enter the month: "))
    year = int(input("Enter the year: "))

    return month, year

def generate():
    project_dir = os.getcwd()

    month, year = get_month_and_year_input()
    bank_files_dir = os.path.join(project_dir, "bank_files")
    folder_name = f"{month}_{year}"
    path = os.path.join(bank_files_dir, folder_name)
   
    # parse excel 
    path_with_before_import_file = os.path.join(path, 'before_import/before_import.csv')
    target_location = os.path.join(path, "spendee/")

    generate_expenses_csv(path_with_before_import_file, target_location)
    generate_incomes_csv(path_with_before_import_file, target_location)

    print('listo, ahora solo debes importar los archivos csv en spendee, los archivos estan en la carpeta spendee')

# if __name__ == "__main__":
generate()
