import pandas as pd
import matplotlib.pyplot as plt


data = {
    'id': list(range(1, 21)),
    'materia': ['Matemáticas', 'Historia', 'Ciencias', 'Lenguaje'] * 5,
    'nota': [80, 65, 90, 75, 95, 70, 85, 60, 78, 82, 93, 68, 73, 88, 77, 50, 92, 63, 85, 79],
    'aprobado': ['Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'No', 'Sí', 'Sí']
}

df = pd.DataFrame(data)

plt.figure(figsize=(12, 8))
plt.boxplot([df[df['materia'] == materia]['nota'] for materia in df['materia'].unique()], labels=df['materia'].unique())
plt.title('Distribución de Notas por Materia')
plt.xlabel('Materia')
plt.ylabel('Notas')
plt.grid(True)

plt.show()

aprobados = df[df['aprobado'] == 'Sí'].shape[0]
no_aprobados = df[df['aprobado'] == 'No'].shape[0]
total_estudiantes = df.shape[0]

labels = ['Aprobados', 'No Aprobados']
sizes = [aprobados, no_aprobados]
colors = ['orange', 'blue']


plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
plt.title('Proporción de Estudiantes Aprobados y No Aprobados')
plt.show()