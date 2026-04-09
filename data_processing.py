import pandas as pd
 
# Cargar datos
df = pd.read_csv("Datos.csv")
 
# Eliminar columna de ID (no aporta información predictiva)
df = df.drop(columns=["Sample code number"])
 
# Convertir Class: 2 (benigno) -> 0, 4 (maligno) -> 1
df["Class"] = df["Class"].map({2: 0, 4: 1})
 
# Guardar nuevo CSV
df.to_csv("Datos_clean.csv", index=False)
 
print("Preprocesamiento completado.")