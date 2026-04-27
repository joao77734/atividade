def invert_texto (texto):
    texto_inverso = texto [:: -1]
    return texto_inverso
n = input ("Digite uma frase: ")

vogais = "aeiouAEIOU"
consoantes = "qwrtypsdfghjklçzxcvbnmQWRTYPSDFGHJKLÇZXCVBNM"
numeros = "0123456789"
lista_vogais = []
lista_consoantes = []
lista_numeros = []

for letra in n :
 if letra in vogais :
    lista_vogais.apend(letra)
 elif letra in consoantes :
    lista_consoantes.apend(letra)
 elif letra in numeros :
    lista_numeros.apend(letra)


print ( "A frase digitada foi >> {}".format (n))

