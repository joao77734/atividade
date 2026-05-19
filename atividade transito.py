codigo_cidade = []
nome_cidade = []
nome_estado = []
numero_veiculos =  []
numero_acidentes_com = []
numeros_acidentes_sem = []
condutor_embrigado = []

codigo_cidade2 = str (input("Digite o código da cidade: "))
nome_cidade2 = str (input("Digite o nome da Cidade: "))
nome_estado2 = str (input("Digite o nome do Estado: "))
numero_veiculos2 = str (input("Digite o número de veículos: "))
numero_acidentes_com2 = str (input("Digite o número de acidentes com vítimas: "))
numeros_acidentes_sem2 = str (input("Digite o número de acidentes sem vítimas: "))
condutor_embrigado2 = str (input("Digite se o condutor estava embrigado ou não: "))

codigo_cidade.append(codigo_cidade2)
nome_cidade.append(nome_cidade2)
nome_estado.append(nome_estado2)
numero_veiculos.append(numero_veiculos2)
numero_acidentes_com.append(numero_acidentes_com2)
numeros_acidentes_sem.append(numeros_acidentes_sem2)
condutor_embrigado.append(condutor_embrigado2)

maior=max(numero_acidentes_com)
indice_maior = numero_acidentes_com.index(maior)

menor=min(numero_acidentes_com)
indice_menor = numero_acidentes_com.index(menor)

print("Maior índice de acidentes de trânsito:",maior)
print("Cidade:",nome_cidade[indice_maior])
print("Estado:",nome_estado[indice_maior])
print()
print("Menor índice de acidentes de trânsito:", menor)
print("Cidade:",nome_cidade[indice_menor])
print("Estado:",nome_estado[indice_menor])

