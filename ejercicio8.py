Usuario = input("digite su usuario")
Edad =int(input("digite su edad"))
Sexo =input("digite el sexo tal como (Hombre / Mujer)")
if Edad >= 63:
    if Sexo == 'Hombre':
        print("se puede jubilar")
    else:
        print("aun no se puede jubilar")
elif Edad >= 54:
    if Sexo == 'Mujer':
        print("se puede jubilar")
else:
    print("un no se puede jubilar")