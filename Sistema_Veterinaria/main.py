from abc import ABC, abstractmethod
from datetime import datetime

#definicion de las clases abstractas
class Persona(ABC):
    def __init__(self, nombre, contacto, direccion):
        self.nombre = nombre
        self.contacto = contacto
        self.direccion = direccion  

    @abstractmethod
    def mostrar_informacion(self):
        pass

class Mascota(ABC):
    def __init__(self, nombre, especie, raza, edad):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.historial_citas = []

    @abstractmethod
    def agregar_al_historial(self, detalles_servicio):
        pass

class Cita(ABC):
    def __init__(self, fecha, hora, servicio, veterinario):
        self.fecha = fecha
        self.hora = hora
        self.servicio = servicio
        self.veterinaria = veterinario

    @abstractmethod
    def actualizar(self, **kwargs):
        pass

#definicion de las subclases
class Cliente(Persona):
    def __init__(self, nombre, contacto, direccion):
        super().__init__(nombre, contacto, direccion)
        self.mascotas = []

    def agregar_mascota(Self, mascota):
        Self.mascotas.append(mascota)

    def mostrar_informacion(self):
        return f"cliente: {self.nombre}, contacto: {self.contacto}, direccion: {self.direccion}"
    
class ResgistroMascotas(Mascota):
    def agregar_al_historial(self, detalles_servicio):
        self.historial_citas.append(detalles_servicio)

    def obtenerHistorial(Self):
        return Self.historial_citas
    
class CitaMascota(Cita):
    def actualizar(self, **kwargs):
        for clave, valor in kwargs.items():
            if hasattr(self, clave):
                setattr(self, clave, valor)

