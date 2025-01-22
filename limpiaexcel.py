import pandas as pd

# Leer el archivo Excel
df = pd.read_excel('./archivo.xlsx')

# Función para eliminar espacios y copiar en la columna de al lado
def eliminar_espacios_copiar(x):
    return x.str.replace(' ', '').str.strip()

# Aplicar la función a cada columna
for i in range(len(df.columns)):
    df[df.columns[i] + '_sin_espacios'] = eliminar_espacios_copiar(df[df.columns[i]])

# Guardar el resultado en un nuevo archivo Excel
df.to_excel('archivo_sin_espacios.xlsx', index=False)