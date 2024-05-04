import csv
import datetime

category_mapping = {
    'Car prestamo': 'Bills & Fees',
    'Clothes': 'Clothes',
    'Cuentas mensuales': 'Bills & Fees',
    'Eating Out': 'Food & Drink (out)',
    'Entertainment': 'Entertainment',
    'Extra auto': 'Car',
    'Food in home': 'Food in home',
    'Fuel': 'Fuel',
    'General': 'Other',
    'Health': 'Healthcare',
    'Shopping': 'Shopping',
    'Shopping online': 'Shopping online',
    'Sports': 'Sport & Hobbies',
    'Transferencias': 'Other',
    'Travel': 'Travel',
    'Work': 'Work'
}

def fix_row(row):
    if row['Category'] in category_mapping:
        row['Category'] = category_mapping[row['Category']]

	# Convert 'Amount' to positive
    row['Amount'] = abs(int(row['Amount']))

	# Reformat 'Date' from dd/mm/yyyy to mm/dd/yyyy
    row['Date'] = datetime.datetime.strptime(row['Date'], '%d/%m/%Y').strftime('%m/%d/%Y')

    return row

def generate_expenses_csv(csv_path, target_location):
    filas_actualizadas = []
    with open(csv_path, 'r') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)
        
		# Remove blank spaces from keys
        lector_csv.fieldnames = [field.strip() for field in lector_csv.fieldnames]
        
        rows_filtered = [{key: value.strip() for key, value in row.items()} for row in lector_csv if int(row['Amount']) < 0]

        for row in rows_filtered:
            row = fix_row(row)
            row = {'Category': row['Category'], 'Date': row['Date'], 'Amount': row['Amount'], 'Note': row['Note']}
            filas_actualizadas.append(row)
    
    # Escribir las filas actualizadas en un nuevo archivo CSV
    ruta_nuevo_csv = target_location + '/expenses.csv'
    with open(ruta_nuevo_csv, 'w', newline='') as nuevo_csv:
        fieldnames = filas_actualizadas[0].keys()
        escritor_csv = csv.DictWriter(nuevo_csv, fieldnames=fieldnames)
        escritor_csv.writeheader()
        escritor_csv.writerows(filas_actualizadas)