class SistemaVeterinaria:
    def __init__(self):
        self.clientes = []

    def registrar_clientes(self):
        try:
            nombre = input("Ingrse el nombre del cliente: ").strip()
            contacto = input("Ingrese el contacto: ").strip()
            direccion = input("Ingrese la direccion: ").strip()

            if not nombre or not contacto or not direccion:
                raise ValueError("Todos los campos deben ser diligenciados.. ")
            
            cliente = Cliente(nombre, contacto, direccion)
            self.clientes.append(cliente)
            print ("cliente registrado con èxito")
            
        except ValueError as e:
            print(f"Error: {e}")

    def registrar_mascota(Self):
        try:
            nombre_cliente = input("Ingrese el nombre del cliente al que asociar la mascota: ").strip()
            #funcion blanda
            cliente = next((c for c in Self.clientes if c.nombre == nombre_cliente), None)
            
            if not cliente:
                raise ValueError("cliente no encontrado....")
            
            nombre_mascota = input("Ingrese el nombre de la mascota: ").strip()
            especie = input("Ingrese la especie: ").strip()
            raza = input("Ingrese la raza: ").strip()
            edad = int(input("Ingrese la edad: ").strip())

            if  not nombre_mascota or not especie or not raza or  edad <= 0:
                raise ValueError("Detalles de la mascota invalidos")
            
            mascota = ResgistroMascotas(nombre_mascota, especie, raza, edad)
            cliente.agregar_mascota(mascota)
            print("Mascota registrada con èxito..")

        except ValueError as e:
            print(f"Error: {e}")
        pass
        

    def programar_cita(self):
        try:
            nombre_cliente = input("Ingrese el nombre del cliente: ").strip()
            nombre_mascota = input("Ingrese el nombre de la mascota: ").strip()

            cliente = next((c for c in self.clientes if c.nombre == nombre_cliente), None)            
            if not cliente:
                raise ValueError("cliente no encontrado....")
            
            mascota = next((m for m in cliente.mascotas if m.nombre == nombre_mascota), None)
            if not mascota:
                raise ValueError("mascota no encontrada...")
            
            #fecha, hora, servicio, veterinario
            fecha = input("ingrese la fecha (AAAA-MM-DD): ").strip()
            hora = input("Ingrese la hora (HH:MM): ").strip()
            servicio = input("ingrese el servicio (colsulta, vacunacion, etc): ").strip()
            veterinario = input("Ingrese el nombre del veterinario: ").strip()

            datetime.strptime(fecha, "%Y-%m-%d")
            datetime.strptime(hora, "%H:%M")

            if not servicio or not veterinario:
                raise ValueError("detalles de la cita invalidos..")
            
            cita = CitaMascota(fecha, hora, servicio, veterinario)
            mascota.agregar_al_historial(cita)
            print("cita programada con exito")
            
            
        except ValueError as e:  
            print(f"error: {e}")

    def cancerlar_cita(self):
        try:
            nombre_cliente = input("Ingrese el nombre del cliente: ").strip()
            nombre_mascota = input("Ingrese el nombre de la mascota: ").strip()

            cliente = next((c for c in self.clientes if c.nombre == nombre_cliente), None)            
            if not cliente:
                raise ValueError("cliente no encontrado....")
            
            mascota = next((m for m in self.cliente.mascotas if m.nombre == nombre_mascota), None)
            if not mascota:
                raise ValueError("mascota no encontrada...") 

            if not mascota.historial_citas:
                raise ValueError("no hay citas registradas para esta mascota")

            print("Citas registradas:")
            for i, cita in enumerate(mascota.historial_citas):
                print(f"{i + 1}, Fecha: {cita.fecha}, Hora: {cita.hora}, servicio{cita.servicio}, Veterinario{cita.veterinario}")
            
            indice = int(input("Seleccione el numero de la cita a cancelar: ").strip()) - 1
            if indice < 0 or indice >= len.delete(mascota.historial_citas):
                raise ValueError("Seleccion invalida")           

            print (f"cita cancelada")
        except ValueError as e: 
            print(f"error: {e}")
            





    def actualizar_cita(self):
        try: 
            nombre_cliente = input("Ingrese el nombre del cliente: ").strip()
            nombre_mascota = input("Ingrese el nombre de la mascota: ").strip()

            cliente = next((c for c in self.clientes if c.nombre == nombre_cliente), None)            
            if not cliente:
                raise ValueError("cliente no encontrado....")
            
            mascota = next((m for m in self.cliente.mascotas if m.nombre == nombre_mascota), None)
            if not mascota:
                raise ValueError("mascota no encontrada...")    
            
            if not mascota.historial_citas:
                raise ValueError("no hay citas registradas para esta mascota")
            
            print("Citas disponibles para actualizar:")
            for i, cita in enumerate(mascota.historial_citas):
                print(f"{i + 1}, Fecha: {cita.fecha}, Hora: {cita.hora}, servicio{cita.servicio}, Veterinario{cita.veterinario}")

            indice = int(input("Seleccione el numero de la cita a actualizar: ").strip()) - 1
            if indice < 0 or indice >= len(mascota.historial_citas):
                raise ValueError("Seleccion invalida")

            cita = mascota.historial_citas[indice]

            print("Deje en blanco los campos de no desea actualizar: ")
            nueva_fecha = input("Nueva fecha (AAAA-MM-DD): ").strip()
            nueva_hora = input("Nueva hora (HH-MM): ").strip()
            nuevo_servicio = input("Nuevo servicio: ").strip()
            nuevo_veterinario = input("Nuevo veterinario: ").strip()

            if nueva_fecha:
                datetime.strptime(nueva_fecha, "%Y-%m-%d")
                cita.actualizar(fecha = nueva_fecha)
            if nueva_hora:
                datetime.strptime(nueva_hora, "%H:%M")
                cita.actualizar(hora = nueva_hora)

            if nuevo_servicio:
                cita.actualizar(servicio = nuevo_servicio)
            if nuevo_veterinario:
                cita.actualizar(veterinario = nuevo_veterinario)

            print("¡Cita actualizada con exito!")

        except ValueError as e:  
            print(f"error: {e}")

    def consultar_historial(self):
        try:
            nombre_cliente = input("Ingrese el nombre del cliente: ").strip()
            nombre_mascota = input("Ingrese el nombre de la mascota: ").strip()

            cliente = next((c for c in self.clientes if c.nombre == nombre_cliente), None)            
            if not cliente:
                raise ValueError("cliente no encontrado....")
            
            mascota = next((m for m in self.cliente.mascotas if m.nombre == nombre_mascota), None)
            if not mascota:
                raise ValueError("mascota no encontrada...")
            
            historial = mascota.obtener_historial()
            if not historial:
                print("No hay historial disponible para esta mascota. ")
            else: 
                for entrada in historial:
                    print(f"Fecha: {entrada.fecha}, Hora: {entrada.hora}, servicio{entrada.servicio}, Veterinario{entrada.veterinario}")
                    

        except ValueError as e:  
            print(f"error: {e}")
    
    def iniciar(self):
        while True:
            print("\nSistema de gestion veterinaria")
            print("1. registrar cliente")
            print("2. registrar mascota")
            print("3. programar cita")
            print("4. cancelar cita")
            print("5. actualizar cita ")
            print("6. consultar historial")
            print("7. salir")

            opcion = input("ingrese una opcion").strip()
            if opcion == "1":
                self.registrar_clientes()
            elif opcion == "2":
                self.registrar_mascota()
            elif opcion == "3":
                self.programar_cita()
            elif opcion == "4":
                self.actualizar_cita()
            elif opcion == "6":
                self.consultar_historial()
            elif opcion == "7":
                print("Saliendo del sistema. ¡adios!")
                break
            else:
                print("opcion invalida. por favor, intentede nuevo.")

if __name__ == "__main__":
    sistema = SistemaVeterinaria()
    sistema.iniciar()







