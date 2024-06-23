import pandas as pd

# Cargar los datos demográficos desde un archivo CSV
url = "https://public.opendatasoft.com/explore/dataset/us-cities-demographics/download/?format=csv&timezone=Europe/Berlin&lang=en&use_labels_for_header=true&csv_separator=%3B"
demografia_df = pd.read_csv(url, sep=';')

# Eliminar columnas no deseadas
columnas_a_eliminar = ['Race', 'Count', 'Number of Veterans']
demografia_df = demografia_df.drop(columns=[col for col in columnas_a_eliminar if col in demografia_df.columns])

# Eliminar filas duplicadas
demografia_df = demografia_df.drop_duplicates()

# Guardar el DataFrame limpio en un archivo CSV
demografia_df.to_csv('demografia_df_limpio.csv', index=False)

print("Datos demográficos cargados, limpiados y guardados con éxito.")