import time
import socket
from requests import get
import smtplib
import socket
import os
print('')

restart = 'S'

while restart == 'S':
    print('#####################')
    time.sleep(0.5)
    print('Consulta de IP por DNS')
    time.sleep(0.5)
    print('Tool by Dr Midnight')
    time.sleep(0.5)
    print('#####################\n')
    time.sleep(0.5)
    print('Iniciando o script...')
    time.sleep(2)
    print()

    print('[1] Puxar IP de Hosts')
    print('[2] Do que se trata?')

    def host():
        print('')
        print('Olá!')
        time.sleep(0.3)
        print('Aqui, você pode pegar endereçamentos de específicos hostnames.\n')
        time.sleep(0.5)
        host = input('Consulte uma DNS: ')
        host = socket.gethostname()
        intern = socket.gethostbyname(host)
        extern = get('https://api.ipify.org').text
        print()

        print(f'Host: {host}')
        print(f'IP Interno: {intern}')
        print(f'IP Externo: {extern}')

    def help():
        print('###########################################################################################################\n')
        print('O QUE É?\n')
        print('O IP é o seu endereço na internet. É por ele que o seu computador se comunica com outros computadores.\n'
              ' Ele pode ser estático (não muda) ou dinâmico (muda com o tempo) e é atribuído pela sua operadora de internet.\n')
        print('Todo Site possui um local o qual recebe Host, ou seja, é Hospedado de uma máquina.')
        print('Quando consultamos uma DNS através da Hostname, estamos checando os dados do Servidor que está fornecendo Host\n')
        print('###########################################################################################################\n')
        print('PARA QUE É ÚTIL?\n')
        print('Com o IP de Host de um determinado Site em mãos, podemos não só apenas saber a geo localização, a qual\n'
              ' o servidor está sendo mantido, como também podemos usar disto para outras coisas\n')
        print('Se uma pessoa cometer algum crime virtual a polícia pode descobrir o endereço verdadeiro do criminoso\n'
              'através do IP procurando a operadora de internet que vai consultar o banco de dados deles onde estão\n'
              'listados todos os clientes e horários mostrando quem usava qual IP e quando. Então se por acaso,'
              ' acabar\nsendo vítima de golpe através de alguma "http", esta ferramenta o ajudará na busca do responsável.\n')
        print('Além disto existem diversos atributos para a área de Pen Tester, tais como:')
        print('--> Invasão de computadores via exploit, que é alguma falha específica presente em algum software de uma máquina'
              ' ligada a rede.')
        print('--> Ataques de DDOS, que é derrubar uma conexão (ou torna-la instável) enviando várias requisições por segundo,'
              ' gerando\n uma sobrecarga na rede onde o dispositivo com aquele IP está conectado.\n')
        print('###########################################################################################################')

    mid = input("\n>>> Escolha a opção: ")

    if mid == '1':
        host()

    elif mid == '2':
        help()

    restart = str(input('\nDeseja realizar outra consulta S/N? ')).strip().upper()[0]
    print('')
    os.system('cls')
