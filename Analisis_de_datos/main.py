import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def cargar_datos(archivo):
    """Carga los datos desde un archivo CSV"""
    try:
        df = pd.read_csv(archivo)
        print(f"Datos cargados exitosamente: {df.shape[0]} filas, {df.shape[1]} columnas")
        return df
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{archivo}'")
        return None

def calcular_estadisticas(df, columna):
    """Calcula estadísticas descriptivas para una columna"""
    return {
        'media': df[columna].mean(),
        'mediana': df[columna].median(),
        'desviacion': df[columna].std(),
        'minimo': df[columna].min(),
        'maximo': df[columna].max()
    }

def mostrar_estadisticas(df, columna):
    """Muestra las estadísticas de una columna"""
    stats = calcular_estadisticas(df, columna)
    print(f"\n--- Estadísticas de {columna} ---")
    print(f"Media: {stats['media']:.2f}")
    print(f"Mediana: {stats['mediana']:.2f}")
    print(f"Desviación Estándar: {stats['desviacion']:.2f}")
    print(f"Mínimo: {stats['minimo']:.2f}")
    print(f"Máximo: {stats['maximo']:.2f}")

def crear_grafico(df, x_col, y_col):
    """Crea un gráfico de dispersión"""
    plt.figure(figsize=(10, 6))
    plt.scatter(df[x_col], df[y_col], alpha=0.7, s=50)
    plt.title(f'Gráfico de Dispersión: {x_col} vs {y_col}')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

def main():
    """Función principal del análisis"""
    # Cargar datos
    df = cargar_datos('text.csv')
    if df is None:
        return
    
    # Mostrar información básica del dataset
    print("\nPrimeras 5 filas del dataset:")
    print(df.head())
    
    # Análisis estadístico para ambas columnas
    columnas = ['Col1', 'Col2']
    for col in columnas:
        if col in df.columns:
            mostrar_estadisticas(df, col)
        else:
            print(f"Advertencia: La columna '{col}' no existe en el dataset")
    
    # Crear gráfico de dispersión
    if 'Col1' in df.columns and 'Col2' in df.columns:
        crear_grafico(df, 'Col1', 'Col2')
    else:
        print("No se puede crear el gráfico: faltan las columnas necesarias")

if __name__ == "__main__":
    main()
