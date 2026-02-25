#entrada
dias_totais = int(input("Digite o total de dias sem acidentes: "))

#processo (30 dias/mes e 365 dias/anos)
anos = dias_totais // 365
resto_dias = dias_totais % 365
meses = resto_dias // 30
dias = resto_dias % 30
print(f"{anos} ano(s), {meses} mes(es) e {dias} dia(s).")
