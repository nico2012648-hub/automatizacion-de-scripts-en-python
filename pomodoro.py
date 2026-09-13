import time
import subprocess
import sys

TIEMPO_ESTUDIO = 45
TIEMPO_DESCANSO = 10

def notificar(titulo, mensaje):
    try:
        subprocess.run(["notify-send", "-u", "normal", "-i", "dialog-information", titulo, mensaje])
    except Exception:
        pass

def cuenta_regresiva(minutos, etiqueta):
    segundos_totales = minutos * 60
    while segundos_totales > 0:
        mins, segs = divmod(segundos_totales, 60)
        formato_tiempo = f"{mins:02d}:{segs:02d}"
        print(f"\r\033[1;36m[{etiqueta}]\033[0m Tiempo restante: \033[1;33m{formato_tiempo}\033[0m ", end="")
        sys.stdout.flush()
        time.sleep(1)
        segundos_totales -= 1
    print()

try:
    print("\033[1;35m=== TEMPORIZADOR POMODORO PARA PYTHON ===\033[0m")
    print("\033[1;90m(Presiona Ctrl + C en cualquier momento para cancelar)\033[0m\n")
    
    notificar("Pomodoro Iniciado", f"¡A programar! Tienes {TIEMPO_ESTUDIO} minutos de enfoque total.")
    
    cuenta_regresiva(TIEMPO_ESTUDIO, "CÓDIGO CONCENTRADO")
    notificar("¡Pausa Activa!", f"¡Hora de descansar! Tómate {TIEMPO_DESCANSO} minutos lejos de la pantalla.")
    
    print("\n\033[1;32m¡Gran bloque de trabajo! Entrando a tiempo de descanso...\033[0m")
    cuenta_regresiva(TIEMPO_DESCANSO, "PAUSA ACTIVA")
    
    notificar("Descanso finalizado", "¡Tiempo de descanso terminado!")
    print("\n\033[1;32m=== ¡BLOQUE COMPLETADO CON ÉXITO! 🐍✨ ===\033[0m")

except KeyboardInterrupt:
    print("\n\n\033[1;31m[!] Temporizador cancelado. ¡Nos vemos en la próxima sesión! 👋\033[0m")
    sys.exit(0)
