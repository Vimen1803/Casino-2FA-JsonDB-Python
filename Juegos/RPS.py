import random
import json
import sys
import subprocess
import os
from colorama import Fore

if len(sys.argv) > 1:
    correo_user = sys.argv[1]

opciones = ["Piedra", "Papel", "Tijera"]
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
        eleccion_player()

def eleccion_player():
    global apuesta, eleccion_persona
    apuesta = round(float(input(f"\nTienes {dinero_total}€, ¿cuanto dinero deseas apostar? --> ")),2)
    while apuesta > dinero_total:
        apuesta = round(float(input(f"Tienes {dinero_total}€, ¿cuanto dinero deseas apostar? --> ")),2)
    eleccion_persona = int(input("\n\nSi quieres jugar piedra pulse 1.\nSi quieres jugar papel pulse 2.\nSi quieres jugar tijera pulse 3.\n\n"))
    while eleccion_persona != 1 and eleccion_persona != 2 and eleccion_persona != 3:
        eleccion_persona = int(input("\n\nEleccion no valida.\nSi quieres jugar piedra pulse 1.\nSi quieres jugar papel pulse 2.\nSi quieres jugar tijera pulse 3.\n\n"))
    eleccion_bot(eleccion_persona)

def eleccion_bot(eleccion_persona):
    global eleccion_npc, resultado
    eleccion_npc = random.choice(opciones)

    if eleccion_npc == "Piedra":
        if eleccion_persona == 1:
            resultado = "empate"
            print(f"\nHe sacado {eleccion_npc}, empate!\n")
        elif eleccion_persona == 2:
            resultado = "win"
            print(f"\nHe sacado {eleccion_npc}, has ganado!\n")
        else:
            resultado = "derrota"
            print(f"\nHe sacado {eleccion_npc}, has perdido!\n")

    elif eleccion_npc == "Papel":
        if eleccion_persona == 1:
            resultado = "derrota"
            print(f"\nHe sacado {eleccion_npc}, has perdido!\n")
        elif eleccion_persona == 2:
            resultado = "empate"
            print(f"\nHe sacado {eleccion_npc}, empate!\n")
        else:
            resultado = "win"
            print(f"\nHe sacado {eleccion_npc}, has ganado!\n")

    elif eleccion_npc == "Tijera":
        if eleccion_persona == 1:
            resultado = "win"
            print(f"\nHe sacado {eleccion_npc}, has ganado!\n")
        elif eleccion_persona == 2:
            resultado = "derrota"
            print(f"\nHe sacado {eleccion_npc}, has perdido!\n")
        else:
            resultado = "empate"
            print(f"\nHe sacado {eleccion_npc}, empate!\n")
    
    calcular_premio()

def calcular_premio():
    global premio
    if resultado == "win":
        premio = apuesta * 2
    elif resultado == "empate":
        premio = apuesta
    else:
        premio = 0
    
    dar_premio()

def dar_premio():
    global dinero_total,dinero_RPS,partidas_RPS,wins_RPS
    ganancia = premio - apuesta
    dinero_total += ganancia
    dinero_RPS += apuesta
    partidas_RPS += 1
    if resultado == "win":
        wins_RPS += 1
        print(f"Has ganado {premio}€\n")
    guardar_datos(dinero_total,dinero_RPS,partidas_RPS,wins_RPS)

def guardar_datos(dinero_total,dinero_RPS,partidas_RPS,wins_RPS):  
    with open("./Usuarios/users.json", "w", encoding="UTF8") as f:
        js[correo_user] = { }
        js[correo_user]["TAG"] = tag
        js[correo_user]["Username"] = username
        js[correo_user]["Password"] = password
        js[correo_user]["Dinero"] = dinero_total
        js[correo_user]["Partidas"] = {"RPS": {"Wins": wins_RPS, "Partidas Totales": partidas_RPS, "Dinero Invertido": dinero_RPS}, "Tragaperras": {"Wins": wins_Tragaperras, "Partidas Totales": partidas_Tragaperras, "Dinero Invertido": dinero_Tragaperras}, "Ruleta": {"Dinero Invertido": dinero_ruleta}}
        js[correo_user]["Fecha de creacion"] = fecha
        user = json.dump(js, f, indent= 6)
        f.flush()
    pregunta_final()

def pregunta_final():
    respuesta = int(input(f"Tienes {dinero_total}€.\nSi deseas salir pulse 0.\nSi deseas cambiar la apuesta pulse 1.\nSi deseas continuar con la misma apuesta pulse 2.\nSi deseas volver al menu pulse 3\n\n"))
    if respuesta == 1:
        coger_datos(correo_user)
    elif respuesta == 2:
        if apuesta <= dinero_total:
            eleccion_bot(eleccion_persona)
        else:
            print("\nNo te queda tanto dinero")
            pregunta_final()
    elif respuesta == 3:
        ruta = os.path.join("Interfaz", "Menu.py")
        subprocess.run(["python", ruta, correo_user])
    else:
        quit()

coger_datos(correo_user)