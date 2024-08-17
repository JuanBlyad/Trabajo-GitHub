
from Begle import Paciente, Sistema


def main():
    sis = Sistema()

    while True:
        try:
            opcion = int(input("Ingrese 0 para salir, 1 para ingresar nuevo paciente, 2 para ver paciente: "))
        except ValueError:
            print("Error: Debe ingresar un número.")
            continue

        if opcion == 1:
            print("A continuación se solicitarán los datos ...")
            nombre = input("Ingrese el nombre: ")
            try:
                cedula = int(input("Ingrese la cédula: "))
            except ValueError:
                print("Error: La cédula debe ser un número.")
                continue

            genero = input("Ingrese el género: ")
            servicio = input("Ingrese el servicio: ")

            pac = Paciente()
            pac.asignarCedula(cedula)
            pac.asignarGenero(genero)
            pac.asignarNombre(nombre)
            pac.asignarServicio(servicio)

            sis.ingresarPaciente(pac)

        elif opcion == 2:
            sis.verDatosPaciente()

        elif opcion == 0:
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
