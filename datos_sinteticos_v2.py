import pandas as pd
import random
import os
from faker import Faker
import datetime
import numpy as np

fake = Faker('es_AR')
Faker.seed(41)
random.seed(41)

def generar_departamentos(n=4):
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

def generar_materias(n=10, departamentos=None):
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
        nombre = fake.first_name()
        apellido = fake.last_name()
        alumnos.append({
            'id': i,
            'nombre': nombre,
            'apellido': apellido,
            'email': f"{nombre.replace(' ','').lower()}_{apellido.replace(' ','').lower()}@{fake.free_email_domain()}",
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
        nombre = fake.first_name()
        apellido = fake.last_name()
        profesores.append({
            'id': i,
            'cargo': random.choice(list(cargos)),
            'dedicacion': random.choice(list(dedicaciones)),
            'salario': round(random.uniform(80000, 150000), 2),
            'titulo_academico': random.choice(list(titulos)),
            'id_departamento': random.choice(list(departamentos['id'])) if departamentos is not None else 1,
            'nombre': nombre,
            'apellido': apellido,
            'email': f"{nombre.replace(' ','').lower()}_{apellido.replace(' ','').lower()}@{fake.free_email_domain()}",
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


alumnos.to_csv('data/alumnos.csv', index=False)
materias.to_csv('data/materias.csv', index=False)
estudia.to_csv('data/estudia.csv', index=False)
dicta.to_csv('data/dicta.csv', index=False)
departamentos.to_csv('data/departamentos.csv', index=False)
tipo_becas.to_csv('data/tipo_becas.csv', index=False)
carreras.to_csv('data/carreras.csv', index=False)
plan_estudio.to_csv('data/plan_estudio.csv', index=False)
profesores.to_csv('data/profesores.csv', index=False)

