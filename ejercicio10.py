def calcularprecio(Precioinicial):
  
  if Precioinicial > 20000:
    Descuento = Precioinicial * 0.2  
    Preciofinal = Precioinicial - Descuento
  else:
    Preciofinal = Precioinicial

  return Preciofinal

precio = float(input("Ingrese el precio del producto: "))

Preciopagar = calcularprecio(precio)

print(f"El precio final a pagar es: ${Preciopagar:.2f}")