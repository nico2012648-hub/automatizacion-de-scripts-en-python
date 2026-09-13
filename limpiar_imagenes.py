import os
import time
from send2trash import send2trash

CARPETA = os.path.expanduser('~/Imágenes')
DIAS_MAXIMOS = 14
EXTENSIONES = ['.jpg', '.jpeg', '.png', '.gif', '.webp']

ahora = time.time()
limite_segundos = DIAS_MAXIMOS * 86400

if os.path.exists(CARPETA):
    for archivo in os.listdir(CARPETA):
        ruta_completa = os.path.join(CARPETA, archivo)
        
        if os.path.isfile(ruta_completa):
            _, extension = os.path.splitext(archivo)
            
            if extension.lower() in EXTENSIONES:
                fecha_modificacion = os.path.getmtime(ruta_completa)
                antiguedad = ahora - fecha_modificacion
                
                if antiguedad > limite_segundos:
                    send2trash(ruta_completa)
                    print(f"Enviado a la papelera: {archivo}")
