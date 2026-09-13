import os
import shutil

CACHE_DIR = os.path.expanduser('~/.cache')

def limpiar_cache():
    bytes_liberados = 0
    if os.path.exists(CACHE_DIR):
        for elemento in os.listdir(CACHE_DIR):
            ruta = os.path.join(CACHE_DIR, elemento)
            try:
                if os.path.isfile(ruta) or os.path.islink(ruta):
                    bytes_liberados += os.path.getsize(ruta)
                    os.remove(ruta)
                elif os.path.isdir(ruta):
                    for root, dirs, files in os.walk(ruta):
                        bytes_liberados += sum(os.path.getsize(os.path.join(root, name)) for name in files)
                    shutil.rmtree(ruta)
            except Exception:
                pass
        
        mb_liberados = round(bytes_liberados / (1024 * 1024), 2)
        print(f"Caché limpiada con éxito. Se liberaron aprox. {mb_liberados} MB.")

limpiar_cache()
