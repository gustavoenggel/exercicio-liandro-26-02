import random as r

numeros = []

def header():
    mensagem = "menu"
    tam = len(mensagem)
    print("="*(tam*2))
    print(mensagem.center(tam*2))
    print("="*(tam*2))


def escolher():
    escolha = int(input('Insira 1 para Sortear.\nInsira 2 para mostrar ultimo sorteio\nInsira 3 para sair. '))
    while True:
        if escolha == 1:
            quantidade = escolher_sorteio()
            sortear(quantidade)
            break

        elif escolha == 2:
            if len(numeros) > 0:
                print("Último sorteio:", sorted(numeros))
                break
            else:
                print('Sua lista esta vazia')
                break
        elif escolha == 3:
            print("Saindo...")
            break





def escolher_sorteio():
    while True:
        try:
            sorteio = int(input('Insira quantos numeros você deseja sortear: '))
        except ValueError:
            print('Insira apenas numeros inteiros.')
            continue

        if sorteio > 100:
            print('Insira um numero abaixo de 100!')
        elif sorteio <= 0:
            print('Insira um numero maior que zero!')
        else:
            return sorteio


def sortear(quantidade):
    for i in range(quantidade):
        numero = r.randint(1, 100)
        numeros.append(numero)
    print(sorted(numeros))

header()
escolher()

