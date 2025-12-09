# Lista de clientes a evaluar (BD)

clientes = [
    {"DNI": "12345678", "nombre": "Ana Pérez", "deudas": [2000, 3000, 150], "ingreso": 1500},
    {"DNI": "45149735", "nombre": "Karen Carcamo", "deudas": [500, 200, 100], "ingreso": 8000},
    {"DNI": "07283014", "nombre": "Nancy Ortiz", "deudas": [500, 150, 300], "ingreso": 1130},
    {"DNI": "75482652", "nombre": "Jorge Mendoza", "deudas": [800, 100, 100], "ingreso": 5000},
    {"DNI": "78452446", "nombre": "Victor Fuentes", "deudas": [6500, 2000, 1000], "ingreso": 1800}
]



# Menu de consulta al analista 

def menuConsulta():
    print("------------------------------------------")
    print("      SISTEMA DE CRÉDITOS CASHBANK        ")
    print("------------------------------------------")

    cliente = consultarDNI()

    while True:    
        print("----------------------------------------------")
        print("¿Que deseas realizar?")
        print("1. Consultar calificación final")
        print("2. Consultar otro DNI")
        print("3. Salir")
        print("----------------------------------------------")


        opcion = input("Elige una opción (en numero): ")

        if opcion == "1":
            ratio, endeudamiento_total, estado, nivel = calculoFinal(cliente)
            calificacionFinal(cliente, ratio, endeudamiento_total, estado, nivel)
        elif opcion == "2":
            cliente = consultarDNI()
        elif opcion == "3" or opcion.lower() == "salir":
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


#CALCULO DE DEUDAS Y ENTRADAS
def calculoFinal(cliente):
    endeudamiento_total = sum(cliente["deudas"])
    ratio = endeudamiento_total / cliente["ingreso"]
    if ratio < 0.40:
        estado = "APROBADO"
        nivel = "Bajo endeudamiento"
    elif ratio < 0.80:
        estado = "APROBADO CON RIESGO"
        nivel = "Endeudamiento moderado"
    elif ratio < 1.0:
        estado = "REVISIÓN MANUAL"
        nivel = "Endeudamiento alto"
    else:
        estado = "RECHAZADO"
        nivel = "Endeudamiento crítico"

    return ratio, endeudamiento_total, estado, nivel


#Funcion para calcular el historial crediticio
def calificacionFinal(cliente, ratio, endeudamiento_total, estado, nivel):
    print(f"DNI: {cliente['DNI']}")
    print(f"Nombre: {cliente['nombre']}")
    print(f"Deuda total: {endeudamiento_total}")
    print(f"Ratio deuda/ingreso: {ratio:.2f}")
    print(f"Estado: {estado}")
    print(f"Nivel: {nivel}")


menuConsulta()