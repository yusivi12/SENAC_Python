# Agora eu quero 10 numeros inteiros e imprimir a soma
soma = 0
for i in range(10):
    print(i)
    j = i + i
    numero = int(input(f'Informe o {j}° número: '))
    soma += numero
    print(f'A soma é {soma}')             
                 