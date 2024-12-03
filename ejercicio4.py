def calcularinversion(DineroInvertido,InteresAnual,Años):
    TotalObtenido = DineroInvertido *(1 + InteresAnual)**Años
    return TotalObtenido
DineroInvertido = float(input("cuanto quieres invertir"))
InteresAnual = float(input("interes a aplicar")) /100 
Años=int(input("cantidad de años que deseas tratar"))
TotalObtenido =calcularinversion
print(f"el capital obtenido tras{Años} años es igual a {TotalObtenido}")
