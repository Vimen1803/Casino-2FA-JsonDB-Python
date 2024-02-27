# Casino en Python

Este proyecto es un casino virtual desarrollado en Python. Permite a los usuarios registrarse, iniciar sesión, jugar diferentes juegos como la ruleta, tragaperras y piedra papel o tijera, así como acceder a información sobre su perfil y saldo.

## Funcionalidades

- **Registro e inicio de sesión:** Los usuarios pueden registrarse proporcionando un nombre de usuario, correo electrónico y contraseña. Se utiliza verificación en dos pasos mediante correo electrónico para asegurar la autenticación segura.
- **Perfil de usuario:** Los usuarios pueden ver información sobre su perfil, incluyendo su nombre de usuario, correo electrónico, saldo disponible y ratio de victorias.
- **Juegos de casino:**
  - **Tragaperras:** Prueba tu suerte en las tragaperras y gana premios.
  - **Piedra, papel o tijera:** Juega al clásico juego de piedra, papel o tijera contra la computadora.

  - **PROXIMAMENTE:**
    - **Ruleta:** Juega a la ruleta y apuesta en diferentes números, colores o jugadas.
    - **BlackJack o 21:** Añadiré la opción de un solo jugador contra la máquina y la conexión con la DataBase.

## Archivos

- **index.py:** El archivo principal que inicia el programa.
- **Usuarios/Inicio_Sesion.py:** Contiene funciones de inicio de sesión.
- **Usuarios/Registro.py:** Contiene funciones de registro.
- **Usuarios/users.json:** Archivo JSON utilizado para almacenar datos de usuarios, partidas y saldo.
- **Interfaz/menu.py:** Contiene funciones para mejorar la jugabilidad.
- **Juegos/Tragaperras.py Juegos/RPS.py Juegos/Ruleta.py:** Código de los juegos a los que podremos jugar.
- **Jueegos/test/traga_test.py:** Archivo de prueba para revisar la jugabilidad.
- **Juegos/test/blackjack_test.py:** Juego de blackjack, sin conectar a la DataBase.
- **correo.html:** Mensaje que será enviado por e-mail para la 2FA.

## Requisitos

El programa requiere Python 3.x y algunas bibliotecas adicionales que se pueden instalar utilizando `pip`.

```bash
pip install -r requirements.txt
```

## Uso

1. Clona o descarga el repositorio en tu máquina local.
2. Crea el archivo `.env`y añade:
                            - correo_admin = "tu_correo"
                            - password = "tu_contraseña"
3. Abre una terminal y navega hasta el directorio del proyecto.
4. Ejecuta el archivo `main.py` para iniciar el programa.

```bash
python main.py
```

5. Sigue las instrucciones en pantalla para registrarte, iniciar sesión y disfrutar de los juegos de casino.

## Problemas y contacto

Si encuentras algún bug o tienes alguna pregunta sobre el funcionamiento del casino, no dudes en contactarme por correo electrónico. Por favor, incluye una descripción detallada del problema que encontraste.

- Contáctame mediante [este correo electrónico](mailto:victormnjfan@gmail.com)

## Notas adicionales

- El saldo en el casino es ficticio y solo se utiliza con propósitos de demostración.
- Se recomienda utilizar una dirección de correo electrónico válida durante el registro para la verificación en dos pasos.
- Este proyecto no trata de promover la ludopatía.

¡Diviértete jugando en el casino virtual desarrollado en Python! Si tienes alguna pregunta o sugerencia, no dudes en contactarme.

---

*Autor: [Vimen1803](https://github.com/Vimen1803)*