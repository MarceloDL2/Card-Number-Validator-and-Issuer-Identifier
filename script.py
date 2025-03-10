def luhn_check(numero_tarjeta):
    numero_tarjeta = [int(d) for d in str(numero_tarjeta)][::-1]
    suma = 0
    for i, digito in enumerate(numero_tarjeta):
        if i % 2 == 1:
            digito *= 2
            if digito > 9:
                digito -= 9
        suma += digito
    return suma % 10 == 0

def identificar_emisora(numero_tarjeta):
    numero_tarjeta = str(numero_tarjeta)
    if numero_tarjeta.startswith(('34', '37')):
        return "American Express"
    elif numero_tarjeta.startswith(('4')):
        return "Visa"
    elif numero_tarjeta.startswith(('51', '52', '53', '54', '55')) or numero_tarjeta.startswith(tuple(str(i) for i in range(2221, 2721))):
        return "Mastercard"
    elif numero_tarjeta.startswith(('6011', '65')) or numero_tarjeta.startswith(tuple(str(i) for i in range(644, 650))):
        return "Discover"
    elif numero_tarjeta.startswith(('36', '38', '39')):
        return "Diners Club"
    elif numero_tarjeta.startswith(('35')):
        return "JCB"
    else:
        return "Desconocida"

numero_tarjeta = input("Ingrese el número de tarjeta: ").strip()
if numero_tarjeta.isdigit():
    emisora = identificar_emisora(numero_tarjeta)
    if luhn_check(numero_tarjeta):
        print(f"El número de tarjeta es válido y pertenece a {emisora}.")
    else:
        print("El número de tarjeta no es válido.")
else:
    print("Entrada no válida. Ingrese solo números.")
