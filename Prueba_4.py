def comprar_entrada_fortificados(compradores_fortificados, stock_fortificados):
    if stock_fortificados <= 0:
        print("No hay entradas disponibles para “los Fortificados”.")
        return stock_fortificados
    nombre = input("Ingrese nombre de comprador: ").strip()
    if nombre in compradores_fortificados:
        print("Nombre de comprador ya registrado. Intente con otro nombre.")
        return stock_fortificados
    tipo = input("Ingrese tipo de entrada (G/V): ").strip().upper()
    if tipo not in ("G", "V"):
        print("Tipo de entrada no válido. Intente otra vez.")
        return stock_fortificados
    while True:
        codigo = input("Ingrese código de confirmación: ").strip()
        if (len(codigo) >= 6 and
            any(c.isupper() for c in codigo) and
            any(c.isdigit() for c in codigo) and
            " " not in codigo):
            print("Código validado.")
            break
        else:
            print("Código no válido. Intente otra vez.")
    compradores_fortificados.add(nombre)
    stock_fortificados -= 1
    print("¡Entrada registrada con éxito para “los Fortificados”!")
    return stock_fortificados

def comprar_entrada_iluminados(compradores_iluminados, stock_iluminados):
    if stock_iluminados <= 0:
        print("No hay entradas disponibles para “los Iluminados”.")
        return stock_iluminados
    nombre = input("Ingrese nombre de comprador: ").strip()
    if nombre in compradores_iluminados:
        print("Nombre de comprador ya registrado. Intente con otro nombre.")
        return stock_iluminados
    tipo = input("Ingrese tipo de entrada (CV/PAL): ").strip().upper()
    if tipo not in ("CV", "PAL"):
        print("Tipo de entrada no válido. Intente otra vez.")
        return stock_iluminados
    while True:
        codigo = input("Ingrese código de confirmación: ").strip()
        if (len(codigo) >= 5 and
            sum(1 for c in codigo if c.isupper()) >= 3 and
            any(c.isdigit() for c in codigo) and
            " " not in codigo):
            print("Código validado.")
            break
        else:
            print("Código no válido. Intente otra vez.")
    compradores_iluminados.add(nombre)
    stock_iluminados -= 1
    print("¡Entrada registrada con éxito para “los Iluminados”!")
    return stock_iluminados

def mostrar_stock(stock_fortificados, stock_iluminados):
    print(f"Entradas disponibles para “los Fortificados”: {stock_fortificados}")
    print(f"Entradas disponibles para “los Iluminados”:   {stock_iluminados}")

def menu():
    compradores_fortificados = set()
    compradores_iluminados = set()
    stock_fortificados = 500
    stock_iluminados = 500

    while True:
        print("\nTOTEM AUTOSERVICIO CONCIERTOS ROCK AND CHILE")
        print("1.- Comprar entrada a “los Fortificados”.")
        print("2.- Comprar entrada a “los Iluminados”.")
        print("3.- Stock de entradas para ambos conciertos.")
        print("4.- Salir.")
        opcion = input("Ingrese opción: ").strip()

        if opcion == "1":
            stock_fortificados = comprar_entrada_fortificados(compradores_fortificados, stock_fortificados)
        elif opcion == "2":
            stock_iluminados = comprar_entrada_iluminados(compradores_iluminados, stock_iluminados)
        elif opcion == "3":
            mostrar_stock(stock_fortificados, stock_iluminados)
        elif opcion == "4":
            print("Programa terminado...")
            break
        else:
            print("Debe ingresar una opción válida!!")

if __name__ == "__main__":
    menu()