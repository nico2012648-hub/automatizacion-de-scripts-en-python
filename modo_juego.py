import subprocess
import time
import sys

print("\033[1;35m=== ACTIVANDO MODO JUEGO (GAME MODE) ===\033[0m")

# 1. Desactivar el compositor visual de XFCE para reducir lag e impacto gráfico
print("\033[1;33m[1/4] Desactivando efectos visuales del escritorio...\033[0m")
try:
    subprocess.run(["xfconf-query", "-c", "xfwm4", "-p", "/general/use_compositing", "-s", "false"])
    print("\033[1;32m[✓] Compositor desactivado (gráficos enfocados en el juego).\033[0m")
except Exception:
    pass

# 2. Cerrar navegadores o apps que consumen mucha RAM
print("\033[1;33m[2/4] Liberando memoria RAM de navegadores...\033[0m")
subprocess.run(["killall", "-q", "brave", "chrome", "firefox"])
print("\033[1;32m[✓] Procesos de fondo cerrados.\033[0m")

# 3. Limpiar memoria RAM acumulada
print("\033[1;33m[3/4] Liberando memoria RAM disponible...\033[0m")
subprocess.run(["sync"])
print("\033[1;32m[✓] RAM optimizada.\033[0m")

# 4. Iniciar Steam
print("\033[1;33m[4/4] Lanzando Steam...\033[0m")
try:
    # Lanza Steam asignándole alta prioridad de proceso (-10)
    subprocess.Popen(["nice", "-n", "-10", "steam"])
    print("\033[1;32m[✓] Steam iniciado con prioridad de CPU alta.\033[0m")
except Exception:
    print("\033[1;31m[!] No se encontró el comando 'steam'. Verfica la instalación.\033[0m")

print("\033[1;36m\n=== ¡MODO JUEGO LISTO! A DISFRUTAR 🎮🔥 ===\033[0m")
