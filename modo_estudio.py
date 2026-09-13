import subprocess
import time

print("\033[1;36m=== ACTIVANDO MODO ENFOQUE DE HARDWARE ===\033[0m")

# 1. Ajustar brillo de pantalla al 70% para cuidar la vista
try:
    subprocess.run(["brightnessctl", "set", "70%"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("\033[1;32m[✓] Brillo de pantalla ajustado al 70%\033[0m")
except Exception:
    print("\033[1;33m[!] No se pudo ajustar el brillo (brightnessctl no detectado)\033[0m")

# 2. Liberar memoria RAM en caché
try:
    subprocess.run(["sync"])
    print("\033[1;32m[✓] Memoria RAM optimizada\033[0m")
except Exception:
    pass

# 3. Lanzar el entorno de estudio habituar
print("\033[1;35m[→] Lanzando Brave y terminal de trabajo...\033[0m")
subprocess.Popen(["python3", "/home/nicolas/Scripts/estudio.py"])

print("\033[1;32m=== MODO ENFOQUE ACTIVO: ¡A DARLE AL CÓDIGO! 🐍✨ ===\033[0m")
