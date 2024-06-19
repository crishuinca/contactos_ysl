contactos = []

def opcion_1():
    print("AGREGAR CONTACTO")
    nombre = input("Ingrese nombre :")
    telefono = int(input("Ingrese teléfono :"))
    correo = input("Ingrese correo: ")
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
        nombre_archivo= input("Ingrese nombre del archivo : ")
        import csv
        with open(nombre_archivo+".csv","w", newline="") as archivo:
            escritor = csv.DictWriter(archivo,["nombre", "telefono", "correo"])
            escritor.writeheader()
            escritor.writerows(contactos)
            print("DEA ARCHIVO FUA CRIADO!!")
def opcion_4():
    pass