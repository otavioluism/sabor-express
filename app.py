import os

restaurantes = []

def exibir_nome_programa():
    print('''
    █▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
    ▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
    ''')


def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair \n')


def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opcao: '))
        print('Voce escolheu a opcao: {}'.format(opcao_escolhida))
        match opcao_escolhida:
            case 1:
                cadastrar_restaurante()
            case 2:
                listar_restaurate()
            case 3:
                print('Ativar restaurante')
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except Exception:
        opcao_invalida()


def opcao_invalida():
    print('Opcao Invalida')
    voltar_menu_principal()


def finalizar_app():
    exibir_subtitulo('Finalizando app!')

def cadastrar_restaurante():
    os.system('clear')
    restaurante_escolhido = input('Digite o nome do restaurante... ')
    restaurantes.append(restaurante_escolhido)
    print('O restaurante {} foi cadastrado com sucesso'.format(restaurante_escolhido))
    voltar_menu_principal()


def exibir_subtitulo(texto):
    os.system('clear')
    print(texto)

def voltar_menu_principal():
    input('Digite qualquer tecla para voltar ao menu: ')
    main()

def listar_restaurate():
    exibir_subtitulo('Lista de restaurantes ')
    for restaurante in restaurantes:
        print('Restaurantes -> {}'.format(restaurante))
    voltar_menu_principal()

def main():
    os.system('clear')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()
