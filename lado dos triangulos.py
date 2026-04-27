ld1 = (input("Digite o primeiro lado do triângulo: "))
ld2 = (input("Digite o segundo lado do triângulo: "))
ld3 = (input("Digite o terceiro lado do triângulo: "))
if ld1 == ld2 and ld2 == ld3:
    print ("Triângulo Equilátero")
elif ld1== ld2 or ld2== ld3 or ld3 == ld1:
    print ("Triângulo Isóceles")
else:
    print ("Triângulo Escaleno")