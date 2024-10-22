# Primeira forma
raio = float(input("Qual o valor de raio? "))
altura = float(input("Qual o valor da altura? "))
pi = 3.14159

volume = pi * (raio * raio) * altura

# Segunda forma
volume2 = 3.14159 * raio**2 * altura

# Terceira forma
import math

volume3 = math.pi * math.pow(raio, 2) * altura

print('O volume é {}'.format(volume))
print(f'O volume2 é {volume2}')
print(f'O volume3 é {volume3}')

