import re

card_list = []

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

cant_tarjetas = get_num("Ingrese la cantidad de tarjetas que se van a verificar: ")

for i in range(1,cant_tarjetas+1):
    credit_card = (input(f"Usuario [{i}] Numero de tarjeta: "))
    card_list.append(credit_card)
#print(card_list)
for tarjetas in card_list:
    model = r'[4-6]\d{3}-?\d{4}-?\d{4}-?\d{4}'
    if re.search(model, tarjetas):
        print(tarjetas,'---> VALID')
    else:
        print(tarjetas,'---> INVALID')
         




