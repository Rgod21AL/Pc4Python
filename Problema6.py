import re  #Libreria necesaria

main_chain = '@robot9! @robot4& I have a good feeling that the show is going to be amazing! @robot9$ @robot7%'

#Ahora buscamos una expresion que tenga este patron --> @robot<digito><signo especial:

wanted_chain = r"@robot\d\W"

lista = re.findall(wanted_chain, main_chain) 

print("\nLista buscada =",lista)

#--------------------------------------------------------
#APUNTES ADICIONALES

found = re.search('robot', main_chain) #Verifica que el string 'robot' esta contenido en la cadena

print("\nEl string 'robot' se encuentra en la cadena?")
if found:
    print("'Robot' was found !!")
else: 
    print("We couldn't find 'robot' ")

list = re.findall('robot', main_chain) #Este metodo findall, devuelve una lista

print(f"\nSe encontraron {len(list)} strings 'robot'")

search = input("\nIngrese la cadena que desea buscar: ")

cadena = re.search(search, main_chain)

if cadena:
    print(f"{search} was found !!")
else:
    print(f"We couldn't find the expresion '{search}'")
