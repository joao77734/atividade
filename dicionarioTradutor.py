tradutor = {}
tradutor ["pineapple"] = 'abacaxi'
tradutor ["apple"] = 'maçã'
tradutor ["orange"] = 'laranja'
print(type(tradutor))
print(tradutor)
tradutor1 = {}
tradutor1 = {"pineapple":"abacaxi","apple":"maçã","orange":"laranja"}
print(tradutor1)
del (tradutor1['apple'])
print(tradutor1)
print(tradutor1.pop('banana','Fruta não encontrada'))
print("pineapple" in tradutor1)
#comando clear é usado para limpar o dicionário
tradutor1.clear()