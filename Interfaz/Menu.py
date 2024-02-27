import json
import os
import sys
import subprocess

if len(sys.argv) > 1:
    correo_user = sys.argv[1]

with open("./Usuarios/users.json", "r") as f:
    js = json.load(f)

username = js[correo_user]["Username"]
tag = js[correo_user]["TAG"]
dinero = js[correo_user]["Dinero"]
wins_RPS = js[correo_user]["Partidas"]["RPS"]["Wins"]
partidas_RPS = js[correo_user]["Partidas"]["RPS"]["Partidas Totales"]
dinero_RPS = js[correo_user]["Partidas"]["RPS"]["Dinero Invertido"]
wins_tragaperras = js[correo_user]["Partidas"]["Tragaperras"]["Wins"]
partidas_tragaperras = js[correo_user]["Partidas"]["Tragaperras"]["Partidas Totales"]
dinero_tragaperras = js[correo_user]["Partidas"]["Tragaperras"]["Dinero Invertido"]
dinero_ruleta = js[correo_user]["Partidas"]["Ruleta"]["Dinero Invertido"]
dinero_total = dinero_tragaperras + dinero_ruleta + dinero_RPS

os.system("cls")

print(f"Bienvenido {username}\n\n")

def eleccion():
    opcion = input("Este es el menú del casino, tienes distintos juegos y opciones.\nSalir    [0]\tCambiar de cuenta[1]\tPerfil[2]\nRPS      [3]\tTragaperras      [4]\tRuleta[5]\nBlackJack[6]\n-> ")
    while opcion not in ["0","1","2","3","4","5","6"]:
        os.system("cls")
        opcion = input("Este es el menú del casino, tienes distintos juegos y opciones.\nSalir    [0]\tCambiar de cuenta[1]\tPerfil[2]\nRPS      [3]\tTragaperras      [4]\tRuleta[5]\nBlackJack[6]\n-> ")
    if opcion == "0":
        print("Gracias por visitar nuestro casino")
        quit()
    elif opcion == "1":
        ruta = os.path.join("index.py")
        subprocess.run(["python", ruta])
    elif opcion == "2":
        print(
            f"\n\nCódigo de usuario: {tag}.\nCorreo electrónico: {correo_user}\n"
            f"Username: {username}\nDinero disponible: {dinero}€\n\n"
            "JUEGOS:\n\n"
            f"RPS:\n-Partidas: {wins_RPS}/{partidas_RPS}\n-Dinero invertido: {dinero_RPS}€\n\n"
            f"Tragaperras:\n-Partidas: {wins_tragaperras}/{partidas_tragaperras}\n"
            f"-Dinero invertido: {dinero_tragaperras}€\n\n"
            f"Ruleta:\n-Dinero invertido: {dinero_ruleta}€\n\n"
            f"DINERO TOTAL GASTADO: {dinero_total}€\n\n\n"
        )
        eleccion()
    elif opcion == "3":
        iniciar_RPS(correo_user)
    elif opcion == "4":
        iniciar_tragaperras(correo_user)
    elif opcion == "5":
       iniciar_Ruleta(correo_user)
    elif opcion == "6":
        iniciar_blackjack(correo_user)

def iniciar_tragaperras(correo_user):
    os.system("cls")
    ruta = os.path.join("Juegos", "Tragaperras.py")
    subprocess.run(["python", ruta, correo_user])

def iniciar_RPS(correo_user):
    os.system("cls")
    ruta = os.path.join("Juegos", "RPS.py")
    subprocess.run(["python", ruta, correo_user])

def iniciar_Ruleta(correo_user):
    os.system("cls")
    ruta = os.path.join("Juegos", "Ruleta.py")
    subprocess.run(["python", ruta, correo_user])

def iniciar_blackjack(correo_user):
    os.system("cls")
    ruta = os.path.join("Juegos","test", "blackjack_test.py")
    subprocess.run(["python", ruta, correo_user])

eleccion()
