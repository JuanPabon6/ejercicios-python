def cambiardolares(dolares):
    TasaCambio = 3934
    peso = dolares * TasaCambio
    return peso

dolares = float(input("digite la cantidad de dolares que quiere cambiar"))
peso = cambiardolares(dolares)
print(f"{dolares:.2f}dolares pasados a pesos colombianos , seria un total de {peso:,.0f}")

while True:
    try:
        
        if dolares < 0:
            print("ingrese una cantidad valida")
            continue
    except ValueError:
        print("la entrada no es valida")
        continue
    continuar =input("deseas realizar otra conversion ? (s/n):")
    if continuar != "s":
        print("el proceso ha terminado !")
        break
    elif continuar !="n":
            dolares = float(input("digite la cantidad de dolares que quiere cambiar"))
            peso = cambiardolares(dolares)
            print(f"{dolares:.2f}dolares pasados a pesos colombianos , seria un total de {peso:,.0f}")
            break






