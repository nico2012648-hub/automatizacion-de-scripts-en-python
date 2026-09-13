import subprocess

print("\033[1;36m=== RESTAURANDO MODO ESCRITORIO NORMAL ===\033[0m")

# 1. Reactivar el compositor visual de XFCE
try:
    subprocess.run(["xfconf-query", "-c", "xfwm4", "-p", "/general/use_compositing", "-s", "true"])
    print("\033[1;32m[✓] Compositor visual reactivado (efectos y transparencias restaurados).\033[0m")
except Exception as e:
    print(f"\033[1;31m[!] Error al reactivar el compositor: {e}\033[0m")

# 2. Notificación visual
try:
    subprocess.run(["notify-send", "-u", "normal", "-i", "display", "Modo Juego Finalizado", "Escritorio restaurado al estado normal."])
except Exception:
    pass

print("\033[1;35m=== ESCRITORIO LISTO Y RESTAURADO 💻✨ ===\033[0m")
