"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import re

def ingest_data():
    with open('clusters_report.txt', 'r') as f:
        line1 = re.split(r'\s{2,}', f.readline().strip())
        line2 = re.split(r'\s{2,}', f.readline().strip())
        lines = f.readlines()
# Combina las dos líneas para formar los nombres de las columnas
    for i in range(len(line1)):
        if line1[i] == "Porcentaje de" or line1[i]=="Cantidad de":
            line1[i] = line1[i] + " " + line2[0]
 
    data = []
    for line in lines:
        fields = line.split('\t')
        
        column1 = fields[0]
        print(column1)
        """column2 = fields[2]
        column3 = fields[6]
        column4 = fields[9]
        data.append([column1, column2, column3, column4])"""
    #df = pd.DataFrame(data, columns=line1)
    #return df[1]
    
print(ingest_data())