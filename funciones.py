contactos = []

import os, msvcrt , time

def opcion_1():
    print("AGREGAR CONTACTO")
    nombre = validar_nombre()
    telefono = validar_telefono()
    correo = validar_correo()
    contacto = {"nombre": nombre, 
                "telefono": telefono,
                "correo": correo}
    contactos.append(contacto)
    print("CONTACTO AÑADIO!")
def opcion_2():
    if len(contactos) == 0:
        print("No existen contactos, meta alguno po loko")
    else:
        print("LISTA DE CONTACTOS")
        for c in contactos:
            print(f"NOMBRE : {c['nombre']}")
            print(f"TELEFONO : {c['telefono']}")
            print(f"CORREO : {c['correo']}")
            
def opcion_3():
    if len(contactos) == 0:
        print("No existen contactos, meta alguno po loko")
    else:
        validar_nom_archivo()
        import csv
        with open(nombre_archivo+".csv","w", newline="") as archivo:
            escritor = csv.DictWriter(archivo,["nombre", "telefono", "correo"])
            escritor.writeheader()
            escritor.writerows(contactos)
            print("DEA ARCHIVO FUA CRIADO!!")
def opcion_4():
    print ("ADIOS NIGGA")
    time.sleep(1)

    
#VALIDACIONES

def validar_opcion(lista_opciones):
    while True:
        try:
            opc = int(input("Ingrese opcion : "))
            if opc in lista_opciones:
                return opc
            else:
                print("ERROR! opcion incorrecta")
        except:
            print("ERROR! Debe ingresar un número entero!")

def validar_nombre():
    while True:
        nombre = input("Ingrese nombre : ")
        if len(nombre)>=3 and nombre.isalpha():
            return nombre
        else:
            print("ERROR! El nombre debe tener al menos 3 letras!")

def validar_telefono():
    while True:
        try:
            telefono = int(input("Ingrese telefono : "))
            if len(str(telefono))== 9 and str(telefono)[0]=="9":
                return telefono
            else:
                print("ERROR! El telefono debe empezar con 9 y tiene que empezar con 9")
        except:
            print("")

def validar_correo():

    while True:
        correo = input("Ingrese correo : ")
        if correo.lower().endswith("@gmail.com") and len(correo.strip())>=13:
            return correo
        else:
            print("ERROR! Correo incorrecto!")

def validar_nom_archivo():

    while True:
        nombre_archivo = input("Ingrese nombre archivo:")
        if len(nombre_archivo.strip())>=3:
            return nombre_archivo
        else:
            print("El archivo tiene que tener 3 o mas letras")