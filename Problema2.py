import requests

url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
response = requests.get(url)
data = response.json()

#print(data) :Se muestra el diccionario con la informacion 
#print(type(data)) : Efectivamente es un dato del tipo dict

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

search_key = data['bpi'] #Buscamos el valor dentro de la llave 'bpi'
#Para USD
find_USD = search_key['USD']  #El valor dentro de la llave 'bpi' es un diccionario, ahi buscamos el valor de la llave 'USD'
cost_bitcoin_USD = find_USD['rate_float'] #El valor de 'USD' es otro diccionario, finalment buscamos el valor de 'rate_float'
#Para GBP
find_GBP = search_key['GBP']
cost_bitcoin_GBP = find_GBP['rate_float']
#Para EUR
find_EUR = search_key['EUR']
cost_bitcoin_EUR = find_EUR['rate_float']

bitcoins = get_num("Ingrese la cantidad de bitcoins que posee: ")
#print(search_key,'\n')
#print(find_USD,'\n')
print(f"1 bitcoin = {cost_bitcoin_USD} USD")
print(f"1 bitcoin = {cost_bitcoin_GBP} GBP")
print(f"1 bitcoin = {cost_bitcoin_EUR} EUR\n")

price_USD = bitcoins*cost_bitcoin_USD
price_GBP = bitcoins*cost_bitcoin_GBP
price_EUR = bitcoins*cost_bitcoin_EUR

print(f"El costo actual de {bitcoins} bitcoins en USD es {price_USD:.4f}")
print(f"El costo actual de {bitcoins} bitcoins en GBP es {price_GBP:.4f}")
print(f"El costo actual de {bitcoins} bitcoins en EUR es {price_EUR:.4f}")