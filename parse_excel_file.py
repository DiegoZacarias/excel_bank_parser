# import sys
import pandas as pd

def parse_excel(excel_path):
    
    print(excel_path)
    # Read Excel file
    df = pd.read_excel(excel_path, skiprows=8, usecols='A:F', skipfooter=5)
    print(df)
    df.to_csv('tests/parsed_file.csv', index=False)
    print('The file has been created...')

def test():
    print('este es un test')
