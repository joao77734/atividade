def valorPagamento(valor, dias):
    if dias == 0:
        return valor
    else:
        multa = valor * 0.03
        juros = valor * 0.01 * dias
        total = valor + multa + juros
        return total
quantidade = 0
valor_total = 0

while True:
    valor = float(input("Digite o valor da prestação: "))

    if valor == 0:
        break

    dias = int(input("Digite os dias de atraso: "))

    pagamento = valorPagamento(valor, dias)

    print("Valor a pagar: ", pagamento)

    quantidade += 1
    valor_total += pagamento

print("----- Relatório Final -----")
print("Quantidade de prestações pagas: ", quantidade)
print("Valor total recebido: R$", valor_total)