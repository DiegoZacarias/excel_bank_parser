import os
from file_operations import create_folder, import_file, get_file_path
from parse_excel_file import parse_excel
from clean_csv import actualizar_csv

def prepare_process(project_dir, file_path, month, year):
    path = create_folder(project_dir, month, year)
    import_file(file_path, path)
    return path

def get_month_and_year_input():
    month = str(input("Enter the month: "))
    year = int(input("Enter the year: "))

    return month, year

def main():
    project_dir = os.getcwd()
    file_path = get_file_path(project_dir)
    month, year = get_month_and_year_input()
    path = prepare_process(project_dir, file_path, month, year)

    # parse excel 
    path_with_original_file = os.path.join(path, 'original/original.xlsx')
    target_location_parsed = os.path.join(path, "parsed/")
    parse_excel(path_with_original_file, target_location_parsed )
    # path_with_parsed_file = os.path.join('parsed/parsed.csv')
    path_with_parsed_file = os.path.join(path, 'parsed/parsed.csv')
    # print('test')
    # print(path_with_parsed_file)
    # print(path_with_original_file)
    target_location_before_import = os.path.join(path, "before_import/")
    actualizar_csv(path_with_parsed_file, target_location_before_import)

    print('listo, ahora solo debes agregar las categorias al archivo csv en la carpeta before_import')
    print('y luego ejecutar el archivo generate_final_csvs.py')

if __name__ == "__main__":
    main()
