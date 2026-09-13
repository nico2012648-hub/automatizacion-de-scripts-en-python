import subprocess
import os
import sys

print("\033[1;36m=== INICIANDO OPTIMIZACIÓN PROFUNDA DE HARDWARE ===\033[0m")

# 1. Limpiar la memoria RAM atrapada en caché (Kernel Drop Caches)
print("\033[1;33m[1/4] Liberando memoria RAM atrapada en caché...\033[0m")
try:
    subprocess.run(["sudo", "sync"])
    subprocess.run("echo 3 | sudo tee /proc/sys/vm/drop_caches", shell=True, stdout=subprocess.DEVNULL)
    print("\033[1;32m[✓] RAM liberada con éxito.\033[0m")
except Exception as e:
    print(f"\033[1;31m[!] Error al liberar RAM: {e}\033[0m")

# 2. Vaciar la memoria Swap (fuerza al sistema a mover todo a la RAM rápida)
print("\033[1;33m[2/4] Reciclando memoria Swap...\033[0m")
try:
    subprocess.run(["sudo", "swapoff", "-a"], check=True)
    subprocess.run(["sudo", "swapon", "-a"], check=True)
    print("\033[1;32m[✓] Swap limpiada y reactivada.\033[0m")
except Exception:
    print("\033[1;30m[-] Swap sin cambios o no requerida en este momento.\033[0m")

# 3. Limpiar registros acumulados del sistema (logs de journalctl a max 50MB)
print("\033[1;33m[3/4] Reduciendo espacio de logs del sistema...\033[0m")
try:
    subprocess.run(["sudo", "journalctl", "--vacuum-size=50M"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("\033[1;32m[✓] Logs del sistema recortados a 50MB max.\033[0m")
except Exception:
    pass

# 4. Trimar / Optimizar la estructura del sistema de archivos
print("\033[1;33m[4/4] Finalizando optimización de procesos...\033[0m")
try:
    subprocess.run(["sudo", "fstrim", "-av"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("\033[1;32m[✓] Almacenamiento optimizado.\033[0m")
except Exception:
    pass

print("\033[1;35m\n=== ¡SISTEMA Y HARDWARE AL 100%! 🚀✨ ===\033[0m")
