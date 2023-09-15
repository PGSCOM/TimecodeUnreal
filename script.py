import os

# Directorio raíz donde se encuentran las carpetas con las secuencias de png
directorio_raiz = "D:/Videojuegos/EpicGames/UnrealMultiguerras/Saved/MovieRenders"

# Velocidad de cuadro (FPS)
fps = 24

# Función para calcular el tiempo en segundos para un frame dado
def calcular_tiempo(frame, fps):
    return frame / fps

# Función para aplicar el formato a los segundos
def formato_segundos(segundos):
    horas = int(segundos // 3600)
    segundos_restantes = int(segundos % 3600)
    minutos = int(segundos_restantes // 60)
    segundos = int(segundos_restantes % 60)
    return f"{horas:02d}:{minutos:02d}:{segundos:02d}"


# Recorre todas las carpetas en el directorio raíz
for carpeta in os.listdir(directorio_raiz):
    carpeta_path = os.path.join(directorio_raiz, carpeta)
    
    # Verifica si la carpeta contiene archivos png
    if os.path.isdir(carpeta_path):
        archivos_png = [archivo for archivo in os.listdir(carpeta_path) if archivo.endswith(".png")]
        
        # Ordena los archivos png alfabéticamente
        archivos_png.sort()
        
        # Verifica si hay al menos un archivo png en la carpeta
        if archivos_png:
            primer_archivo = archivos_png[0]
            nombre_archivo = os.path.splitext(primer_archivo)[0]
            nombre_escena, numero_frame = nombre_archivo.split(".")
            numero_frame = int(numero_frame)
            tiempo_segundos = calcular_tiempo(numero_frame, fps)
            hhmmss = formato_segundos(tiempo_segundos)
            
            # Imprime el tiempo de inicio para el primer frame de la carpeta
            print(f"Carpeta: {carpeta}")
            print(f"  Tiempo de inicio (segundos): {tiempo_segundos}")
            print(hhmmss)
