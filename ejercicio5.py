Nota = int(input("ingrese la cantidad de notas del estudiante"))
Suma = 0
i = 1
while (i <= Nota):
    print("ingrese la nota" , i)
    nota=float(input())
    Suma=Suma + nota
    i+=1
    prom = Suma / Nota
    print(f"el promedio de las notas es{prom}")
    if prom >= 4.5 :
        print("aprobado") 
    else:
        print( "no aprobado")
        


    
