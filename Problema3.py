from pyfiglet import Figlet
import random

figlet = Figlet()

list_fuentes = figlet.getFonts()

print("LISTA DE FUENTES")
print(list_fuentes)

text = input("\nIngrese su texto: ")

def get_font():
    while True:   #Para pedirle al usuario que ingrese los correos que él requiera
        rpta = input("\nDesea ingresar una fuente? [si/no]: ")
        if rpta == 'Si' or rpta == 'si':
            font = input("\nIngrese la fuente que desea: ")
            while True:
                if list_fuentes.count(font) == 0:
                    print("Su fuente no existe, intentelo de nuevo")
                    font = input("Ingrese la fuente que desea: ")
                else:
                    break
            break
        elif rpta == 'No' or rpta == 'no':
            font = random.choice(list_fuentes)
            break
        else:
            print("Opcion no valida, intentelo de nuevo")
    return font

fuente = get_font()

figlet.setFont(font=fuente) #Para el fondo 

print(f"\nSu texto en la fuente '{fuente}' es: ")
print(figlet.renderText(text)) #Imprimimos el texto