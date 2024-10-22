anonasc = int(input("Ano nascimento: "))
anoatual = int(input("Ano atual: "))

idadeAnos = anoatual - anonasc
idadeMeses = idadeAnos * 12
idadeDias = idadeAnos * 365

idadeDias2 = idadeMeses * 30

print(f"""Idade em anos: {idadeAnos}
    Idade em meses: {idadeMeses}
    Idade em dias: {idadeDias}""")