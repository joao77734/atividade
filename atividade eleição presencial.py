voto_c1 = 0
voto_c2 = 0
voto_c3 = 0
voto_c4 = 0
votos_nulos = 0
votos_brancos = 0
total_votos= 0

while True:
    voto = input("Digite o voto (1-4), Enter para voto em branco e qualquer número para nulo. ")
    if voto == "0":
        break

    if voto =="":
        votos_brancos +=1
    elif voto.isdigit():
        voto = int(voto)

    
    if voto == 1:
        voto_c1 += 1
    elif voto ==2:
        voto_c2 += 1
    elif voto ==3:
        voto_c3 += 1
    elif voto ==4:
        voto_c3 += 1
    else:
        votos_nulos += 1
    
    total_votos += 1

ganhador = "Candidato 1"
maior = voto_c1

if voto_c2 > maior:
    maior = voto_c2
    ganhador = "Candidato 2"

if voto_c3 > maior:
    maior = voto_c3
    ganhador = "Candidato 3"

if voto_c4 > maior:
    maior = voto_c4
    ganhador = "Candidato 4"

print("\n Resultado da Eleição: ")
print ("\n Votos Candidato 1: ", voto_c1)
print ("\n Votos Candidato 2: ", voto_c2)
print ("\n Votos Candidato 3: ", voto_c3)
print ("\n Votos Candidato 4: ", voto_c4)
print ("\n Votos nulos: ", votos_nulos)
print ("\n Votos em Branco: ", votos_brancos)
print ("\n Total de Votos: ", total_votos)
print("Ganhador: ", ganhador)