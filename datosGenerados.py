#Se importan las bibliotecas que se van a utilizar para esta practica
from faker import Faker
import pandas as pd

#Funcion que recibe los datos generados y los exporta por medio de Pandas en archivos .csv
def exportarCSV(datos):
    exportar = pd.DataFrame(datos)
    exportar.to_csv('registros.csv', index=False)
    
#Creacion de nuestras variables iniciales
fake = Faker()
n = 50
datos = {}

#Datos generados por medio de un 'for', la cantidad de datos basada en la variable int 'n'
for i in range(n):
    datos[i] = {
        'nombre': fake.name(),
        'correo': fake.email(),
        'direccion': fake.address(),
        'usuario': fake.user_name()
    }

#Se manda a llamar la funcion para exportar los datos generados
exportarCSV(datos)