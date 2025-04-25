# Sistema de venta de billetes de avión

class Vuelo:
    def __init__(self, numero_vuelo, origen, destino, fecha, salida, llegada, precio):
        self.numero_vuelo = numero_vuelo
        self.origen = origen
        self.destino = destino
        self.fecha = fecha
        self.salida = salida #cambio
        self.llegada = llegada #cambio
        self.precio = precio

    def __str__(self):
        return (f"Número de vuelo: {self.numero_vuelo}, Origen: {self.origen}, destino: {self.destino}, Fecha: {self.fecha}, hora de salida: {self.salida}, hora de 		llegada: {self.llegada}, precio: {self.precio}€")

class Pasajero:
    def __init__(self, nombre, apellido, edad, telefono, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.telefono = telefono
        self.correo = correo
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}, Edad: {self.edad}, Tel: {self.telefono}, Email: {self.correo}"

class Informacion:
    def __init__(self, vuelo, pasajero, asientos):
        self.vuelo = vuelo
        self.pasajero = pasajero
        self.asientos = asientos

def mostrar_vuelos_disponibles(vuelos):
    print("Vuelos disponibles:")
    for vuelo in vuelos:
        print(vuelo)

def pedir_datos_pasajero():
    nombre = input("Ingrese su nombre: ")
    apellidos = input("Ingrese su apellido: ")
    edad = int(input("Ingrese su edad: "))
    telefono = input("Ingrese su número de teléfono: ")
    correo = input("Ingrese su correo electrónico: ")
    return Pasajero(nombre, apellidos, edad, telefono, correo)

def reserva():
    numero = input("Ingrese el número de vuelo que desea reservar: ")
    cantidad = int(input("Ingrese la cantidad de asientos que desea reservar (máximo 10): "))
    return numero, cantidad

def reservar_vuelo(lista, numero_vuelo, pasajero, cantidad):
    for vuelo in lista:
        if vuelo.numero_vuelo == numero_vuelo:
            if cantidad <= 0:
                print("La cantidad de asientos debe ser mayor que cero.")
                return
            elif cantidad > 10:
                print("Lo sentimos, no se pueden reservar más de 10 asientos por reserva.")
                return
            reserva = Informacion(vuelo, pasajero, cantidad)
            print(f"¡Reserva exitosa para el vuelo {vuelo.numero_vuelo}!")
            print(f"Nombre del pasajero: {pasajero.nombre} {pasajero.apellido}, Asientos reservados: {cantidad}")
            return reserva
    print("No se encontró ningún vuelo con el número especificado.")


def main():
    vuelos = [
        Vuelo("AA123", "Nueva York", "Los Angeles", "2024-05-15", "08:00", "11:00", 250.00),
        Vuelo("AA456", "Los Angeles", "Chicago", "2024-05-20", "10:00", "13:00", 200.00),
        Vuelo("AA789", "Chicago", "Miami", "2024-05-25", "12:00", "15:00", 300.00)
    ]

    print("Bienvenido al sistema de venta de billetes de avión.")
    opcion = input("Seleccione una opción:\n1. Ver vuelos disponibles\n2. Reservar vuelo\nIngrese su opción: ")

    if opcion == '1':
        mostrar_vuelos_disponibles(vuelos)
        
    elif opcion == '2':
        pasajero = pedir_datos_pasajero()
        numero_vuelo, cantidad_asientos = reserva()
        reservar_vuelo(vuelos, numero_vuelo, pasajero, cantidad_asientos)
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()
