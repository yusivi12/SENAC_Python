# sl = float(input('Qual seu salário? '))
valorHora = float(input('Valor hora: '))
horas = int(input('Horas trabalhadas: '))
descontos = float(input('Descontos: '))

salario = (valorHora * horas) - descontos

print(f'O salário é {salario}')
print(f'O salário é {salario:.2f}')
print('O salário é {:.2f}'.format(salario))