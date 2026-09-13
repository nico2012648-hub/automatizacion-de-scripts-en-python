import os
import shutil
import datetime
import getpass
import requests

# Obtener usuario de forma segura
try:
    usuario = getpass.getuser().capitalize()
except Exception:
    usuario = os.environ.get('USER', 'Usuario').capitalize()

hora_actual = datetime.datetime.now().strftime("%H:%M")
fecha_actual = datetime.datetime.now().strftime("%d/%m/%Y")

# Obtener uso de disco en la raíz /
total, used, free = shutil.disk_usage("/")
disco_libre_gb = round(free / (1024 ** 3), 1)
disco_usado_pct = round((used / total) * 100, 1)

# Obtener clima en tiempo real
try:
    # Consulta la ubicación aproximada por IP de forma rápida (timeout corto para no congelar la terminal)
    respuesta = requests.get("https://wttr.in/?format=%C+%t", timeout=2)
    if respuesta.status_code == 200:
        clima_info = respuesta.text.strip()
    else:
        clima_info = "No disponible"
except Exception:
    clima_info = "Sin conexión"

# Mensaje de bienvenida
print(f"\033[1;34m==================================================\033[0m")
print(f"\033[1;32m¡Hola de nuevo, {usuario}! 👋\033[0m")
print(f"\033[1;33mHora:\033[0m {hora_actual} | \033[1;33mFecha:\033[0m {fecha_actual}")
print(f"\033[1;36mDisco Disponible:\033[0m {disco_libre_gb} GB libres ({disco_usado_pct}% en uso)")
print(f"\033[1;31mClima actual:\033[0m {clima_info} 🌤️")
print(f"\033[1;35mRecordatorio:\033[0m ¡A darle al estudio de Python hoy! 🐍")
print(f"\033[1;34m==================================================\033[0m\n")
