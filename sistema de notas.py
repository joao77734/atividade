n1= float(input("Digite a 1° Nota Parcial: "))
n2= float(input("Digite a 2° Parcial: "))

media = (n1 + n2) / 2
print (media)

if media >= 7.0 and media == 9:
    print (f"Média: {media}  ->>> Aprovado!")
elif media == 10:
    print (f"Média: {media} ->>> Aprovado com Distinção!")
else:
    print (f"Média: {media}  ->>> Reprovado!")