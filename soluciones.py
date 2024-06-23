import pandas as pd
from typing import Set

def ej_1_cargar_datos_demograficos() -> pd.DataFrame:
    # Leer el archivo CSV con los datos demográficos ya generados
    demografia_df = pd.read_csv('demografia_df.csv')
    return demografia_df

def ej_2_cargar_calidad_aire() -> pd.DataFrame:
    # Leer el archivo CSV con los datos de calidad del aire ya generados
    calidad_aire_df = pd.read_csv('calidad_aire_df.csv')
    return calidad_aire_df