def CalcularCalificacion():

    Nombre = input("Ingrese su nombre")
    Asignatura = input("Ingrese la asignatura ")

    Nota1 = float(input("Ingrese la nota del primer examen (0-5): "))
    while Nota1 < 0 or Nota1 > 5:
        print("La nota debe estar entre 0 y 5.")
        Nota1 = float(input("Ingrese la nota del primer examen (0-5): "))

    Nota2 = float(input("Ingrese la nota del segundo examen (0-5): "))
    while Nota2 < 0 or Nota2 > 5:
        print("La nota debe estar entre 0 y 5.")
        Nota2 = float(input("Ingrese la nota del segundo examen (0-5): "))

    Nota3 = float(input("Ingrese la nota del tercer examen (0-5): "))
    while Nota3 < 0 or Nota3 > 5:
        print("La nota debe estar entre 0 y 5.")
        Nota3 = float(input("Ingrese la nota del tercer examen (0-5): "))

    CalificacionFinal = (Nota1 * 0.3) + (Nota2 * 0.3) + (Nota3 * 0.4)


    if CalificacionFinal >= 4.0:
        aprobado = "APROBADO"
    else:
        aprobado = "REPROBADO"

    # Mostrar resultados
    print(f"\nResultados para {Nombre} en la asignatura {Asignatura}:")
    print(f"Calificación final: {CalificacionFinal:.2f}")
    print(f"Estado: {aprobado}")

CalcularCalificacion()