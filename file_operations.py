import os
import helpers

def create_folder(project_dir):
    month = str(input("Enter the month: "))
    year = int(input("Enter the year: "))
    bank_files_dir = os.path.join(project_dir, "bank_files")
    new_folder_name = f"{month}_{year}"
    path = os.path.join(bank_files_dir, new_folder_name)
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        print(f"{new_folder_name} already exists at {project_dir}")
    subfolders = ['original', 'parsed', 'before_import', 'spendee']
    for subfolder in subfolders:
        subfolder_path = os.path.join(path, subfolder)
        if not os.path.exists(subfolder_path):
            os.makedirs(subfolder_path)
    return path

def import_file(file_path, to):
    target_path = os.path.join(to, "original/")
    helpers.move_file(file_path, target_path)

def check_file(project_dir):
    path = project_dir + "/aux/"
    file = os.listdir(path)[0]
    file_path = os.path.join(path, file)
    result = helpers.is_xlsx(file_path)
    if not result:
        raise Exception(f"File should be .xlsx. File path: {file_path}")
