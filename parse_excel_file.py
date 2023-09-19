import pandas as pd

def parse_excel(excel_path, target_location):
    
    print(excel_path)
    # Read Excel file
    df = pd.read_excel(excel_path, skiprows=8, usecols='A:F', skipfooter=5)
    print(df)
    df.to_csv(target_location + '/parsed_file.csv', index=False)
    print('The file has been created...')
    print(target_location+'/parsed_file.csv')
