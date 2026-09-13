import subprocess

# Lista con el tutorial oficial de Python actualizado
links = [
    "https://gemini.google.com",
    "https://docs.python.org/3/tutorial/index.html",
    "https://www.youtube.com/watch?v=nKPbfIU442g&t=0s"
]

print("\033[1;33mIniciando sesión de estudio con el Tutorial Oficial de Python...\033[0m")

# Lanzar todo junto en una sola instancia de Brave
subprocess.Popen(["flatpak", "run", "com.brave.Browser"] + links)

# Abrir terminal enfocada en tu directorio de trabajo
ruta_estudio = "/home/nicolas/Documentos/Python"
subprocess.run(["mkdir", "-p", ruta_estudio])
subprocess.Popen(["xfce4-terminal", "--working-directory=" + ruta_estudio])

print("\033[1;32m¡Entorno listo con el tutorial cargado! A darle al código. 🐍✨\033[0m")
