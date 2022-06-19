def empty_lines(name_file):
    n =0
    with open(name_file, 'r') as archivo:
        for linea in archivo:
            if linea == "":
                n = n+1
    return n

def total_lines(name_file):
    try:
        with open(name_file, 'r') as archivo:
            contenido = archivo.read()        #Tambien se pudo hacer con readlines() pero consume mas memoria
            lista = contenido.split("\n")
            return len(lista)
    except FileNotFoundError as error:
        print(error,"--> Su archivo no es '.py' o no existe, intentelo de nuevo")
        return total_lines(name_file)

nombre_archivo = input("Ingrese la ruta de su archivo en python: ")

rpta = total_lines(nombre_archivo)
print(empty_lines(nombre_archivo))
print (rpta)