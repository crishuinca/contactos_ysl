from funciones import *

while True:
    print(""" MENÚ CONTACTOS
          
          1. Agregar contacto
          2. Mostrar contactos
          3. Guardar archivo CSV
          4. Salir""")

    opc = validar_opcion([1,2,3,4])

    if opc == 1:
        opcion_1()
    elif opc == 2:
        opcion_2()
    elif opc == 3:
        opcion_3()
    else:
        opcion_4()
