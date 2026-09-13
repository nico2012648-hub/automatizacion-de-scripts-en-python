import os
import shutil
import time

ORIGEN_ESCRITORIO = os.path.expanduser('~/Escritorio')
ORIGEN_IMAGENES = os.path.expanduser('~/Imágenes')
DESTINO_BASE = os.path.expanduser('~/Imágenes/Capturas')

def organizar_capturas():
    # Buscar en Escritorio e Imágenes
    for origen in [ORIGEN_ESCRITORIO, ORIGEN_IMAGENES]:
        if not os.path.exists(origen):
            continue
            
        for archivo in os.listdir(origen):
            # Filtra archivos que empiecen por 'Captura' o 'Screenshot'
            if archivo.lower().startswith(('captura', 'screenshot')) and archivo.endswith(('.png', '.jpg', '.jpeg')):
                ruta_original = os.path.join(origen, archivo)
                
                # Obtener la fecha de modificación del archivo
                mtime = os.path.getmtime(ruta_original)
                fecha = time.localtime(mtime)
                
                ano = time.strftime('%Y', fecha)
                mes = time.strftime('%m-%B', fecha)
                
                # Crear estructura de carpetas: ~/Imágenes/Capturas/2026/08-August/
                carpeta_destino = os.path.join(DESTINO_BASE, ano, mes)
                os.makedirs(carpeta_destino, exist_ok=True)
                
                ruta_final = os.path.join(carpeta_destino, archivo)
                shutil.move(ruta_original, ruta_final)
                print(f"Captura movida: {archivo} -> {carpeta_destino}")

organizar_capturas()
