# Responsável por importar comando de tempo
import time
import csv

cidades = open('distancias.csv', 'r')
cidades_csv = list(csv.reader(cidades)) #Tratamento da biblioteca CSV
cidades.close()

# Variáveis globais
custo = 0
custo_km = 0

# Responsável por printar o menu de opções
def menu():
    print('\n')
    print('\033[0;96m', 'TRANSPORTADORA LB'.center(25, '-'), '\033[0;0m\n')
    print('1 - Custo por km rodado')
    print('2 - Consultar trecho')
    print('3 - Melhor rota')
    print('4 - Rota completa')
    print('5 - Sair')
    # Responsável por solicitar a opção para o usuário e retornar a mesma quando chamar a função
    item = input('\nEscolha uma opção: ')
    return item

#FUNÇÕES - Opções do Menu
def opcao_1():
    print('''\n\033[1;94mOpção 1:
    Custo por km rodado\033[0;0m\n''')
    temp = 0

    while temp != 1:
        n = input('Informe o custo por KM rodado em Reais: R$')

        if n.isalpha():
            print('\033[1;90mInforme apenas em números!\033[0;0m\n')

        elif n.replace('.','',1).isdigit() or n.isnumeric():
            n = float(n)
            if n >= 0:
                global km_rodado
                km_rodado = n
                temp = 1

        else:
            print('\033[1;90mO valor informado é negativo!\033[0;0m')
            print('\033[1;90mFavor informe um valor positivo.\033[0;0m\n')

    return km_rodado

#FUNÇÕES - Opções do Menu
def opcao_2():
    print('''\n\033[1;94mOpção 2:
    Consulta trecho\033[0;0m''')

#FUNÇÕES - Opções do Menu
def opcao_3():
    print('''\n\033[1;94mOpção 3:
    Melhor rota\n\033[0;0m''')

#FUNÇÕES - Opções do Menu
def opcao_4():
    print('''\033[1;94mOpção 4:
    Rota completa\033[0;0m''')


#Responsável por consultar o trecho e entregar a distância entre as cidades percorridas
def consultarTrecho(ori, dest):
    origem_input = ori
    destino_input = dest

    origem_index = 1 + cidades_csv[0].index(origem_input)
    destino_index = cidades_csv[0].index(destino_input)

    distancia = int(cidades_csv[origem_index][destino_index])
    print(f'\nA distância da cidade de {origem_input} até {destino_input} é de {distancia}km.')
    return distancia

#Responsável por informar o custo total do trecho
def custoTrecho():
    custo = distancia * km_rodado
    print('Custo total do trecho: R${:.2f}'.format(custo))
    return custo

#Responsável por armazenar as informações do item 3 do menu
def historicoLog():
    registro_consultas = open('log.txt', 'a', encoding = 'utf-8')
    linha = (50 * '-')
    registro_consultas.write('\n{} >> {}:'.format(origem, destino))
    registro_consultas.write('\nDistância: {}km\nCusto total do trecho: R${:.2f}\n'.format(distancia, custo))
    registro_consultas.write(linha)
    registro_consultas.close()

#Reponsável por informar a melhor rota das cidades informadas
def melhorRota(cidades_lista):
    a = cidades_lista[0]
    b = cidades_lista[1]
    c = cidades_lista[2]

    cidade_a_index = 1 + cidades_csv[0].index(a)
    cidade_b_index = cidades_csv[0].index(b)
    distancia_ab = int(cidades_csv[cidade_a_index][cidade_b_index])
    cidade_c_index = cidades_csv[0].index(c)
    distancia_ac = int(cidades_csv[cidade_a_index][cidade_c_index])
    cidade_b2_index = 1 + cidades_csv[0].index(b)
    distancia_bc = int(cidades_csv[cidade_b2_index][cidade_c_index])

    if distancia_ab < distancia_ac:
        print('\033[1mDe: 'f'\033[0m{a}')
        print('\033[1mPara: 'f'\033[0m{b}')
        print(f'O percurso deste trajeto é mais curto e será de: {distancia_ab}km.\n')
        print('Após, você partirá: ')
        print('\033[1mDe: 'f'\033[0m{b}')
        print('\033[1mPara: 'f'\033[0m{c}')
        print(f'O percurso deste trajeto será de: {distancia_bc}km.\n')

        distancia_total = distancia_ab + distancia_bc
        print(f'Distância total percorrida: {distancia_total}km.')

    else:
        print('\033[1mDe: 'f'\033[0m{a}')
        print('\033[1mPara: 'f'\033[0m{c}')
        print(f'O percurso deste trajeto é mais curto e será de: {distancia_ac}km.\n')
        print('Após, você partirá: ')
        print('\033[1mDe: 'f'\033[0m{c}')
        print('\033[1mPara: 'f'\033[0m {b}')
        print(f'O percurso deste trajeto será de: {distancia_bc}km.\n')

        distancia_total = distancia_ac + distancia_bc
        print(f'Distância total percorrida: {distancia_total}km.')

