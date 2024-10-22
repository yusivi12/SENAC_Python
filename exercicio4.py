F = float(input('Temperatura em F:'))

C = 5 * (F - 32) / 9

print('''{:.2f} F
      equivalem a {:.2f}°C'''.format(F, C))