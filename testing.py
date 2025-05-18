from datos_sinteticos_v2 import *

departamentos = generar_departamentos(3)
tipo_becas = generar_tipo_becas()
lista_carreras = ['Ciencias de Datos', 'Ciencias de la comunicación', 'Licenciatura en Física', 'Diseño Gráfico']
carreras = generar_carreras(4, lista_carreras=lista_carreras)

lista_materias = [
    'Análisis 1', 'Análisis 2: la venganza de Leibniz', 'Querida, integré a los niños!', 'Mate Lavado 1',
    'Física 1', 'Física 2: 2 Harmonic 2 Oscillate', 'Física 3: el último oscilador',
    'Dibujo Técnico', 'Estadística', 'Historia del Arte', 'Literatura', 
]
materias = generar_materias(lista_materias=lista_materias, departamentos=departamentos)
plan_estudio = generar_plan_estudio(materias, carreras)
alumnos = generar_alumnos(tipo_becas=tipo_becas)

# profesores = generar_profesores(departamentos=departamentos)
# estudia = generar_estudia(alumnos, carreras)
# dicta = generar_dicta(profesores, materias)
# print(generar_cursada(alumnos, materias))

print(generar_periodos_academicos(2))

# alumnos.to_csv('data/alumnos.csv', index=False)
# materias.to_csv('data/materias.csv', index=False)
# estudia.to_csv('data/estudia.csv', index=False)
# dicta.to_csv('data/dicta.csv', index=False)
# departamentos.to_csv('data/departamentos.csv', index=False)
# tipo_becas.to_csv('data/tipo_becas.csv', index=False)
# carreras.to_csv('data/carreras.csv', index=False)
# plan_estudio.to_csv('data/plan_estudio.csv', index=False)
# profesores.to_csv('data/profesores.csv', index=False)
