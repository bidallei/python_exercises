import PyPDF2
import pandas as pd

archivopdf = "./pdfejemplo.pdf"

# Abrir el archivo PDF
with open(archivopdf, 'rb') as archivo_pdf:
    lector_pdf = PyPDF2.PdfReader(archivo_pdf)
    texto = ''
    for pagina in lector_pdf.pages:
        texto += pagina.extract_text()

# Limpiar el texto y convertirlo a una lista de líneas
lineas = texto.split('\n')

# Crear un DataFrame de pandas
df = pd.DataFrame(lineas, columns=['Texto'])

# Guardar el DataFrame en un archivo Excel
df.to_excel('archivo.xlsx', index=False)