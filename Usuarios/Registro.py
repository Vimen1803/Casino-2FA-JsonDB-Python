import json
import random
from datetime import datetime
import smtplib
import re
import string
import subprocess
import os
from decouple import config
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

os.system("cls")

email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

correo_admin = config("correo_admin")
password = config("password")

if os.path.exists("Usuarios/users.json"):
    with open("Usuarios/users.json", "r") as h:
        c = h.read()
        js = json.loads(c)
else:
    with open("Usuarios/users.json", "w", encoding="utf8") as f:
        json.dump({}, f, indent= 6)
        f.close()
        with open("Usuarios/users.json", "r") as h:
            c = h.read()
            js = json.loads(c)

server = smtplib.SMTP("smtp.gmail.com", port= 587)
server.ehlo()

server.starttls()
server.login(correo_admin, password) 

print("\n\n\t\t\t---------\n\t\t\t Registro\n\t\t\t---------\n\n")

def coger_datos():
    username = str(input("¿Cual es tu username? --> "))
    while len(username) < 4:
        username = str(input("Usuario no valido.\n¿Cual es tu username? --> "))
        
    correo_user = str(input("¿Cual es tu gmail? --> " ))
    if correo_user in js:
        entrada = False
    else:
        if re.match(email_pattern, correo_user):
            entrada = True
        else: 
            entrada = False
    while entrada == False:
        correo_user = str(input("Correo no valido.\n¿Cual es tu gmail? --> " ))
        if re.match(email_pattern, correo_user) and correo_user not in js:
            entrada = True

    pass_user = str(input("¿Cual es tu contraseña? --> "))
    while len(pass_user) < 8:
        pass_user = str(input("Contraseña no valida.\n¿Cual es tu contraseña? --> "))
        
    enviar_correo(correo_user, username, pass_user)

def enviar_correo(correo_user, username, pass_user):
    with open("template\correo.html", 'r') as file:
        mensaje_html = file.read()
    codigo = str(random.randint(100000,999999))
    mensaje_html = mensaje_html.replace('{codigo}', codigo)
    asunto = "Codigo de verificacion Vimen's app"
    
    mensaje = MIMEMultipart()
    mensaje['From'] = correo_admin
    mensaje['To'] = correo_user
    mensaje['Subject'] = asunto

    mensaje.attach(MIMEText(mensaje_html, 'html'))
    
    server.sendmail(correo_admin, correo_user, mensaje.as_string())
    
    codigo_usuario = str(input("Se le ha enviado un codigo secreto a la direccion de correo electronico.\nIngrese su codigo secreto --> "))
    while codigo_usuario != codigo:
        codigo_usuario = str(input("Codigo incorrecto, vuelva a intentarlo --> "))

    guardar_datos(correo_user, username, pass_user)

def guardar_datos(correo_user, username, pass_user):
    with open("Usuarios/users.json", "w", encoding="utf8") as f:
        caracteres = string.ascii_letters + string.digits
        tag = ''.join(random.choices(caracteres, k=4))
        tag = str(tag)
        tag = tag.upper()
        now = datetime.now()
        fecha = (f"{now.day}-{now.month}-{now.year}|{now.hour}:{now.minute}")
        usuario = correo_user.lower()
        js[str(usuario)] = { }
        js[str(usuario)]["TAG"] = (f"#{tag}")
        js[str(usuario)]["Username"] = username
        js[str(usuario)]["Password"] = pass_user
        js[str(usuario)]["Dinero"] = 200
        js[str(usuario)]["Partidas"] = {"RPS": {"Wins": 0, "Partidas Totales": 0, "Dinero Invertido": 0}, "Tragaperras": {"Wins": 0, "Partidas Totales": 0, "Dinero Invertido": 0}, "Ruleta": {"Dinero Invertido": 0}}
        js[str(usuario)]["Fecha de creacion"] = fecha
        user = json.dump(js, f, indent= 6)
        f.flush()
        print("Verificacion realizada con éxito")
        iniciar_menu(correo_user)

def iniciar_menu(correo_user):
    ruta = os.path.join("Interfaz", "Menu.py")
    subprocess.run(["python", ruta, correo_user])

coger_datos()