import csv
import sys

def get_amount(row):
	# debito = int(row['Debitos'].replace('.', ''))
    debito = int(float(row['Debitos'].replace('.', '').replace(',', '.')))

	# credito = int(row['Creditos'].replace('.', ''))
    credito = int(float(row['Creditos'].replace('.', '').replace(',', '.')))
    
    if debito < 0 and credito == 0:
		# si debito es menor a 0 y credito es igual a 0, entonces debito es el valor a retornar
        return debito
    elif credito > 0 and debito == 0:
		# si credito es mayor a 0 y debito es igual a 0, entonces credito es el valor a retornar
        return credito

def actualizar_csv(csv_path, target_location):
    filas_actualizadas = []
    with open(csv_path, 'r') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)
		# Remove blank spaces from keys and values
        lector_csv.fieldnames = [field.strip() for field in lector_csv.fieldnames]
        rows_filtered = [{key: value.strip() for key, value in row.items()} for row in lector_csv if row['Fecha'].strip() != ""]

        for row in rows_filtered:
            row = {
                'Category': "",
                'Date': row['Fecha'],
                'Amount': get_amount(row),
                'Note': row['Descripcion']
                }
            filas_actualizadas.append(row)
    
    # # Escribir las filas actualizadas en un nuevo archivo CSV
    ruta_nuevo_csv = target_location + '/before_import.csv'
    with open(ruta_nuevo_csv, 'w', newline='') as nuevo_csv:
        fieldnames = filas_actualizadas[0].keys()
        escritor_csv = csv.DictWriter(nuevo_csv, fieldnames=fieldnames)
        escritor_csv.writeheader()
        escritor_csv.writerows(filas_actualizadas)

# Ruta del archivo CSV
# ruta_archivo_csv = 'files_aux/extracto.csv'
# actualizar_csv(ruta_archivo_csv, target_location)

# Actualizar el CSV y guardar los cambios en un nuevo archivo

# El archivo modificado es el que vamos a usar para el script financial.py, recordar agregar categorias