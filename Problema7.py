import re

list_emails = []

userID = input("Ingrese el correo electronico: ")
list_emails.append(userID)

while True:   #Para pedirle al usuario que ingrese los correos que él requiera
    rpta = input("Desea añadir otro correo? [si/no]: ")
    if rpta == 'Si' or rpta == 'si':
        userID = input("Ingrese el correo electronico: ")
        list_emails.append(userID)
    elif rpta == 'No' or rpta == 'no':
        break
    else:
        print("Opcion no valida, intentelo de nuevo")

print('\nCorreos ingresados: ',list_emails,'\n')

for emails in list_emails:  #'emails' es el valor que está contenido en cada posicion de la lista
    model = r'[A-Za-z0-9\W*]+@+[\w\W]+.com'
    if re.search(model, emails):   #Si 'model' esta dentro de 'emails'...                    
        print(emails, "is a valid email address\n")
    else:
        print(emails, "is not a valid email address\n")

