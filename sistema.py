# Lista de clientes a evaluar (BD)

clientes = [
    {"DNI": "12345678", "nombre": "Ana Pérez", "historial": "Bueno", "clasificacion": "A"},
    {"DNI": "87654321", "nombre": "Juan Torres", "historial": "Regular", "clasificacion": "B"},
    {"DNI": "11112222", "nombre": "María López", "historial": "Malo", "clasificacion": "C"}
]


# Menu de consulta al analista 

def menuConsulta(personal):
    print(f"Bienvenido a la consulta {personal}")

    cliente = consultarDNI()

    while True:    
        print("----------------------------------------------")
        print("¿Que deseas realizar?")
        print("1. Consultar historial crediticio")
        print("2. Consultar clasificacion")
        print("3. Consultar otro DNI")
        print("4. Salir")
        print("----------------------------------------------")


        opcion = input("Elige una opción (en numero): ")

        if opcion == "1":
            calcularHistorial(cliente)
        elif opcion == "2":
            imprimirClasificacion(cliente)
        elif opcion == "3":
            cliente = consultarDNI()
        elif opcion == "4" or opcion.lower() == "salir":
            print("Saliendo del sistema...")
            print("¡Hasta pronto!")
            break
        else:
            print("Opcion incorrecta, intente nuevamente")

#Funcion de buscar cliente en la BD
def buscarCliente(dni):
    for i in clientes:
        if i["DNI"] == dni:
            return i
    return None

#Funcion para consultar si el DNI es válido o no existe en la BD
def consultarDNI():
    while True:
        dniPersona = input("Ingrese el DNI de la persona a consultar: ")

        if len(dniPersona) == 8 and dniPersona.isdigit():
            cliente = buscarCliente(dniPersona)
            if cliente:
                return cliente
            else:
                print("El DNI no existe en la Base de datos")
        else:
            print("DNI inválido, intente nuevamente")      

#Funcion para calcular el historial crediticio (puede moficarse)
def calcularHistorial(cliente):
    print(f"funciona {cliente['DNI']} {cliente['nombre']}")

#Funcion para imprimir la clasificacion (puede modificarse)
def imprimirClasificacion(cliente):
    print(f"funciona {cliente['DNI']} {cliente['nombre']}")


menuConsulta("Gabriel")