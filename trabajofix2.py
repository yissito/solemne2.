medicos = {
    "medico1": "contrasena1",
    "medico2": "contrasena2",
}

mascotas = {}


def ingresar_informacion():
    nombre = input("Nombre de su Mascota: ")
    numero_chip = input("Número del chip de su Mascota: ")
    tutor = input("Nombre del Tutor: ")
    fecha_ultima_vacuna = input("Fecha de la última vacuna (dia-mes-ano): ")

    mascotas[numero_chip] = {
        "nombre": nombre,
        "tutor": tutor,
        "fecha_ultima_vacuna": fecha_ultima_vacuna
    }
    print("Su mascota ha sido registrada con éxito.")


def consultar_informacion():
    numero_chip = input("Número de chip de la Mascota: ")
    if numero_chip in mascotas:
        mascota = mascotas[numero_chip]
        print("Nombre de la Mascota:", mascota["nombre"])
        print("Nombre del Tutor:", mascota["tutor"])
        print("Número de chip de la Mascota:", numero_chip)
        print("Fecha última vacuna:", mascota["fecha_ultima_vacuna"])
        if mascota["extraviada"]:
            print("Estado: MASCOTA EXTRAVIADA")
        else:
            print("Estado: SIN INCIDENCIAS")


def main():
    while True:
        print("Menú de opciones:")
        print("1. Ingresar Información")
        print("2. Consultar Información")
        print("3. Salir")
        opcion = input("Seleccione una opción (1,2,3): ")
        if opcion == "1":
            consulta()
        elif opcion == "2":
            consulta2()
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Por favor intente de nuevo.")
def consulta():
    intentos = 3
    while intentos > 0:
        usuario = input("Usuario: ")
        contrasena = input("Contraseña: ")
        if usuario in medicos and medicos[usuario] == contrasena:
            print("Bienvenido, Médico Veterinario.")
            while True:
                print("Menú de opciones:")
                print("1. Ingresar Mascota al Registro")
                print("2. Ingresar registro de última vacunación")
                print("3. Ingresar estado de Extraviado")
                print("4. Consultar Información")
                print("5. Salir")
                opcion = input("Seleccione una opción (1/2/3/4/5): ")
                if opcion == "1":
                    ingresar_mascota()
                elif opcion == "2":
                    ingresar_ultima_vacuna()
                elif opcion == "3":
                    ingresar_estado_extraviado()
                elif opcion == "4":
                    consultar_informacion()
                elif opcion == "5":
                    break
                else:
                    print("Opción no válida. Intente de nuevo.")
        else:
            intentos -= 1
            if intentos > 0:
                print("Usuario o contraseña incorrectos. Intente de nuevo.")
            else:
                print("Número máximo de intentos alcanzado. Adiós.")


def ingresar_mascota():
    nombre = input("Nombre de su Mascota: ")
    numero_chip = input("Número del chip de su Mascota: ")
    tutor = input("Nombre del Tutor: ")
    fecha_ultima_vacuna = input("Fecha última vacuna (dia-mes-ano): ")

    mascotas[numero_chip] = {
        "nombre": nombre,
        "tutor": tutor,
        "fecha_ultima_vacuna": fecha_ultima_vacuna,
        "extraviada": False
    }
    print("Su mascota ha sido registrada con éxito.")


def ingresar_ultima_vacuna():
    numero_chip = input("Número del chip de su Mascota: ")
    if numero_chip in mascotas:
        fecha_ultima_vacuna = input("Nueva fecha de última vacuna (dia-mes-ano): ")
        mascotas[numero_chip]["fecha_ultima_vacuna"] = fecha_ultima_vacuna
        print("Fecha de la última vacuna actualizada.")
    else:
        print("Mascota no encontrada en el registro.")


def ingresar_estado_extraviado():
    numero_chip = input("Número de chip de la Mascota: ")
    if numero_chip in mascotas:
        confirmacion = input("¿Confirmar extraviado? (S/N): ")
        if confirmacion.lower() == "s":
            mascotas[numero_chip]["extraviada"] = True
            print("Mascota marcada como extraviada.")
    else:
        print("Mascota no encontrada en el registro.")

def consulta2():
            intents = 3
            while intents > 0:
                usuario = input("Usuario: ")
                contrasena = input("Contraseña: ")
                if usuario in medicos and medicos[usuario] == contrasena:
                    print("Bienvenido, Médico Veterinario.")
                    while True:
                        print("1. Consultar Información")
                        print("2. Salir")
                        opcion = input("Seleccione una opción (1/2): ")
                        if opcion == "1":
                            consultar_informacion()
                        elif opcion == "2":
                            break
                        else:
                            print("Opción no válida. Intente de nuevo.")
                else:
                    intents -= 1
                    if intents > 0:
                        print("Usuario o contraseña incorrectos. Intente de nuevo.")
                    else:
                        print("Número máximo de intentos alcanzado. Adiós.")


if __name__ != "__main__":
    pass
else:
    print("Bienvenido al sistema de registro y consulta de mascotas.")
    main()
