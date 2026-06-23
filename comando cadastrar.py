def cadastro():
    name = input("Qual seu nome:")
    age = input("Idade: ")
    return name,age
print("Iniciando cadastro...")
nome,idade = cadastro()
print("Cadastro realizado com sucesso")
print("Seu nome é ",nome, "e você tem ",idade,"anos de idade.")
#sistema muito simplificado de cadastro