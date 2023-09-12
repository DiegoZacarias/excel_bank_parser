import shutil
from pathlib import Path

def is_xlsx(file_path):
    print(f'the file name is: {file_path}')
    with open(file_path, 'rb') as f:         
        first_four_bytes = f.read()[:4] 

    return first_four_bytes == b'PK\x03\x04'

def move_file(from_path, to_path):
    try:
        if not Path(from_path).is_file() :
            raise Exception(f"File doesn't exist. File path: {from_path}")

        shutil.move(from_path, to_path)
    except Exception as e:
        print(e)
        print("Skipping process")
        raise

