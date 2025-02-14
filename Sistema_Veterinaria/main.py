clientes = []

class SistemaVeterianaria:
    class Persona:
        id_counter = 1

        def __init__(self, nombre, contacto):
            self.id = SistemaVeterianaria.Persona.id_counter
            self.nombre = nombre
            self.contacto = contacto

            SistemaVeterianaria.Persona.id_counter += 1 

    class Cliente(Persona):
        def __init__(self, nombre, contacto, direccion):
            super().__init__(nombre, contacto)
            self.direccion = direccion
            self.mascota = []

        def agregar_mascota(self, mascota):
            self.mascota.append(mascota)

    class Mascota:
        id_counter = 1

        def __init__(self, nombre, especie, raza, edad):
            self.nombre = nombre
            self.especie = especie
            self.raza = raza
            self.edad = edad
            self.historial_clinico = []

    class Citas:
        id_counter = 1 

        def __init__(self, fecha, hora, servicio, veterinario):
            self.id = SistemaVeterianaria.Citas.id_counter
            self.fecha = fecha
            self.hora = hora
            self.servicio = servicio
            self.veterinario = veterinario

            SistemaVeterianaria.Citas.id_counter += 1

        def registrar_cliente():
            print("-_-_-_-_REGISTRO DE CLIENTES_-_-_-_-")
            nombre = input("por favor ingrese el nombre del cliente: ")
            contacto = input("por favor ingrese el contaco del cliente: ")
            direccion = input("por favor ingrese la direccion del cliente: ")
            cliente = SistemaVeterianaria.Cliente(nombre, contacto, direccion)

            print("--------REGISTRO DE MASCOTAS--------")
            nombre_mascota = input("por favor ingrese el nombre de la mascota: ")
            especie = input("por favor ingrese la especie: ")
            raza = input("por favor ingrse la raza: ")
            mascota = SistemaVeterianaria.Mascota(nombre_mascota, especie, raza)

            cliente.agregar_mascota(mascota)

            clientes.append(cliente)
            print("Cliente y mascota agregados con exito...")


        
        def programar_cita():
            pass

        def consultar_historial():
            pass

        def menu_principal():
            while True:
                print("=-=-=-=-Menu principal-=-=-=-=")
                print("1. Registrar cliente y mascota")
                print("2. Programar cita")
                print("3. Consultar historial de servicios")
                print("4. salir")
                opc = input("Seleccione una opcion: ")

                if opc == "1":
                    registrar_cliente()                   
                elif opc == "2":
                    pass
                elif opc == "3":
                    pass
                elif opc == "4":
                    pass
                else:
                    print("Opcion no valida.")
                    print("Por favor digite una de las occiones dentro del menu...")

menu_principal()



