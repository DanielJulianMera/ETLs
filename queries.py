import pandas as pd
import sqlite3

# Cargar los datos desde los archivos CSV
calidad_aire_df = pd.read_csv('calidad_aire_df.csv')
demografia_df = pd.read_csv('demografia_df.csv')

# Conectar a la base de datos SQLite (se crea automáticamente si no existe)
conn = sqlite3.connect('ciudades.db')

# Guardar los DataFrames en la base de datos
calidad_aire_df.columns = [col.replace('.', '_') for col in calidad_aire_df.columns]  # Ajustar los nombres de columnas
calidad_aire_df.to_sql('calidad_aire', conn, if_exists='replace', index=False)
demografia_df.to_sql('demografia', conn, if_exists='replace', index=False)

# Realizar un JOIN y agregar datos para verificar si las ciudades más pobladas tienen la peor calidad del aire
query = '''
SELECT d.City, d.[Total Population] as Population, ca.CO, ca.PM10, ca.SO2, ca.PM2_5, ca.O3, ca.NO2,
       (ca.CO + ca.PM10 + ca.SO2 + ca.PM2_5 + ca.O3 + ca.NO2) AS total_concentration
FROM demografia d
JOIN calidad_aire ca ON d.City = ca.City
ORDER BY d.[Total Population] DESC
LIMIT 11
'''

result = pd.read_sql_query(query, conn)
conn.close()

print(result)