import subprocess
import time

print("\033[1;36m=== INICIANDO ENTORNO DE PROGRAMACIÓN ===\033[0m")

# 1. Abrir Brave directo en Gemini
print("\033[1;33m[1/2] Lanzando Gemini en Brave...\033[0m")
subprocess.Popen(["brave-browser", "--new-window", "https://gemini.google.com"])

time.sleep(1)

# 2. Abrir VSCodium en la carpeta de Python
print("\033[1;33m[2/2] Abriendo VSCodium...\033[0m")
subprocess.Popen(["codium", "/home/nicolas/Documentos/Python"])

print("\033[1;32m=== ¡TODO LISTO PARA TIRAR CÓDIGO! 🐍✨ ===\033[0m")