#PROCESSAMENTO DO MENU
# Laço para chamar a função reponsavel pela escolha no menu
escolha = '0'
while(escolha != '5'):
    # Início da estrutura de condição responsável por receber a escolha do usuário no menu e dar inicio com seu devido valor
    escolha = menu()
    # Responsável por executar a opção "Custo por km rodado"
    if escolha == '1':
        custo_km = opcao_1()
        print(f'\nO custo por km rodado informado é de R${custo_km :.2f}.')

    # Responsável por executar a opção "Consultar trecho"
    elif escolha == '2':
        if custo_km <= 0:
            print('\n\033[1;101m Atenção! \033[0;0m')
            print('O custo do KM rodado não foi informado.')
            print('Favor informe antes de prosseguir para as demais opções.')
            print('\nRedirecionando para o Menu...')
            time.sleep(1)
            continue
        opcao_2()
        t1 = 1
        t2 = 1
        while t1 == t2:
            origem = input('\nInforme uma cidade de origem: ').upper()
            if origem in cidades_csv[0]:
                print('\033[0;92mCidade válida!\033[0;0m')
                while t1 == t2:
                    destino = input('\nInforme uma cidade de destino: ').upper()
                    if destino in cidades_csv[0]:
                        if origem != destino:
                            print('\033[0;92mCidade válida!\033[0;0m')
                            print('\nConsultando...')
                            time.sleep(2)
                            t2 = 2
                        else:
                            print('\033[1;90mOpção inválida, digite cidades diferentes!\033[0;0m')
                    else:
                        print('\033[1;90mOpção inválida, digite uma cidade de destino válida!\033[0;0m')
            else:
                print('\033[1;90mOpção inválida, digite uma cidade de origem válida!\033[0;0m')


        distancia = consultarTrecho(origem, destino)
        custo = custoTrecho()
        historicoLog()

    # Responsável por executar a opção "Melhor rota"
    elif escolha == '3':
        if custo_km <= 0:
            print('\n\033[1;101m Atenção! \033[0;0m')
            print('O custo do KM rodado não foi informado.')
            print('Favor informe antes de prosseguir para as demais opções.')
            print('\nRedirecionando para o Menu...')
            time.sleep(1)
            continue
        opcao_3()

        a1 = 1
        a2 = 1

        while a1 == a2:
            print('Separando por virgula')
            lista_cidades = input('Informe três cidades: ').upper().split(",")
            if len(lista_cidades) == 3:

                if lista_cidades[0] in cidades_csv[0] and lista_cidades[1] in cidades_csv[0] and lista_cidades[2] in cidades_csv[0]:

                    if lista_cidades[0] != lista_cidades[1] and lista_cidades[0] != lista_cidades[2] and lista_cidades[1] != lista_cidades[2]:
                        print('\033[0;92mCidades válidas!\033[0;0m')
                        a2 = 2
                        print('\nCalculando melhor rota...\n')
                        time.sleep(2)

                        print('A melhor rota a ser seguida é:\n')
                        melhorRota(lista_cidades)

                    else:
                        print('\033[1;90mQuantidade informada é insuficiente ou inválida!\033[0;0m\n')
                else:
                    print('\033[1;90mQuantidade informada é insuficiente ou inválida!\033[0;0m\n')     
            else:
                print('\033[1;90mQuantidade informada é insuficiente ou inválida!\033[0;0m\n')

    # Responsável por executar a opção "Rota completa"
    elif escolha == '4':
        if custo_km <= 0:
            print('\n\033[1;101m Atenção! \033[0;0m')
            print('O custo do KM rodado não foi informado.')
            print('Favor informe antes de prosseguir para as demais opções.')
            print('\nRedirecionando para o Menu...')
            time.sleep(1)
            continue

        vetor_cidades = []
        cidades_input = ''
        tamanho = 0
        while cidades_input != 'FIM':

                cidades_input = input('Informe no mínimo 3 cidades [Digite "fim" para finalizar]: ').upper()

                if cidades_input in cidades_csv[0]:

                    if cidades_input not in vetor_cidades:
                        vetor_cidades.append(cidades_input)
                        tamanho = len(vetor_cidades)

                        if tamanho < 3:
                            while tamanho < 3:

                                print('\n\033[1;90mQuantidade informada é insuficiente!\033[0;0m\n')

                                cidades_input = input('Informe no mínimo 3 cidades [Digite "fim" para finalizar]: ').upper()
                                if cidades_input in cidades_csv[0]:

                                    if cidades_input not in vetor_cidades:
                                        vetor_cidades.append(cidades_input)
                                        tamanho += 1

                            print('\n\033[0;92mVocê atingiu a quantidade mínima de cidades informadas!\033[0;0m\n')
                        else:
                            print('\n\033[0;92mVocê atingiu a quantidade mínima de cidades informadas!\033[0;0m\n')

                    else:
                        print('\n\033[1;90mDeve informar cidades diferentes!\033[0;0m\n')

                elif cidades_input == 'FIM':
                    continue

                else:
                    print('\n\033[1;90mDeve informar cidades válidas!\033[0;0m\n')

        print('\nVerificando...\n')
        time.sleep(2)

        cidade_a = vetor_cidades[0]
        cidade_b = vetor_cidades[1]
        cidade_c = vetor_cidades[2]

        cidade_a_distancia = 1 + cidades_csv[0].index(cidade_a)
        cidade_b_distancia = cidades_csv[0].index(cidade_b)
        distancia_ab = int(cidades_csv[cidade_a_distancia][cidade_b_distancia])
        print('--' * 50)
        print('Você partirá:')
        print('\033[1mDe: 'f'\033[0m{cidade_a}')
        print('\033[1mPara: 'f'\033[0m{cidade_b}')
        print(f'O percurso deste trajeto será de: {distancia_ab}km.\n')

        cidade_b_distancia = 1 + cidades_csv[0].index(cidade_b)
        cidade_c_distancia = cidades_csv[0].index(cidade_c)
        distancia_bc = int(cidades_csv[cidade_b_distancia][cidade_c_distancia])

        print('Em seu segundo trajeto.\nVocê partirá:')
        print('\033[1mDe: 'f'\033[0m{cidade_a}')
        print('\033[1mPara: 'f'\033[0m{cidade_c}')
        print(f'O percurso deste trajeto será de: {distancia_bc}km.')
        print('--' * 50)

        distancia_total_percorrida = distancia_ab + distancia_bc
        print(f'A distância total percorrida é de: {distancia_total_percorrida}km.\n')

        custo_viagem_total = distancia_total_percorrida * custo_km
        print(f'O custo total da viagem foi de: R${custo_viagem_total :.2f}.\n')

        qtd_total_litros = distancia_total_percorrida * 2.57
        print(f'Quantidade total de litros de combustível consumidos ao final da viagem: {qtd_total_litros :.2f} litros.\n')

        dias_viagem = distancia_total_percorrida // 583
        print(f'O trajeto levará cerca de {dias_viagem} dias.')

        print('--' * 50)

    # Responsável por executar a opção "Sair"
    elif escolha == '5':
        print('\nSaindo...\n')
        time.sleep(2)

    else:
        print('\n\033[1;90mOpção desconhecida!\033[0;0m')
        print('\nRedirecionando para o Menu...')
        time.sleep(1)