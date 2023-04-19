import os
import csv
import random
import string

modalidades = ["100m lisos", "200m lisos", "400m lisos", "800m lisos", "1500m lisos", "110m vallas",
               "400m vallas", "3000m obstáculos", "4x100m relevo", "4x400m relevo"]  # Lista de modalidades

for i in range(50):
    # Generar nombre aleatorio del corredor
    nombre_corredor = ''.join(random.choices(string.ascii_uppercase, k=5))
    # Generar metros corridos aleatorios
    metros_corridos = random.choice(
        [100, 200, 400, 800, 1500, 110, 400, 3000, 4*100, 4*400])
    # Generar modalidad aleatoria
    modalidad = random.choice(modalidades)
    # Generar título del archivo
    titulo_archivo = f"{nombre_corredor} - {metros_corridos}m - {modalidad}"
    # Generar nombre del archivo
    nombre_archivo = f"{titulo_archivo}.csv"
    # Generar tiempos aleatorios
    tiempos = []
    for j in range(6):
        minutos = random.randint(0, 1)
        segundos = random.randint(0, 59)
        centesimas = random.randint(0, 99)
        tiempo = f"{minutos:02}:{segundos:02}.{centesimas:02}"
        tiempos.append(tiempo)
    # Escribir archivo CSV
    with open(nombre_archivo, "w", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(["Carrera", "Tiempo"])
        for j, tiempo in enumerate(tiempos):
            carrera = f"Carrera {j+1}"
            writer.writerow([carrera, tiempo])


if not os.path.exists("registros"):
    os.makedirs("registros")
nombre_archivo = f"registros/{titulo_archivo}.csv"
