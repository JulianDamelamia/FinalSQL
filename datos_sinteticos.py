# -*- coding: utf-8 -*-
"""
Created on Sat May 17 18:30:25 2025

@author: Usuario
"""

import pandas as pd
import numpy as np
import os
import datetime
from faker import Faker
import random
fake = Faker()

df = pd.read_csv('Supabase Snippet Retrieve Column Information.csv')
tablas = list(df.table_name.unique())
dtype = list(df.data_type.unique())
dtype_dict = {
        'integer': 'int',
        'character varying': 'str',
        'character': 'str',
        'date': 'datetime.date',
        'timestamp with time zone': 'datetime.datetime',
        'double precision': 'float',
        'numeric': 'float',
    }

for tabla in tablas:
    lista_columnas = list(df[df['table_name'] == tabla].column_name)
    print(f'Tabla: {tabla}')
    dict(zip (lista_columnas, [ []*len(lista_columnas) ] ))
    # tabla_nueva = pd.DataFrame(columns = list(df[df['table_name'] == tabla].column_name), index = false)
#%%
fake = Faker("es_AR")

# Generador con contexto (para nombre/apellido/email consistentes)
class GeneradorContextual:
    def __init__(self):
        self.contador_id = {}

    def generar_dato(self, tipo, columna, contexto):
        if columna == 'id':
            tabla = contexto['tabla']
            if tabla not in self.contador_id:
                self.contador_id[tabla] = 1
            valor = self.contador_id[tabla]
            self.contador_id[tabla] += 1
            return valor

        elif 'telefono' in columna.lower():
            return f"11-{random.randint(1000,9999)}-{random.randint(1000,9999)}"

        elif 'email' in columna.lower():
            nombre = contexto.get('nombre') or fake.first_name().lower()
            apellido = contexto.get('apellido') or fake.last_name().lower()
            dominio = fake.free_email_domain()
            return f"{nombre}_{apellido}@{dominio}"
        
        elif 'direccion' in columna.lower():
            return fake.street_address()
        
        elif tipo == 'integer':
            return random.randint(1, 1000)
        elif tipo in ['character varying', 'character']:
            if columna.lower() == 'nombre':
                contexto['nombre'] = fake.first_name().lower()
                return contexto['nombre'].capitalize()
            elif columna.lower() == 'apellido':
                contexto['apellido'] = fake.last_name().lower()
                return contexto['apellido'].capitalize()
            else:
                return fake.word().capitalize()
        elif tipo == 'date':
            return fake.date_between(start_date='-30y', end_date='today')
        elif tipo == 'timestamp with time zone':
            return fake.date_time_between(start_date='-5y', end_date='now')
        elif tipo in ['double precision', 'numeric']:
            return round(random.uniform(0, 10000), 2)
        else:
            return None

# Función principal
def generar_datos_sinteticos(df, cantidad=10):
    generador = GeneradorContextual()
    tablas = df['table_name'].unique()
    tablas_sinteticas = {}

    for tabla in tablas:
        subdf = df[df['table_name'] == tabla]
        columnas = list(subdf['column_name'])
        tipos = list(subdf['data_type'])

        datos = []
        for _ in range(cantidad):
            contexto = {'tabla': tabla}
            fila = {
                col: generador.generar_dato(tipo, col, contexto)
                for col, tipo in zip(columnas, tipos)
            }
            datos.append(fila)

        df_tabla = pd.DataFrame(datos)
        tablas_sinteticas[tabla] = df_tabla

    return tablas_sinteticas


tablas_generadas = generar_datos_sinteticos(df, cantidad=20)
alumno = tablas_generadas['alumno']
print(tablas_generadas['alumno'])
print(tablas_generadas['materia'])
#%%
import pandas as pd
import random

fake = Faker('es_AR')
Faker.seed(42)
random.seed(42)

def generar_departamentos(n=3):
    departamentos = []
    for i in range(1, n+1):
        departamentos.append({
            'id': i,
            'nombre': fake.company_suffix().capitalize()
        })
    return pd.DataFrame(departamentos)

def generar_tipo_becas():
    tipos = [
        {'id': 1, 'concepto_beca': 'Parcial', 'monto': 5000.0},
        {'id': 2, 'concepto_beca': 'Total', 'monto': 15000.0}
    ]
    return pd.DataFrame(tipos)

def generar_carreras(n=2):
    carreras = []
    for i in range(1, n+1):
        carreras.append({
            'id': i,
            'titulo': fake.job().capitalize()
        })
    return pd.DataFrame(carreras)

