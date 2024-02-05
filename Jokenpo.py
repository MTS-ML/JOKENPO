from random import randint


def menu(texto):
    #  APRESENTAÇÃO
    linha()
    print(f'{texto_colorido(texto, "azul_piscina").center(43)}')
    linha()
    print(f'[0] - PEDRA\n'
          '[1] - PAPEL\n'
          '[2] - TESOURA')
    linha()


def placar(texto):
    print(f'{"-" * 20}\n{texto.center(30)}\n{"-" * 20}')


def linha():
    print('-' * 35)


def rodada(humano: int, maquina: int):
    if humano == maquina:
        print(f'{texto_colorido("Empate!", "amarelo")}')
        return 'Empate'
    elif (humano == 0 and maquina == 2) or (humano == 1 and maquina == 0) or (humano == 2 and maquina == 1):
        print(f'{texto_colorido("Usuário venceu", "verde")}')
        return 'Vitoria'
    else:
        print(f'{texto_colorido("Computador venceu", "vermelho")}')
        linha()
        return 'Derrota'


def texto_colorido(texto, cor):
    cores = {
        'amarelo': '\033[33m',
        'verde': '\033[32m',
        'vermelho': '\033[31m',
        'azul_piscina': '\033[36m',
        'roxo': '\033[35m',

        'reset': '\033[0m'
    }

    return f"{cores[cor]}{texto}{cores['reset']}"


lista = ['PEDRA', 'PAPEL', 'TESOURA']
vitorias = derrotas = empates = rodadas = 0

while True:
    # VERIFICA SE NÚMERO ESTÁ ENTRE 0 - 2 E PARA OUTROS ERROS NA HORA DA ENTRADA
    while True:
        try:
            menu('JOKENPO')
            user = int(input('Opção: '))
            if user > 2 or user < 0:
                print(f'{texto_colorido("ERRO!", "vermelho")} Digite um número entre 0 - 2')
            else:
                break
        except:
            print(f'{texto_colorido("ERRO!", "vermelho")} Digite um número entre 0 - 2')

    pc = randint(0, 2)
    print(f'Usuário escolheu {texto_colorido(lista[user], "azul_piscina")}')
    print(f'Computador escolheu {texto_colorido(lista[pc], "azul_piscina")}')
    linha()

    resultado = rodada(user, pc)
    if resultado == 'Vitoria':
        vitorias += 1
    elif resultado == 'Derrota':
        derrotas += 1
    else:
        empates += 1

    rodadas += 1

    #  VERIFICAÇÃO
    while True:
        verificacao = input('Deseja continuar? [S/N]: ').upper().strip()
        if verificacao == 'S' or verificacao == 'N':
            break
        else:
            print('Digite apenas S ou N')
    if verificacao == 'N':
        placar(texto_colorido("PLACAR", "azul_piscina"))
        print(f'{texto_colorido("VITÓRIAS", "verde")}: {vitorias}\n'
              f'{texto_colorido("DERROTAS", "vermelho")}: {derrotas}\n'
              f'{texto_colorido("EMPATES", "amarelo")}: {empates}\n'
              f'\n{texto_colorido("RODADAS", "roxo")}: {rodadas}\n')
        break
