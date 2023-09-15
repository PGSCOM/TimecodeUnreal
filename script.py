import os

# Directorio raíz donde se encuentran las carpetas con las secuencias de jpeg
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
    carpeta_path = directorio_raiz + '/' + carpeta + '/'
    
    # Verifica si la carpeta contiene archivos jpeg
    if os.path.isdir(carpeta_path):
        archivos_jpeg = [archivo for archivo in os.listdir(carpeta_path) if archivo.endswith(".jpeg")]
        
        # Ordena los archivos jpeg alfabéticamente
        archivos_jpeg.sort()
        
        # Verifica si hay al menos un archivo jpeg en la carpeta
        if archivos_jpeg:
            primer_archivo = archivos_jpeg[0]
            nombre_archivo = os.path.splitext(primer_archivo)[0]
            nombre_escena, numero_frame = nombre_archivo.split(".")
            numero_frame = int(numero_frame)
            tiempo_segundos = calcular_tiempo(numero_frame, fps)
            hhmmss = formato_segundos(tiempo_segundos)
            
            # Imprime el tiempo de inicio para el primer frame de la carpeta
            print(f"Carpeta: {carpeta}")
            print(f"  Tiempo de inicio (segundos): {tiempo_segundos}")
            print(hhmmss)


            # Convertir a .mov con ffmpeg

            import subprocess
            import os

            # Directorio de las imágenes jpeg
            input_directory = carpeta_path

            # Nombre del archivo de salida
            output_file = directorio_raiz + "/" + f"{nombre_escena}.mov"

            # Timecode en formato HH:MM:SS:FF (horas, minutos, segundos, fotogramas)
            timecode = hhmmss  # Por ejemplo, comenzar en 0 horas, 0 minutos, 0 segundos y 0 fotogramas

            # Obtener la lista de archivos en el directorio de entrada
            image_files = sorted([f for f in os.listdir(input_directory) if f.endswith(".jpeg")])

            # Construir una lista de argumentos para FFmpeg
            ffmpeg_args = [
                "ffmpeg",
                "-framerate", "24",  # Tasa de fotogramas de salida (ajusta según sea necesario)
                "-start_number", str(numero_frame),  # Número de inicio para los nombres de archivo
                "-i", input_directory + f"{nombre_escena}.%07d.jpeg",  # Patrón de nombres de archivo
                "-c:v", "libx264",
                "-pix_fmt", "yuv420p",
                "-crf", "18",  # Calidad de compresión (ajusta según sea necesario)
                "-timecode", timecode,
                output_file
            ]

            # Ejecutar el comando FFmpeg para crear el video
            subprocess.run(ffmpeg_args)

            print(f"Video creado con timecode y guardado como '{output_file}'.")
            print(ni)