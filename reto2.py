import os
import time

opcion1 = "Cambiar contraseña"
opcion2 = "Ingresar coordenadas actuales"
opcion3 = "Ubicar zona wifi más cercana"
opcion4 = "Guardar archivo con ubicación cercana"
opcion5 = "Actualizar registros de zonas wifi desde archivo"
opcion6 = "Elegir opción de menú favorita"
opcion7 = "Cerrar sesión"

listamenu = [opcion1, opcion2, opcion3, opcion4, opcion5, opcion6, opcion7]

contadorError = 0

print("Bienvenido al sistema de ubicación para zonas públicas WIFI")

nombreUsuario = "51747"
Contraseña = "74517"
captcha1 = 747
captcha2 = int((1**7)-7+5+5)
captcha3 = captcha1+captcha2

usuarioIngresado = input("Ingrese su usuario: ")
if usuarioIngresado == nombreUsuario:
    if input("Ingrese su contraseña: ") == Contraseña:
        verificacion = int(
            input(f"Por favor resuelva la siguiente operación: {captcha1} + {captcha2}: "))
        if verificacion == captcha3:
            os.system("cls")
            print("Sesión iniciada")
            time.sleep(2)
            while contadorError < 4:
                os.system("cls")
                for x in range(len(listamenu)):
                    print(f"{x+1} - {listamenu[x]}")
                opción_ingresada = int(input("Elija una opción: "))
                if opción_ingresada in range(1,8):
                    #opcionElegidalista = listamenu[opcionElegida-1]
                    if opción_ingresada == 1:
                        print(f"Usted ha eligido la opción {opción_ingresada}")
                        break
                    elif opción_ingresada == 2:
                        print(f"Usted ha eligido la opción {opción_ingresada}")
                        break
                    elif opción_ingresada == 3:
                        print(f"Usted ha eligido la opción {opción_ingresada}")
                        break
                    elif opción_ingresada == 4:
                        print(f"Usted ha eligido la opción {opción_ingresada}")
                        break
                    elif opción_ingresada == 5:
                        print(f"Usted ha eligido la opción {opción_ingresada}")
                        break

                    elif opción_ingresada == 6:
                        print(f"Usted ha elegido la opción {opción_ingresada}")
                        favorito = int(input("Seleccione opción favorita: "))
                        if favorito == 1 or favorito == 2 or favorito == 3 or favorito == 4 or favorito == 5:
                            if int(input("Si sumas 2+2 la respuesta es: ")) == 4:
                                if int(input("Al sumar 5+5 y a ese resultado le restas 3 la respuesta es: ")) == 7:
                                    mover = listamenu[favorito-1]
                                    listamenu.remove(mover)
                                    listamenu.insert(0, mover)
                                else:
                                    os.system("cls")
                                    print("Error")
                                    time.sleep(2)
                            else:
                                os.system("cls")
                                print("Error")
                                time.sleep(2)
                        else:
                            os.system("cls")
                            print("Error")
                            time.sleep(2)
                            continue
                    elif opción_ingresada == 7:
                        print("Hasta pronto")
                        exit()
                else:
                    contadorError += 1
                    os.system("cls")
                    print("Error")
                    time.sleep(2)
                    continue
        else:
            print("Error")
    else:
        print("Error")
else:
    print("Error")
