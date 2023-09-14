import os
import helpers

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

def check_file(project_dir):
    path = project_dir + "/aux/"
    file = os.listdir(path)[0]
    file_path = os.path.join(path, file)
    result = helpers.is_xlsx(file_path)
    if not result:
        raise Exception(f"File should be .xlsx. File path: {file_path}")

def get_file_path(project_dir):
    aux_folder_path = project_dir + "/aux/"
    try:
        files = os.listdir(aux_folder_path)
        if len(files) == 0:
            raise Exception("Folder 'aux/' is empty")
        if len(files) > 1:
            raise Exception(f"Folder 'aux/' should contains only 1(one) file. Contains {len(files)}")
        check_file(project_dir)
        return os.path.join(aux_folder_path, files[0])
        
    except Exception as e:
        print(e)
        print("Skipping folder creation")
        print("Skipping process")
        raise
