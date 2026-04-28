#comando utilizado para laços de repetição, conhecido também como "loop", se a condição da estrutura while já for falsa desde o início, o bloco de comandos associado a ela nunca é executado.
#o comando "while True:" é utilizado para criar um laço infinito.
while True:
    valor=int(input("Digite 1 ou 0 para encerrar:"))
    if valor ==1:
        print("Valor Correto")
    else:
        print("Valor para Encerrar")
        break