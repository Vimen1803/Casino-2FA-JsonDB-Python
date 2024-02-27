import random
import json
import smtplib
import os
import subprocess
from decouple import config
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

os.system("cls")

if os.path.exists("Usuarios/users.json"):
    pass
else:
    print("Primero deberas registrarte.\n")
    ruta = os.path.join("Usuarios", "Registro.py")
    subprocess.run(["python", ruta])

codigo = str(random.randint(100000, 999999))

correo_admin = config("correo_admin")
password = config("password")

server = smtplib.SMTP("smtp.gmail.com", port=587)
server.ehlo()
server.starttls()
server.login(correo_admin, password)

print("\t\t\t------------------\n\t\t\t INICIO DE SESION\n\t\t\t------------------")

def coger_datos():
    correo_user = input(str("\n¿Ingrese el correo al que desea acceder?--> "))
    correo_user = correo_user.lower()

    with open("Usuarios/users.json", "r") as f:
        js = json.load(f)
        if correo_user not in js:
            seleccion = str(input("\nEsta cuenta no existe.\nRegistrarte[0]\t\tIniciar sesion[1]\tSalir[2]\n-> "))
            if seleccion == "0":
                ruta = os.path.join("Usuarios", "Registro.py")
                subprocess.run(["python", ruta])
            elif seleccion == "1":
                coger_datos()
            else:
                quit()
        else:
            username = js[correo_user]["Username"]
            pass_log = str(input("\nIngrese su contraseña --> "))
            pass_user = js[correo_user]["Password"]     
            while pass_log != pass_user:
                pass_log = str(input("Contraseña incorrecta. Ingrese su contraseña --> "))

            enviar_mail(correo_user, username)

def enviar_mail(correo_user, username):
    with open("template\correo.html", 'r') as file:
        mensaje_html = file.read()
    mensaje_html = mensaje_html.replace('{codigo}', codigo)
    asunto = "Codigo de verificacion Vimen's app"
    
    mensaje = MIMEMultipart()
    mensaje['From'] = correo_admin
    mensaje['To'] = correo_user
    mensaje['Subject'] = asunto

    mensaje.attach(MIMEText(mensaje_html, 'html'))
    
    server.sendmail(correo_admin, correo_user, mensaje.as_string())

    codigo_usuario = str(input("\nSe le ha enviado un codigo secreto a la direccion de correo electronico.\nIngrese su codigo secreto --> "))
    while codigo_usuario!=codigo:
        codigo_usuario = str(input("Codigo incorrecto, intentelo de nuevo --> "))
    iniciar_menu(correo_user)

def iniciar_menu(correo_user):
    ruta = os.path.join("Interfaz", "Menu.py")
    subprocess.run(["python", ruta, correo_user])

coger_datos()