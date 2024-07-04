from tabulate import tabulate

def obtener_datos_personales():
    while True:
        try:
            tot = int(input("¿Cuántas personas quiere mostrar en la tabla? "))
            if tot > 0 and tot < 10:
                break
            else:
                print("Por favor, ingrese un número mayor que 0 y menor que 10.")
        except ValueError:
            print("Por favor, ingrese un número entero.")

    lst_dic_personas = []

    for i in range(tot):
        print(f"Datos para la persona {i + 1} de {tot}:")
        nombre = input(f"Ingrese el nombre de la persona {i + 1}: ")
        apellido = input(f"Ingrese el apellido de la persona {i + 1}: ")
        telefono = input(f"Ingrese el número telefónico de la persona {i + 1}: ")
        
        dic_persona = {
            "Nombre"  : nombre[:20],    # Truncar a 20 caracteres si es necesario
            "Apellido": apellido[:20],  # Truncar a 20 caracteres si es necesario
            "Teléfono": telefono[:20]   # Truncar a 20 caracteres si es necesario
        }
        lst_dic_personas.append(dic_persona)

    return lst_dic_personas

def mostrar_tabla_personas(lst_dic_personas):
    print("\nDatos personales:")
    print(tabulate(lst_dic_personas, headers="keys", tablefmt="grid"))

def main():
    lst_dic_personas = obtener_datos_personales()
    mostrar_tabla_personas(lst_dic_personas)

if __name__ == "__main__":
    main()