from faker import Faker
import pandas as pd

def exportarCSV(datos):
    exportar = pd.DataFrame(datos)
    exportar.to_csv('registros.csv', index=False)
    
    
fake = Faker()
n = 50
datos = {}

for i in range(n):
    datos[i] = {
        'nombre': fake.name(),
        'correo': fake.email(),
        'direccion': fake.address(),
        'usuario': fake.user_name()
    }

exportarCSV(datos)