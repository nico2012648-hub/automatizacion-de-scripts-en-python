import os
import shutil

PAPELERA_FILES = os.path.expanduser('~/.local/share/Trash/files')
PAPELERA_INFO = os.path.expanduser('~/.local/share/Trash/info')

def vaciar_carpeta(ruta):
    if os.path.exists(ruta):
        for elemento in os.listdir(ruta):
            ruta_elemento = os.path.join(ruta, elemento)
            try:
                if os.path.isfile(ruta_elemento) or os.path.islink(ruta_elemento):
                    os.remove(ruta_elemento)
                elif os.path.isdir(ruta_elemento):
                    shutil.rmtree(ruta_elemento)
            except Exception as e:
                pass

vaciar_carpeta(PAPELERA_FILES)
vaciar_carpeta(PAPELERA_INFO)
print("Papelera vaciada con éxito.")
