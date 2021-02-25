def linha():
    print("="*30)


linha()
print ("BEM VINDO A CALCULADORA DE PYTHON")
print("Por gentileza, escreva tudo com letra minúscula. Obrigado!")
linha()


primeiro_numero = float(input("Digite um número: "))
segundo_numero = float(input("Digite outro número: "))
pergunta = input("Qual a operação você deseja fazer? ")


multiplicacao = (primeiro_numero * segundo_numero)
divisão = (primeiro_numero / segundo_numero)
subtração = (primeiro_numero - segundo_numero)
soma = (primeiro_numero + segundo_numero)


if pergunta == "multiplicação":
    print(multiplicacao)
elif pergunta == "divisão":
    print (divisão)
elif pergunta == "subtração":
    print(subtração)
elif pergunta == "soma":
    print(soma)
else:
    print("Repita toda a operação!")

