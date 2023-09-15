import os

# Directorio raíz donde se encuentran las carpetas con las secuencias de PNG
directorio_raiz = "D:/Videojuegos/EpicGames/UnrealMultiguerras/Saved/MovieRenders"

# Velocidad de cuadro (FPS)
fps = 24

# Función para calcular el tiempo en segundos para una imagen dada
def calcular_tiempo(frame, fps):
    return frame / fps

# Diccionario para almacenar los tiempos de inicio para cada escena
tiempos_de_inicio = {}

# Recorre todas las carpetas en el directorio raíz
for carpeta in os.listdir(directorio_raiz):
    carpeta_path = os.path.join(directorio_raiz, carpeta)
    
    # Verifica si la carpeta contiene archivos PNG
    if os.path.isdir(carpeta_path):
        for archivo in os.listdir(carpeta_path):
            if archivo.endswith(".png"):
                nombre_archivo = os.path.splitext(archivo)[0]
                nombre_escena, numero_frame = nombre_archivo.split(".")
                numero_frame = int(numero_frame)
                tiempo_segundos = calcular_tiempo(numero_frame, fps)
                
                # Almacena el tiempo de inicio en el diccionario
                if nombre_escena in tiempos_de_inicio:
                    tiempos_de_inicio[nombre_escena].append(tiempo_segundos)
                else:
                    tiempos_de_inicio[nombre_escena] = [tiempo_segundos]

# Imprime los tiempos de inicio para cada escena
for escena, tiempos in tiempos_de_inicio.items():
    print(f"Escena: {escena}")
    for tiempo in tiempos:
        print(f"  Tiempo de inicio (segundos): {tiempo}")
