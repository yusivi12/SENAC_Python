altura = float(input("Informe sua altura: "))
sexo = input("Informe seu Sexo: ")
peso = 0

# OPERADORES RELACIONAIS
# > maior  >= maior ou igual  < menor  <= menor ou igual  == igual(comparação)  != diferente

# OPERADORES LOGICOS
# and (e -> &&)
# or (ou -> ||)
# not (não -> !) 

if sexo == 'm' or sexo == 'M':
    peso = (72.7 * altura) - 58
elif sexo == 'f' or sexo == 'F':
    peso = (62.1 * altura) - 44.7
else:
    print("Sexo inválido")    
print(f"seu peso ideal é {peso:.3f}")

