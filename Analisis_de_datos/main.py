import pandas as pd

try:
    df = pd.read_csv('text.csv')
    print("El archivo se ha leido correctamente")
    print(df.head())
    print("El archivo se ha leido correctamente")
except FileNotFoundError:
    print("El archivo no existe ")
    exit(1)

# -------------------
# 2. Análisis Estadístico
# -------------------

print("\n--- Estadísticas de la Columna 1 (Col1) ---")
media_col1 = df['Col1'].mean()
mediana_col1 = df['Col1'].median()
desv_col1 = df['Col1'].std()

print(f"Media de Col1: {media_col1:.2f}")
print(f"Mediana de Col1: {mediana_col1:.2f}")
print(f"Desviación Estándar de Col1: {desv_col1:.2f}")

print("\n--- Estadísticas de la Columna 2 (Col2) ---")
media_col2 = df['Col2'].mean()
mediana_col2 = df['Col2'].median()
desv_col2 = df['Col2'].std()

print(f"Media de Col2: {media_col2:.2f}")
print(f"Mediana de Col2: {mediana_col2:.2f}")
print(f"Desviación Estándar de Col2: {desv_col2:.2f}")
import matplotlib.pyplot as plt

plt.scatter(df['Col1'], df['Col2'])
plt.title('Scatter Plot de Col1 vs Col2')
plt.xlabel('Col1')
plt.ylabel('Col2')
plt.grid(True)
plt.show()
