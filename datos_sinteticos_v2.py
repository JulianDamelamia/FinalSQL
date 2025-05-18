import pandas as pd
import random
import os
from faker import Faker
import datetime
import numpy as np

fake = Faker('es_AR')
Faker.seed(41)
random.seed(41)


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

def generar_materias(n=10, lista_materias = None, departamentos=None):
    materias = []
    rango = len(lista_materias) if lista_materias is not None else n
    for i in range(1, n+1):
        materias.append({
            'id': i,
            'nombre': fake.catch_phrase() if lista_materias is None else random.choice(lista_materias),
            'duracion': 'cuatrimestral',
            'creditos': random.randint(4, 10),
            'horas_semanales': random.randint(2, 6),
            'asistencia_requerida': 75,
            'id_departamento': random.choice(list(departamentos['id'])) if departamentos is not None else 1
        })
    return pd.DataFrame(materias)

def generar_cursada(alumnos:pd.DataFrame, materias:pd.DataFrame, periodos_academicos:pd.DataFrame)-> pd.DataFrame:
    id_alumnos_list = list(alumnos['id'])
    id_materia_list =  list(materias['id'])
    id_periodo_academico_list = list(periodos_academicos['id'])
    cursada = []
    id_cursada = 1
    id_calificaciones = 1
    id_asistencia = 1
    for id_alumno in id_alumnos_list:
        cursada.append({
            'id': id_cursada,
            'id_alumno': id_alumno,
            'id_materia': random.choice(id_materia_list),
            'id_calificaciones': id_calificaciones,
            'id_asistencia': id_asistencia,
            'id_periodo_academico': random.choice(id_periodo_academico_list)
            })
        id_cursada += 1
        id_calificaciones += 1
        id_asistencia += 1
    return(pd.DataFrame(cursada))

def generar_periodos_academicos(n=10):
    periodos = []
    anio = 2026-n
    cuatrimestres_dict = {'1C':{'ini':3, 'fin':6}, '2C':{'ini':8, 'fin':11}}
    for i in range(n):
        periodos.append({
            'id':f'1C{anio}',
            'duracion': 'cuatrimestral',
            'fecha_inicio': datetime.date(anio, cuatrimestres_dict['1C']['ini'], 1),
            'fecha_fin': datetime.date(anio, cuatrimestres_dict['1C']['fin'], 30),

        })
        periodos.append({
            'id':f'2C{anio}',
            'duracion': 'cuatrimestral',
            'fecha_inicio': datetime.date(anio, cuatrimestres_dict['2C']['ini'], 1),
            'fecha_fin': datetime.date(anio, cuatrimestres_dict['2C']['fin'], 30),

        })
        periodos.append({
            'id':f'A{anio}',
            'duracion': 'anual',
            'fecha_inicio': datetime.date(anio, cuatrimestres_dict['1C']['ini'], 1),
            'fecha_fin': datetime.date(anio, cuatrimestres_dict['2C']['fin'], 30),

        })
        anio += 1
    return pd.DataFrame(periodos)

def generar_asistencia(df_cursada:pd.DataFrame) -> pd.DataFrame:
    asistencia_por_cursada = []
    pass
tipo_personal = pd.DataFrame([{'id': 1, 'descipcion': 'Docente', 'salario':123456}, {'id': 2, 'descipcion': 'No Docente', 'salario':123456}])
def generar_personal(docentes:pd.DataFrame, departamentos:pd.DataFrame, n_no_docentes=5, tipo_personal=tipo_personal):
    personal = []
    for i in range(1, n_no_docentes+1):
        nombre = fake.first_name()
        apellido = fake.last_name()
        personal.append({
            'id': i,
            'id_departamento':random.choice(list(departamentos['id'])) if departamentos is not None else 1,
            'nombre':nombre,
            'apellido':apellido,
            'email':f"{nombre.replace(' ','').lower()}_{apellido.replace(' ','').lower()}@{fake.free_email_domain()}",
            'estado':random.choices(['activo', 'licencia','inactivo'], weights=[20, 5, 2], k=1)[0],
            'id_tipo_personal':2,
            'antiguedad':random.randint(1, 30),
        })
        #TODO: falta agregar los docentes que haya generado en el dict docentes con id_tipo_personal = 1
        pass
    # return pd.DataFrame(personal)
def generar_departamentos(n=2):
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

def generar_carreras(n=4, lista_carreras = None):
    carreras = []
    rango = len(lista_carreras) if lista_carreras is not None else n
    for i in range(1, rango+1):
        carreras.append({
            'id': i,
            'titulo': fake.job().capitalize() if lista_carreras is None else lista_carreras[i-1],
        })
    return pd.DataFrame(carreras)




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

def generar_plan_estudio(materias:dict, carreras:dict, materias_por_carrera:int =5):
    plan = []
    for id_carrera in list(carreras['id']):
        anio_actualizacion = random.randint(1980, 2024)
        for i in range(1, materias_por_carrera+1):
            plan.append({
                'id': i,
                'id_carrera': id_carrera,
                'anio_actualizacion':anio_actualizacion,
                'creditos_requeridos': random.randint(120, 200),
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



