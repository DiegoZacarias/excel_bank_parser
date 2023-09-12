import os
from file_operations import create_folder, import_file, check_file

def prepare_process(project_dir):
    try:
        aux_folder_path = project_dir + "/aux/"
        files = os.listdir(aux_folder_path)
        if len(files) == 0:
            raise Exception("Folder 'aux/' is empty")
        if len(files) > 1:
            raise Exception(f"Folder 'aux/' should contains only 1(one) file. Contains {len(files)}")
        check_file(project_dir)
        path = create_folder(project_dir)
        file_path_to_be_imported = os.path.join(aux_folder_path, files[0])
        import_file(file_path_to_be_imported, path)
    except Exception as e:
        print(e)
        print("Skipping folder creation")
        print("Skipping process")
        raise

def main():
    project_dir = os.getcwd()
    prepare_process(project_dir)
    print('listo')

if __name__ == "__main__":
    main()
