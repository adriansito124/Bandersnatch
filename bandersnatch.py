import random

vida = 0
força = 1
agil = 1
smart = 1
moska = 5

def doiscaminho():
    print('|  |        |  |')
    print('|  |        |  |')
    print('|  |        |  |')
    print('|   |______|   |')
    print(' |            |')
    print('  |__ -0-  __|')
    print('    |_    _| ')
    print('      |  |')
    
   
def trescaminho():
    print('|  |  |   |  |  |')
    print('|  |  |   |  |  |')
    print('|  |  |   |  |  |')
    print('|   ||     ||   |')
    print(' |             |')
    print('  |_    -0-   |')
    print('    |_      _| ')
    print('      |    |')


while True:
    while True:
        try:
            classe = int(input('Escolha uma classe:\n1-Mago\n2-Guerreiro\n3-Arqueiro\nQualquer outro numero para sair...\n\n-->'))
            break
        except ValueError:
            print('INSIRA UM NUMERO!\n')

    if classe == 1:
        força = 0
        vida = 18
        smart = 3
        break
    elif classe == 2:
        força = 2
        agil = 2
        smart = 0
        vida = 22
        break
    elif classe == 3:
        agil = 3
        vida = 21
        break
    else:
        break

print('Você é um aventureiro e decide entrar dentro de uma dungeon, tem dois caminhos a frente qual você escolhe?')

doiscaminho()

escolha = int(input('\n1->Esquerda\n2->Direita\n-->'))

if escolha == 1:
    print('Enquanto você caminha para o caminho da esquerda você observa no escuro uma criatura, o que você faz?')
    mosca = int(input('\n1->Atacar\n2->Conversar\n3->Esconder\n-->'))
else:
    print('Indo para a direita, você observa de longe um objeto, o que você faz?')
    bau = int(input('\n1->Atacar\n4->Fugir\n-->'))

if mosca == 1:
    while True:
        atk = int(input('1->Magia\n2->Faca\n3->Flecha\n\n-->'))
        if atk == 1 and smart > 0 and vida>0 and moska > 0:
            dano = random.randint(1, 5)
            moska = moska - dano
            print(f'Ataque bem sucedido! Vida restante da criatura: {moska}')
            if moska <= 0:
                print('você matou a criatura!')
                break
            else:
                print('A criatura foi atingida, mas está indo te atacar!')
                dano = random.randint(0, 3)
                vida = vida - dano
                print(f'A criatura tirou {dano} pontos de vida! Vida atual {vida}')
        elif atk == 2 and força > 0 and vida>0 and moska > 0:
            dano = random.randint(1, 5)
            moska = moska - dano
            print(f'Ataque bem sucedido! Vida restante da criatura: {moska}')
            if moska <= 0:
                print('você matou a criatura!')
                break
            else:
                print('A criatura foi atingida, mas está indo te atacar!')
                dano = random.randint(0, 3)
                vida = vida - dano
                print(f'A criatura tirou {dano} pontos de vida! Vida atual {vida}')
        elif atk == 3 and agil > 0 and vida>0 and moska > 0:
            dano = random.randint(1, 5)
            moska = moska - dano
            print(f'Ataque bem sucedido! Vida restante da criatura: {moska}')
            if moska <= 0:
                print('você matou a criatura!')
                break
            else:
                print('A criatura foi atingida, mas está indo te atacar!')
                dano = random.randint(0, 3)
                vida = vida - dano
                print(f'A criatura tirou {dano} pontos de vida! Vida atual {vida}')
        elif vida <= 0:
            print('Você morreu..')
            break
        elif vida > 0:
            print('A criatura está indo te atacar!')
            dano = random.randint(0, 3)
            vida = vida - dano
            print(f'A criatura tirou {dano} pontos de vida! Vida atual {vida}')







