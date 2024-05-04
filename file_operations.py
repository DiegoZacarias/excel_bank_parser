import os
import helpers
from pathlib import Path

def create_folder(project_dir, month, year):
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

def check_file(file_path):
    result = helpers.is_xlsx(file_path)
    if not result:
        raise Exception(f"File should be .xlsx. File path: {file_path}")

def get_file_path(project_dir):
    aux_folder_path = project_dir + "/aux/"
    try:
        files = os.listdir(aux_folder_path)
        # Filter to include only .xlsx files
        xlsx_files = [file for file in files if file.endswith('.xlsx')]

        if len(xlsx_files) == 0:
            raise Exception("Folder 'aux/' is empty")
        if len(xlsx_files) > 1:
            raise Exception(f"Folder 'aux/' should contains only 1(one) file. Contains {len(xlsx_files)}")

        file_path_in_aux = os.path.join(aux_folder_path, xlsx_files[0])
        check_file(file_path_in_aux)
        return file_path_in_aux
        
    except Exception as e:
        print(e)
        print("Skipping folder creation")
        print("Skipping process")
        raise

def rename_file(file_path, new_file_name):
    try:
        if not Path(file_path).is_file() :
            raise Exception(f"File doesn't exist. File path: {file_path}")
        # Extract directory path and file name
        directory, old_file_name = os.path.split(file_path)

        # Create the new file path with the new file name
        new_file_path = os.path.join(directory, new_file_name)

        # Rename the file
        os.rename(file_path, new_file_path)
        print(f"File '{file_path}' has been renamed to '{new_file_path}'.")
        return new_file_path
    except Exception as e:
        print(e)
        print("Skipping process")
        raise