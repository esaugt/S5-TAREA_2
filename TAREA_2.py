class Paciente:
    def __init__(self, nombre, edad,CEDULA, genero):
        self.nombre = nombre
        self.edad = edad
        self.cedula=CEDULA
        self.genero = genero

class Receta:
    def __init__(self,paciente, medicamentos, dosificacion):
        self.paciente = paciente
        self.medicamentos = medicamentos
        self.dosificacion = dosificacion

class Cita:
    def __init__(self,paciente , horario, motivo):
        self.paciente = paciente
        self.horario = horario
        self.motivo = motivo

class HistoriaClinica:
    def __init__(self,paciente, sintomas, diagnosticos, tratamientos):
        self.paciente = paciente
        self.sintomas = sintomas
        self.diagnosticos = diagnosticos
        self.tratamientos = tratamientos

pacientes = []
recetas = []
citas = []
historias_clinicas = []


while True:
    print("""
    .--------------------------------------.
    |              C-UNEMI                 |
    |--------------------------------------|
    |                                      |
    |   1. Agregar Paciente                |
    |   2. Ingresar Receta                 |
    |   3. Agendar Cita                    |
    |   4. Ingresar Historia Clinica       |
    |   5. Mostrar Pacientes               |
    |   6. Mostrar Recetas                 |
    |   7. Mostrar Citas                   |
    |   8. Mostrar Historia Clinica        |
    |   9. Salir                           |
    |                                      |
    .--------------------------------------.""")

    opcion = int(input("\nIngresa una opcion: "))

    if opcion == 1:
        nombre = input("Ingresa el nombre del paciente: ")
        edad = int(input("Ingresa la edad del paciente: "))
        cedula= int(input("Ingresa la cedula del paciente: "))
        genero = input("Ingresa el genero del paciente (M/F): ")
        paciente1 = Paciente(nombre, edad,cedula, genero)
        pacientes.append(paciente1)
        print("\nPaciente agregado correctamente")

    elif opcion == 2:
        if len(pacientes) == 0:
            print("\nNo hay pacientes registrados, primero agrega un paciente")
        else:
            print("\nPacientes: ")
            for i, paciente in enumerate(pacientes):
                print(f"{i+1}. {paciente.nombre}")
            seleccion = int(input("\nSelecciona un paciente: "))
            paciente_seleccionado = pacientes[seleccion-1]
            medicamentos = input("Ingresa los medicamentos a recetar (separados por coma): ")
            dosificacion = input("Ingresa la dosificacion de cada medicamento (separados por coma): ")
            receta1 = Receta(paciente_seleccionado.nombre, medicamentos, dosificacion)
            recetas.append(receta1)
        print("\nReceta agregada correctamente")


 
    elif opcion == 3:
        if len(pacientes) == 0:
            print("\nNo hay pacientes registrados, primero agrega un paciente")
        else:
            print("\nPacientes: ")
            for i, paciente in enumerate(pacientes):
                print(f"{i+1}. {paciente.nombre}")
            seleccion = int(input("\nSelecciona un paciente: "))
            paciente_seleccionado = pacientes[seleccion-1]
            horario = input("Ingresa el horario de la cita: ")
            motivo = input("Ingresa el motivo de la cita: ")
            cita1 = Cita(paciente_seleccionado.nombre, horario, motivo)
            citas.append(cita1)
        print("\nCita agendada correctamente")




    elif opcion ==4:
        if len(pacientes) == 0:
            print("\nNo hay pacientes registrados, primero agrega un paciente")
        else:
            print("\nPacientes: ")
            for i, paciente in enumerate(pacientes):
                print(f"{i+1}. {paciente.nombre}")
            seleccion = int(input("\nSelecciona un paciente: "))
            paciente_seleccionado = pacientes[seleccion-1]
            sintomas = input("Ingresa los sintomas del paciente (separados por coma): ")
            diagnosticos = input("Ingresa los diagnosticos del paciente (separados por coma): ")
            tratamientos = input("Ingresa los tratamientos del paciente (separados por coma): ")
            historia_clinica1 = HistoriaClinica(paciente_seleccionado.nombre, sintomas, diagnosticos, tratamientos)
            historias_clinicas.append(historia_clinica1)
        print("\nHistoria clinica agregada correctamente")


    elif opcion == 5:
        if len(pacientes) == 0:
            print("\nNo hay pacientes registrados, primero agrega un paciente")
        else:
            print("\nPacientes: ")
            for paciente in pacientes:
                print(f"Clinica: C-Unemi") 
                print(f"Ruc: 21121718112022")
                print(f"Nombre: {paciente.nombre}")
                print(f"Edad: {paciente.edad}")
                print(f"Genero: {paciente.genero}")
                print("""""")

    elif opcion == 6:
        if len(recetas) == 0:
            print("\nNo hay recetas registradas, primero ingresa una receta")
        else:
            print("\nReceta: ")
            for receta in recetas:
                print(f"                DR.JULIO DIAZ.                  ")
                print(f"| Clinica: C-Unemi          Ruc: 21121718112022 ") 
                print(f"| Paciente: {receta.paciente}")
                print(f"| Cedula:{paciente.cedula}")
                print(f"| Edad: {paciente.edad}    ")
                print(f"| ----------------------------------------------")
                print(f"| Medicamentos: {receta.medicamentos}           ")
                print(f"| ----------------------------------------------")
                print(f"| Dosificación: {receta.dosificacion}           ")
                print(f"| ----------------------------------------------|")
                print(f"|                CONTACTANOS                    |")
                print(f"|                098192****                     |")
                print(f"| ----------------------------------------------|")
                print("""""")

    elif opcion == 7:
        if len(citas) == 0:
            print("\nNo hay citas agendadas, primero agenda una cita")
        else:
            print("\nCitas: ")

            for cita in citas:
                print(f"Clinica: C-Unemi") 
                print(f"Ruc: 21121718112022")
                print(f"Paciente: {cita.paciente}\nsu Cita esta programada para el dia : ")
                print(f"Horario: {cita.horario}")
                print(f"Motivo: {cita.motivo}")
                print("""""")
    elif opcion == 8:
        if len(historias_clinicas) == 0:
            print("\nNo hay historias clinicas registradas, primero ingresa una historia clinica")
        else:
            print("\nHistoria Clinica ")
            for historia in historias_clinicas:
                print(f"                DR.JULIO DIAZ.                  ")
                print(f"| Clinica: C-Unemi          Ruc: 21121718112022 ") 
                print(f"| Paciente: {historia.paciente} Edad: {paciente.edad}")
                print(f"| Cedula:{paciente.cedula}")
                print(f"| Sintomas: {historia.sintomas}")
                print(f"| ----------------------------------------------")
                print(f"| Diagnosticos: {historia.diagnosticos}           ")
                print(f"| ----------------------------------------------")
                print(f"| Tratamientos: {historia.tratamientos}           ")
                print(f"| ----------------------------------------------|")
                print(f"|                CONTACTANOS                    |")
                print(f"|                098192****                     |")
                print(f"| ----------------------------------------------|")
                print("""""")

    elif opcion == 9:
        print("\nGracias Por Preferirnos. Somos C-UNEMI")
        print(""" """)
        break
    else:
        print("\nOpcion incorrecta, intenta nuevamente")