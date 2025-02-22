import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

clientes = []
mascotas = []

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
            self.mascotas = []

        def agregar_mascota(self, mascota):
            self.mascota.append(mascota)

    class Mascota:
        id_counter = 1

        def __init__(self, nombre, especie, raza, edad):
            self.id = SistemaVeterianaria.Mascota.id_counter
            self.nombre = nombre
            self.especie = especie
            self.raza = raza
            self.edad = edad
            self.historial_clinico = []

            SistemaVeterianaria.Mascota.id_counter += 1

        def agregar_cita(self, cita):
            self.historial_clinico.append(cita)

        def mostrar_historial(self):
            return self.historial_clinico

    class Cita:
        id_counter = 1 

        def __init__(self, fecha, hora, servicio, veterinario):
            self.id = SistemaVeterianaria.Cita.id_counter
            self.fecha = fecha
            self.hora = hora
            self.servicio = servicio
            self.veterinario = veterinario

            SistemaVeterianaria.Cita.id_counter += 1

        #funciones auxiliares
        def validar_fecha(fecha):
            from datetime import datetime
            try:
                datetime.strftime(fecha, "%Y-%m-%d")
                return True
            except ValueError:
                return False
            
        def validar_hora(hora):
            from datetime import datetime
            try:
                datetime.strftime(hora, "HH:MM")
                return True
            except ValueError:
                return False

        #funciones del sistema
        def registrar_cliente():
            print("-_-_-_-_REGISTRO DE CLIENTES_-_-_-_-")
            nombre = input("por favor ingrese el nombre del cliente: ").strip()
            contacto = input("por favor ingrese el contaco del cliente: ").strip()
            direccion = input("por favor ingrese la direccion del cliente: ").strip()
            cliente = SistemaVeterianaria.Cliente(nombre, contacto, direccion)
            clientes.append(cliente)
            print(f"Cliente registrado con exito. ID: {cliente.id}")

        def registrar_mascota():
            print("--------REGISTRO DE MASCOTAS--------")

            cliente_id = int(input("Ingrese el ID del cliente para vincular a la mascota: ").strip())
            cliente = next((c for c in clientes if c.id == cliente_id), None)

            if not cliente:
                print("cliente no encontrado")
                return

            nombre_mascota = input("por favor ingrese el nombre de la mascota: ").strip()
            especie = input("por favor ingrese la especie: ").strip()
            raza = input("por favor ingrse la raza: ").strip()
            edad = int(input("Por favor digite la edad de la mascota: ").strip())  
            mascota = SistemaVeterianaria.Mascota(nombre_mascota, especie, raza, edad)
            

            cliente.agregar_mascota(mascota)
            mascotas.append(mascota)
            print(f"Mascota registrada con exito, ID : {mascota.id}")
        
        def programar_cita():
            cliente_id = int(input("Ingrese el ID del cliente: ").strip())
            cliente = next((c for c in clientes  if c.id == cliente_id),None)

            if not cliente:
                print("cliente no encontrado")
                return
            
            mascota_id = int(input("Ingrese el ID de la mascota: "))
            mascota = next((m for m in cliente.mascotas if m.id == mascota_id), None)

            if not mascota:
                print("mascota no encontrada")
                return
            
            fecha = input("Ingrese la fecha de la cita(YYYY-MM-DD): ").strip()
            while not validar_fecha(fecha):
                print("Fecha invalida, Por favor digite el formato indicado (YYYY-MM-DD)")
            fecha = input("Ingrese la fecha de la cita(YYYY-MM-DD): ").strip()

            hora = input("Ingrese la hora  de la cita (HH:MM): ").strip()
            while not validar_hora(hora):
                print("Hora invalida, Por favor digite el formato indicado (HH:MM))")

            servicio = input("Ingrese el servicio (Consultoria, Vacunacion, etc..): ").strip()            
            veterinario = input("Ingrese el nombre del Veterinaro: ")

            cita = SistemaVeterianaria.Cita(fecha, hora, servicio, veterinario)
            mascota.agregar_cita(cita)
            print("Cita agendada")
            
        def consultar_historial():

            print("Consultar historial de citas ")

            cliente_id = int(input("Ingrese el ID del cliente: ").strip())
            cliente = next((c for c in clientes  if c.id == cliente_id),None)

            if not cliente:
                print("cliente no encontrado")
                return
            
            mascota_id = int(input("Ingrese el ID de la mascota: "))
            mascota = next((m for m in cliente.mascotas if m.id == mascota_id), None)

            if not mascota:
                print("mascota no encontrada")
                return
            
            mascota.mostrar_historial()

        #intefaz de usuario (tkinter)
        class VeterinariaApp:
            def __init__(self, root):
                self.root = root
                self.root.title("Sistema Veterinaria")
                self.root.geometry("500x600")

                self.clientes = clientes
                self.mascotas = mascotas

                self.main_menu()

            def clear_window(self):
                for widget in self.root.winfo_children():
                    widget.destroy()

            def main_menu(self):
                self.clear_window()
                
                tk.Label(self.root, text="Sistema de Veterinaria", font=("Arial Black", 16)).pack(pady=10)

                tk.Button(self.root, text="Registrar Cliente", command="", font=("ADLaM Display",10)).pack(pady=5)
                tk.Button(self.root, text="Registrar Mascota", command="",font=("ADLaM Display",10)).pack(pady=5)
                tk.Button(self.root, text="Programar Cita", command="",font=("ADLaM Display",10)).pack(pady=5)
                tk.Button(self.root, text="Consultal Historial de Citas", command="",font=("ADLaM Display",10)).pack(pady=5)
                tk.Button(self.root, text="salir", command="",font=("ADLaM Display",10)).pack(pady=5)
            
            def registrar_cliente():
                pass



        root = tk.Tk()
        app = VeterinariaApp(root)
        root.mainloop()


