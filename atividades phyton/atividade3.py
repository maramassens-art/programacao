contador = 1
while contador <= 4:
    nota = float(input("Insira a nota do {contador} aluno"))
    if nota < 0 or nota > 18:
       print("nota inválida . a nota deve estar entre 0 e 10")
       continue
    somas_notas += nota
    contador +=1
media = soma_notas/4
print("A média das 4 notas é: ",media)
,





