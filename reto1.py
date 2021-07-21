import os
import time
print("Bienvenido al sistema de ubicación para zonas públicas WIFI")

nombreUsuario="51747"
Contraseña="74715"
captcha1=747
captcha2= int((1**7)-7+5+5)
captcha3=captcha1+captcha2


usuarioIngresado=input("Ingrese su usuario: ")
if usuarioIngresado==nombreUsuario:
    if input("Ingrese su contraseña: ") == Contraseña:
        verificacion =int(input(f"Por favor resuelva la siguiente operación: {captcha1} + {captcha2}: "))
        if verificacion == captcha3:
            time.sleep(2)
            print("Sesión iniciada")
        else:
            print("Error")
    else:
        print("Error")
else:
    print("Error")

