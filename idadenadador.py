idade_nadador = int(input("Informe a idade do nadador: "))

# OPERADORES RELACIONAIS
# > maior  >= maior ou igual  < menor  <= menor ou igual  == igual(comparação)  != diferente

# OPERADORES LOGICOS
# and (e -> &&)
# or (ou -> ||)
# not (não -> !) 

if idade_nadador >= 5 and idade_nadador <= 7:
    print ('Categoria Infantil A = 5 até 7 anos')
elif idade_nadador >= 8 and idade_nadador <= 10:
    print ('Categoria Infantil B = 8 até 10 anos')
elif idade_nadador >= 11 and idade_nadador <= 13:
    print ('Categoria Juvenil A = 11 até 13 anos')
elif idade_nadador >= 14 and idade_nadador <= 17:
    print ('Categoria Juvenil B = 14 até 17 anos')
elif idade_nadador >= 18:
    print('Adulto = maiores de 18 anos')
else:
    print('Categoria Invalidada.')        
