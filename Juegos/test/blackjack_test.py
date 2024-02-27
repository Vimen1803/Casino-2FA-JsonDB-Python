import random
import sys
import os
from colorama import Fore
import subprocess

if len(sys.argv) > 1:
    correo_user = sys.argv[1]

baraja = {"As": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}
palos = ["Corazones", "Diamantes", "Treboles", "Picas"]
print(Fore.WHITE + "")

def definir_valores():
    global jugadores, jugadores_plantados, jugadores_eliminados, distancia_21, Manos
    jugadores = []
    jugadores_plantados = []
    jugadores_eliminados = []
    distancia_21 = []
    Manos = {}

def saber_n_jugadores():
    jugadores = 0
    while jugadores < 2 or jugadores > 10:
        jugadores = int(input("Introduce el numero de jugadores (2-10) -> "))
    return jugadores

def saber_nombres_jugadores(numero_jugadores):
    print("\n")
    for i in range(1, numero_jugadores+1):
        jugador = input(f"Introduce el nombre del jugador {i} -> ")
        while jugador in [nombre for _, nombre in jugadores]:
            jugador = input(f"Ese jugador ya existe, introduce el nombre del jugador {i} -> ")
        jugadores.append((f"jugador_{i}", jugador))
    print("\n")
    return jugadores

def pregunta_final():
    respuesta = input("Volver a jugar[y/n]\n-> ")
    while respuesta.lower() not in ["y", "n"]:
        respuesta = input("Volver a jugar[y/n]\n-> ").lower
    if respuesta == "y":
        main()
    else:
        if not correo_user:
            sys.exit()
        else:
            ruta = os.path.join("Interfaz", "Menu.py")
            subprocess.run(["python", ruta, correo_user])

def reparto():
    for jugador in jugadores:
        mano_jugador = []
        for i in range(2):
            carta, i = obtener_carta()
            mano_jugador.append(carta)
        Manos[jugador[1]] = mano_jugador
        print(f"El jugador {jugador[1]} ha obtenido las cartas: {', '.join(mano_jugador)}")
        sacar_valores(jugador)

def sacar_valores(jugador):
    valor_total = 0
    for carta in Manos[jugador[1]]:
        carta = carta.split()
        carta = carta[0]
        carta_valor = baraja[carta]
        valor_total += carta_valor
    for carta in Manos[jugador[1]]:
        carta = carta.split()
        carta = carta[0]
        if carta == "As":
            if valor_total > 21:
                valor_total -= 10
            else:
                pass
    if valor_total == 21:
        print(Fore.CYAN+"\n\t\t  [B L A C K J A C K]\n\t\tEl jugador {jugador[1]} ha ganado.")
        print(Fore.WHITE + "")
        pregunta_final()
    elif valor_total > 21:
        jugadores_eliminados.append(jugador[1])
    return valor_total

def reparto_extra():
    for jugador in jugadores:
        if jugador[1] not in jugadores_eliminados and jugador[1] not in jugadores_plantados:
            eleccion = int(input(f"\nJuega {jugador[1]} \nPedir[1]    Plantarse[2]\n-> "))
            if eleccion != 1 and eleccion != 2:
                eleccion = int(input(f"\nJuega {jugador[1]} \nPedir[1]    Plantarse[2]\n-> "))
            else:
                if eleccion == 1:
                    carta, _ = obtener_carta()
                    Manos[jugador[1]].append(carta)
                    print(f"El jugador {jugador[1]} ha obtenido la carta {carta}")
                    sacar_valores(jugador)
                else:
                    print(f"El jugador {jugador[1]} se ha plantado.\n")
                    jugadores_plantados.append(jugador[1])
    revision()

def revision():
    print("\n")
    for jugador, mano in Manos.items():
        if jugador in jugadores_eliminados:
            print(Fore.RED +f"La mano del jugador {jugador} tiene las siguientes cartas: {' '.join(mano)}.[Jugador eliminado.]")
        elif jugador in jugadores_plantados:
            print(Fore.YELLOW + f"La mano del jugador {jugador} tiene las siguientes cartas: {' '.join(mano)}.[Jugador plantado.]")
        else:
            print(Fore.CYAN +f"La mano del jugador {jugador} tiene las siguientes cartas: {' '.join(mano)}")
        print(Fore.WHITE + "")

    if len(jugadores_eliminados) == len(jugadores):
        print("Todos los jugadores han perdido!")
        print(Fore.RED + "El crupier ha ganado.")
        print(Fore.WHITE + "")
        pregunta_final()
    elif len(jugadores_plantados) == len(jugadores):
        for jugador in jugadores:
            if jugador[1] in jugadores_plantados:
                distancia = sacar_valores(jugador)
                distancia = 21 - distancia
                distancia_21.append((distancia, jugador[1]))
        ganador = min(distancia_21)
        print(Fore.CYAN + f"\nTodos los jugadores se han plantado,[EL GANADOR ES -> {ganador[1]}]")  
        print(Fore.WHITE + "")
        pregunta_final()
    elif len(jugadores_eliminados) + len(jugadores_plantados) == len(jugadores):
        for jugador in jugadores:
            if jugador[1] in jugadores_plantados:
                distancia = sacar_valores(jugador)
                distancia = 21 - distancia
                distancia_21.append((distancia, jugador[1]))
        ganador = min(distancia_21)
        print(Fore.CYAN + f"\nLa partida ha finalizado,[EL GANADOR ES -> {ganador[1]}]")
        print(Fore.WHITE + "")
        pregunta_final()
    else:
        reparto_extra()


def obtener_carta():
    carta_numero = random.choice(list(baraja.keys()))
    palo = random.choice(palos)
    carta = f"{carta_numero} de {palo}"
    return carta, baraja[carta_numero]

def main():
    os.system("cls")
    definir_valores()
    numero_jugadores = saber_n_jugadores()
    nombres_jugadores = saber_nombres_jugadores(numero_jugadores)
    reparto()
    reparto_extra()

main()