import os
import shutil

# Ruta de la carpeta Descargas
descargas_dir = os.path.expanduser('~/Descargas')

# Reglas: Carpetas destino y sus extensiones
carpetas = {
    'Imágenes': ['.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp'],
    'Documentos': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Instaladores': ['.deb', '.AppImage', '.tar.gz', '.zip', '.rar'],
    'Videos': ['.mp4', '.mkv', '.avi']
}

for archivo in os.listdir(descargas_dir):
    ruta_archivo = os.path.join(descargas_dir, archivo)
    
    # Solo procesamos archivos, no carpetas que ya existan
    if os.path.isfile(ruta_archivo):
        nombre, extension = os.path.splitext(archivo)
        
        for carpeta, extensiones in carpetas.items():
            if extension.lower() in extensiones:
                destino_dir = os.path.join(os.path.expanduser('~'), carpeta)
                os.makedirs(destino_dir, exist_ok=True)
                shutil.move(ruta_archivo, os.path.join(destino_dir, archivo))
                print(f"Movido: {archivo} -> {carpeta}")
                break
