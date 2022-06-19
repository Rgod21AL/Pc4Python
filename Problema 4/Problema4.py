
msg = """\tBIENVENIDO A SU MENU DE OPCIONES
[1]. Crear tablas de multiplicar
[2]. Leer tablas ingresadas
[3]. Mostrar una producto de las tablas
[4]. SALIR
Opcion: """

def get_num(msg: str)->int:
    "Solicita un número entero positivo y verifica que sea valido"
    try:
        x = int(input(msg))
        if x>=0 and x<=12:
            return x
        else:
            return get_num("Solo se permiten enteros positivos menores o iguales a 12, intentelo de nuevo: ")
    except:
        return get_num("ERROR!! Comando no valido, intentelo de nuevo: ")

def create_files(num: int):
    "Crea los ficheros de las tablas de multiplicar"
    with open(f'tabla del {num}.txt', 'w') as f:
        for i in range(1,13):
            productos = f'{i} x {num} = {num*i}\n'
            f.write(productos)
        pass

def show_files(num: int):
    "Muestra los ficheros en pantalla"
    try:                                                     #OTRA OPCION:
        with open(f'tabla del {num}.txt', 'r') as tabla:     #archivo = open(f'tabla del {num1}.txt', 'r')
            contenido = tabla.read()                         #tabla = archivo.read()
            print(f"\tTABLA DEL {num}")                      #archivo.close()
            print(contenido)                                 #print(tabla)
            pass
    except FileNotFoundError as e:
        print(e, "--> Archivo no encontrado")

def find_lines(num1: int, num2: int):
    try:
        archivo = open(f'tabla del {num1}.txt', 'r')
        lineas = archivo.readlines() #Al usar este metodo, las lineas se devuelven en una LISTA
        archivo.close()
        print(lineas[num2-1])
    except FileNotFoundError as e:
        print(e, "--> Archivo no encontrado")

while True:
    opcion = input(msg)
    if opcion == '1':
        numero = get_num("Ingrese un numero [1-12]: ")
        create_files(numero)
    elif opcion == '2':
        numero = get_num("Ingrese la tabla de multiplicar que desea ver: ")
        show_files(numero)
    elif opcion == '3':
        n1 = get_num("Ingrese la tabla de multiplicar que desea ver: ")
        n2 = get_num("Numero de linea que desea ver: ")
        find_lines(n1, n2)
    elif opcion == '4':
        print("Gracias por usar nuestro programa, vuelva pronto!!")
        break
    else:
        print("Opcion no valida, intentelo de nuevo")