def generar_materias(n=5, departamentos=None):
    materias = []
    for i in range(1, n+1):
        materias.append({
            'id': i,
            'nombre': fake.catch_phrase(),
            'duracion': 'cuatrimestral',
            'creditos': random.randint(4, 10),
            'horas_semanales': random.randint(2, 6),
            'asistencia_requerida': 75,
            'id_departamento': random.choice(list(departamentos['id'])) if departamentos is not None else 1
        })
    return pd.DataFrame(materias)

def generar_alumnos(n=10, tipo_becas=None):
    alumnos = []
    for i in range(1, n+1):
        alumnos.append({
            'id': i,
            'nombre': fake.first_name(),
            'apellido': fake.last_name(),
            'email': f"{fake.first_name().lower()}_{fake.last_name().lower()}@{fake.free_email_domain()}",
            'telefono': f"11-{random.randint(1000,9999)}-{random.randint(1000,9999)}",
            'direccion': fake.street_address(),
            'nacimiento': fake.date_of_birth(minimum_age=18, maximum_age=30),
            'id_beca': random.choice(list(tipo_becas['id'])) if tipo_becas is not None else None
        })
    return pd.DataFrame(alumnos)

def generar_profesores(n=5, departamentos=None):
    profesores = []
    cargos = ['Profesor Titular', 'Profesor Adjunto', 'JTP', 'Ayudante']
    dedicaciones = ['Tiempo completo', 'Medio tiempo', 'Horas cátedra']
    titulos = ['Licenciado', 'Ingeniero', 'Magíster', 'Doctor']

    for i in range(1, n+1):
        profesores.append({
            'id': i,
            'cargo': random.choice(list(cargos)),
            'dedicacion': random.choice(list(dedicaciones)),
            'salario': round(random.uniform(80000, 150000), 2),
            'titulo_academico': random.choice(list(titulos)),
            'id_departamento': random.choice(list(departamentos['id'])) if departamentos is not None else 1,
            'nombre': fake.first_name(),
            'apellido': fake.last_name(),
            'email': f"{fake.first_name().lower()}_{fake.last_name().lower()}@{fake.free_email_domain()}",
            'estado': 'activo',
            'id_tipo_personal': 1,  # ejemplo fijo
            'antiguedad': random.randint(1, 30),
        })
    return pd.DataFrame(profesores)

def generar_plan_estudio(materias, carreras, n=10):
    plan = []
    for i in range(1, n+1):
        plan.append({
            'id': i,
            'anio_actualizacion': random.randint(2015, 2024),
            'creditos_requeridos': random.randint(120, 200),
            'id_carrera': random.choice(list(carreras['id'])),
            'id_materia': random.choice(list(materias['id'])),
        })
    return pd.DataFrame(plan)

def generar_estudia(alumnos, carreras, n=15):
    estudia = []
    estados = ['activo', 'egresado', 'retirado']
    for i in range(1, n+1):
        estudia.append({
            'id': i,
            'id_alumno': random.choice(list(alumnos['id'])),
            'id_carrera': random.choice(list(carreras['id'])),
            'estado': random.choice(estados),
            'creditos_acumulados': random.randint(0, 200),
        })
    return pd.DataFrame(estudia)

def generar_dicta(profesores, materias, n=10):
    dicta = []
    for i in range(1, n+1):
        dicta.append({
            'id': i,
            'id_profesor': random.choice(list(profesores['id'])),
            'id_materia': random.choice(list(materias['id'])),
        })
    return pd.DataFrame(dicta)


departamentos = generar_departamentos(3)
tipo_becas = generar_tipo_becas()
carreras = generar_carreras(5)
materias = generar_materias(departamentos=departamentos)
alumnos = generar_alumnos(tipo_becas=tipo_becas)
profesores = generar_profesores(departamentos=departamentos)
plan_estudio = generar_plan_estudio(materias, carreras)
estudia = generar_estudia(alumnos, carreras)
dicta = generar_dicta(profesores, materias)

# Mostrar un par de tablas como ejemplo
print(alumnos.head())
print(materias.head())
print(estudia.head())

# Guardar CSVs si querés
alumnos.to_csv('data/alumnos.csv', index=False)
materias.to_csv('data/materias.csv', index=False)
estudia.to_csv('data/estudia.csv', index=False)
dicta.to_csv('data/dicta.csv', index=False)
