#dia mes data
dia=int(input("digite o dia(1-30)"))
mes=int(input("digite o mes (1-12)"))
dia_passados =(mes - 1 ) * 30 + dia
print(f"ja se passaram{dia_passados}dias desde do inicio do ano.")
