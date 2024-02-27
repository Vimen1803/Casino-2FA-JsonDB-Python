import json
import sys
import subprocess
import random
import os
from colorama import Fore

if len(sys.argv) > 1:
    correo_user = sys.argv[1]

opciones = ["A", "B", "C", "D", "V"]
peso = [1.25, 1.25, 1.25, 1.25, 1]
print(Fore.WHITE + "")

def coger_datos(correo_user):
    global js
    with open("./Usuarios/users.json", "r") as f:
        js = json.load(f)
        global dinero_total, dinero_Tragaperras,partidas_Tragaperras,wins_Tragaperras,username,password,tag,wins_RPS,partidas_RPS,dinero_RPS,dinero_ruleta,fecha
        tag = js[correo_user]["TAG"]
        username = js[correo_user]["Username"]
        password = js[correo_user]["Password"]
        dinero_total = js[correo_user]["Dinero"]
        wins_RPS = js[correo_user]["Partidas"]["RPS"]["Wins"]
        partidas_RPS = js[correo_user]["Partidas"]["RPS"]["Partidas Totales"]
        dinero_RPS = js[correo_user]["Partidas"]["RPS"]["Dinero Invertido"]
        dinero_Tragaperras = js[correo_user]["Partidas"]["Tragaperras"]["Dinero Invertido"]
        partidas_Tragaperras = js[correo_user]["Partidas"]["Tragaperras"]["Partidas Totales"]
        wins_Tragaperras = js[correo_user]["Partidas"]["Tragaperras"]["Wins"]
        dinero_ruleta = js[correo_user]["Partidas"]["Ruleta"]["Dinero Invertido"]
        fecha = js[correo_user]["Fecha de creacion"]
        calcular_apuesta()     

def calcular_apuesta():
    global apuesta
    apuesta = round(float(input(f"\nTienes {dinero_total}€, ¿cuanto dinero deseas apostar? --> ")),2)
    while apuesta > dinero_total or apuesta <= 0:
        apuesta = round(float(input(f"\n\nTienes {dinero_total}€, ¿cuanto dinero deseas apostar? --> ")),2)
    if apuesta <= dinero_total:
        combinacion()

def combinacion():
    global combinacion1, combinacion2, combinacion3, premio, premio2, premio3, premio4, recompensa
    combinacion1, combinacion2, combinacion3 = random.choices(opciones, weights=peso, k=3)
    premio, premio2, premio3, premio4 = False, False, False, False
    if combinacion1 == combinacion2 == combinacion3:
        premio = True
        if combinacion1 == "V":
            premio2 = True
            premio = False
    elif combinacion1 == combinacion2 != combinacion3:
        if combinacion3 == "V":
            premio3 = True
        elif combinacion1 == "V":
            premio4 = True
    elif combinacion1 == combinacion3 != combinacion2:
        if combinacion2 == "V":
            premio3 = True
        elif combinacion1 == "V":
            premio4 = True
    elif combinacion3 == combinacion2 != combinacion1:
        if combinacion1 == "V":
            premio3 = True
        elif combinacion2 == "V":
            premio4 = True

    print(f"\nLa combinacion ha sido: {combinacion1}|{combinacion2}|{combinacion3}")
    if premio == True:
        recompensa = apuesta * 10
        print(f"Has ganado {recompensa}€")
    elif premio2 == True:
            recompensa = apuesta * 20
            print(f"Has ganado {recompensa}€")
    elif premio3 == True:
        recompensa = apuesta * 2
        print(f"Has ganado {recompensa}€")
    elif premio4 == True:
        recompensa = apuesta * 5
        print(f"Has ganado {recompensa}€")
    else:
        recompensa = 0
        print("Has perdido!")

    dar_premio()

def dar_premio():
    global dinero_total, dinero_Tragaperras, partidas_Tragaperras, wins_Tragaperras
    ganancia = recompensa - apuesta
    dinero_total += ganancia
    dinero_Tragaperras += apuesta
    partidas_Tragaperras += 1
    if premio == True or premio2 == True or premio3 == True or premio4 == True:
        wins_Tragaperras += 1
    else:
        wins_Tragaperras += 0

    guardar_datos(dinero_total, dinero_Tragaperras, partidas_Tragaperras, wins_Tragaperras)

def guardar_datos(dinero_total, dinero_Tragaperras, partidas_Tragaperras, wins_Tragaperras): 
    with open("./Usuarios/users.json", "w", encoding="UTF8") as f:
        js[correo_user] = { }
        js[correo_user]["TAG"] = tag
        js[correo_user]["Username"] = username
        js[correo_user]["Password"] = password
        js[correo_user]["Dinero"] = (dinero_total)
        js[correo_user]["Partidas"] = {"RPS": {"Wins": wins_RPS, "Partidas Totales": partidas_RPS, "Dinero Invertido": dinero_RPS}, "Tragaperras": {"Wins": wins_Tragaperras, "Partidas Totales": partidas_Tragaperras, "Dinero Invertido": dinero_Tragaperras}, "Ruleta": {"Dinero Invertido": dinero_ruleta}}
        js[correo_user]["Fecha de creacion"] = fecha
        user = json.dump(js, f, indent= 6)
        f.flush()
    pregunta_final()

def pregunta_final():
    respuesta = int(input(f"\nTienes {dinero_total}€.\nSi deseas salir pulse 0.\nSi deseas cambiar la apuesta pulse 1.\nSi deseas continuar con la misma apuesta pulse 2.\nSi deseas volver al menu pulse 3\n\n"))
    if respuesta == 1:
        coger_datos(correo_user)
    elif respuesta == 2:
        if apuesta <= dinero_total:
            combinacion()
        else:
            print("\nNo te queda tanto dinero")
            pregunta_final()
    elif respuesta == 3:
        ruta = os.path.join("Interfaz", "Menu.py")
        subprocess.run(["python", ruta, correo_user])
    else:
        quit()

coger_datos(correo_user)