import random

opciones = ["A", "B", "C", "D", "V"]
peso = [1.25, 1.25, 1.25, 1.25, 1]

def test(repes, apuesta):
    jackpot_normal = 0
    jackpot_V = 0
    dosN_1V = 0
    dosV_1N = 0
    profit = 0
    ganancia = 0
    for i in range(repes):
        resultado_1, resultado_2, resultado_3 = random.choices(opciones, weights=peso, k=3)
        if resultado_1==resultado_2==resultado_3:
            if resultado_1 == "V":
                jackpot_V+=1
                ganancia = apuesta*20
            else:
                jackpot_normal+=1
                ganancia = apuesta*10
            profit += ganancia
        elif resultado_1==resultado_2!=resultado_3:
            if resultado_3 == "V":
                dosN_1V+=1
                ganancia = apuesta*2
                profit+=ganancia
            elif resultado_1 == "V":
                dosV_1N+=1
                ganancia = apuesta*5
                profit+=ganancia
        elif resultado_1==resultado_3!=resultado_2:
            if resultado_2 == "V":
                dosN_1V+=1
                ganancia = apuesta*2
                profit+=ganancia
            elif resultado_1 == "V":
                dosV_1N+=1
                ganancia = apuesta*5
                profit+=ganancia
        elif resultado_2==resultado_3!=resultado_1:
            if resultado_1 == "V":
                dosN_1V+=1
                ganancia = apuesta*2
                profit+=ganancia
            elif resultado_2 == "V":
                dosV_1N+=1
                ganancia = apuesta*5
                profit+=ganancia
    gano = profit
    profit-= apuesta*repes

    print(f"Jackpot_normal -> {jackpot_normal}\nJackpot_V -> {jackpot_V}\n2N+1V -> {dosN_1V}\n2V+1N -> {dosV_1N}\nTiradas -> {repes}\nMeto -> {repes*apuesta}\nGanancia -> {gano}\nProfit final -> {profit}")
    print(f"Ratio -> {round(1+profit/(repes*apuesta),2)}")
repes = int(input("Repes -> "))
apuesta = round(float(input("Apuesta -> ")),2)
test(repes, apuesta)