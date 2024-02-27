import os
import subprocess
from colorama import Fore

eleccion = ""

os.system("cls")

print(Fore.CYAN + "\t\t\t-------------------------------\n\t\t\t BIENVENIDO AL CASINO DE VIMEN\n\t\t\t-------------------------------\n\n")

while eleccion != 1 or eleccion != 0:
    eleccion = int(input("\t\tIniciar sesion[0]\t\tRegistrarse[1]\n-> "))
    if eleccion == 0 or eleccion == 1:
        break

if eleccion == 0:
     ruta = os.path.join("Usuarios", "Inicio_Sesion.py")
     subprocess.run(["python", ruta])

elif eleccion == 1:
    ruta = os.path.join("Usuarios", "Registro.py")
    subprocess.run(["python", ruta])