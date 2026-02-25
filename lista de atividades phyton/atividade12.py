#valorsalário
salário = float(input("Digite o salário inicial: "))
x = salário * 0.15
aumento = salário + x
imposto = aumento * 0.08
salariofinal = aumento - imposto
print("o salario sem aumento era : ",salário)
print("o salario com aumento ficou : ",aumento)
print("o salario final ficou de : ",salariofinal)

