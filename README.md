# TimecodeUnreal ⏱️

Este es un script sencillo de Python que transforma una secuencia de imágenes .png generadas por Unreal Engine en un archivo de video .mov con timecode. Además, exporta un archivo .csv que puede ser importado como metadatos en DaVinci Resolve.

## ¿Cómo funciona? ❔

El script utiliza la biblioteca `subprocess` para ejecutar FFmpeg y crear un video con los datos de timecode de Unreal a partir de una serie de imágenes.

Además, el script también escribe en un archivo CSV los datos relevantes de cada escena y toma. Este archivo CSV puede ser importado en DaVinci Resolve para agregar los metadatos a las escenas.

## Requisitos 💻

- Python 3.6 o superior
- FFmpeg instalado y accesible desde la línea de comandos

## Uso ℹ️

1. Renderizar las imágenes en Unreal Engine con las configuraciones de la carpeta [ExportConfig Unreal](https://github.com/PGSCOM/TimecodeUnreal/blob/main/ExportConfig%20Unreal) editando la ruta de salida.
2. Editar la variable directorio_raiz a la ruta de la carpeta donde se encuentran las imágenes y la variable fps.
3. Ejecuta el script.

## Nota ⚠️

Este script está diseñado para funcionar en Windows, por lo que los comandos pueden necesitar ser modificados para otros sistemas operativos.
