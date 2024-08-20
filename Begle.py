class Sistema:
    def __init__(self):
        self.__lista_pacientes = []
        self.__numero_pacientes = len(self.__lista_pacientes)

    def ingresarPaciente(self, paciente):
        self.__lista_pacientes.append(paciente)
        self.__numero_pacientes = len(self.__lista_pacientes)

    def verNumeroPacientes(self):
        return self.__numero_pacientes

    def verDatosPaciente(self):
        try:
            cedula = int(input("Ingrese la cedula a buscar: "))
        except ValueError:
            print("Error: La cédula debe ser un número.")
            return

        for paciente in self.__lista_pacientes:
            if cedula == paciente.verCedula():
                paciente.mostrarDatos()
                return
        print("Paciente no encontrado.")
    
    def verificarPaciente(self,cedula):
        encontrado = False
        for p in self.__lista_pacientes:
            if cedula == p.verCedula():
                encontrado = True
                break
        return encontrado

class Paciente:
    def __init__(self):
        self.__nombre = ""
        self.__cedula = 0
        self.__genero = ""
        self.__servicio = ""

    def verNombre(self):
        return self.__nombre

    def verServicio(self):
        return self.__servicio

    def verGenero(self):
        return self.__genero

    def verCedula(self):
        return self.__cedula

    def asignarNombre(self, n):
        self.__nombre = n

    def asignarServicio(self, s):
        self.__servicio = s

    def asignarGenero(self, g):
        self.__genero = g

    def asignarCedula(self, c):
        self.__cedula = c

    def mostrarDatos(self):
        print(f"Nombre: {self.__nombre}")
        print(f"Cédula: {self.__cedula}")
        print(f"Género: {self.__genero}")
        print(f"Servicio: {self.__servicio}")