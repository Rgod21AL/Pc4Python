import random

def get_num(msg: str)->int:
    "Solicita un número entero positivo y verifica que sea valido"
    try:
        x = int(input(msg))
        if x>0:
            return x
        else:
            return get_num("SOLO SE PERMITEN ENTEROS POSITIVOS, intentelo de nuevo: ")
    except:
        return get_num("ERROR!! Comando no valido, intentelo de nuevo: ")

nivel = get_num("Ingrese el nivel que desea jugar: ")
num_aleatorio = random.randint(1,nivel)
print(f"\t  ADIVINA EL NUMERO QUE SE OBTUVO DEL 1 al {nivel}")
print("\t----------------------------------------------")

while True:
    num_ingresado = get_num("Ingrese un numero: ")
    if num_ingresado > nivel:
        print(f"No se permiten numeros mayores a {nivel}, intentelo otra vez")
    elif num_aleatorio < num_ingresado:
        print("¡Te pasaste!")
    elif num_aleatorio > num_ingresado:
        print("¡Demasiado pequeño!")
    elif num_aleatorio == num_ingresado:
        print("¡Adivinaste!")
        break