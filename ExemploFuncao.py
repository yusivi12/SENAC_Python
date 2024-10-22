from Funcoes import relatorio

produtos = []

def incluir():
    print("Acessando a função incluir")
    while True:
        nome = input("Nome do produto: ")
        preco = float(input("Preço: "))
        cat = input("Categoria: ")
        p = {}
        p['nomeprod'] = nome
        p['precoprod'] = preco
        p['catprod'] = cat
        produtos.append(p)
        r = input("Deseja continuar? ")
        if r == 'n' or r == 'N':
            break
while True:
    print("Menu")
    print("1 - Cadastro")
    print("2 - Relarório")
    print("0 - Sair")
    op = int(input("Informe opção: "))
    if op == 0:
        break
    elif op ==1:
        incluir()
    elif op == 2:
        relatorio()