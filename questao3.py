'''Nesta primeira função foram dfinidos os modelos de camisetas e seus respectivos preços, implementando-se
uma mensagem de aviso caso o cliente digite um código de produto inexistente.'''
def escolha_modelo():
    print('Bem vindo à loja de camisetas do Guilherme\n')
    print('Entre como o modelo desejado')
    print('MCS - Manga Curta Simples')
    print('MLS - Manga Longa Simples')
    print('MCE - Manga Curta Estampada')
    print('MLE - Manga Longa Estampada')

    while True:
        modelo= input('Entre com o modelo desejado: ').upper().strip()
        if(modelo == 'MCS'):
            return 1.80
        elif(modelo == 'MLS'):
            return 2.10
        elif(modelo == 'MCE'):
            return 2.90
        elif(modelo == 'MLE'):
            return 3.20
        else:
            print('Modelo escolhido é inválido, tente novamente.')

'''Na segunda função é feita a escolha da quantidade de camisetas, imprimindo-se uma mensagem de aviso caso
o pedido extrapole a capacidade de produção da fábrica, bem como alertando se um caractere diferente de
um numeral seja digitado erroneamente.
Importante entender a dinâmica do cálculo de retorno do número de camisetas já com o desconto. Como não
estamos trabalhando com valores e sim com quantidade de um produto, o desconto aplicado sobre a quantidade 
de camisetas simula uma diminuição na quantidade de camisetas pedidas, proporcionalmente ao valor do desconto.
Mas no final, o cálculo considera o pedido inteiro feito pelo cliente, informando o mesmo valor a ser pago, 
caso o cálculo fosse feito utilizando os valores das camisetas.
 '''
def num_camisetas():
    while True:
        try:
            numero_de_camisetas= int(input('Digite a quantidade de camisetas: '))
            if (numero_de_camisetas > 20000):
             print('Não aceitamos tantas camisetas de uma vez.')
             print('Por favor, entre com a quantidade de camisetas novamente!')
             continue
            elif (20 <= numero_de_camisetas < 200):
                des= 5/100
            elif (200 <= numero_de_camisetas < 2000):
                des= 7/100
            elif (2000 <= numero_de_camisetas <= 20000):
                des= 12/100 
            else:
                des = 0  
            return numero_de_camisetas * (1 - des) 
        except ValueError:
            print('Valor digitado não é um número, tente novamente!')
          
'''A terceira função apresenta as opções de frete, assim como seus respectivos valores. Aqui também foi
implementeada uma mensagem alertando o clinte caso uma opção inválida seja digitada.'''
def frete():
    print('Escolha o tipo de frete:')
    print('1 - Frete por trasnportadora - R$ 100')
    print('2 - Frete por Sedex - R$ 200')
    print('0 - Retirar o pedido na fábrica - R$ 0')
    while True:
            op_frete= input('Escolha o tipo de frete: ')
            if (op_frete == '1'):
                return 100    
            elif (op_frete == '2'):
                return 200 
            elif (op_frete == '0'):
                return 0
            else:
                print('Opção de frete iválida, tente novamente!')

#programa principal
''' No programa principal foi implementado o código que calcula a quantidade de camisetas, valor destas com
desconto e frete escolhido''' 

valor_total= escolha_modelo() * num_camisetas() + frete()
print(f'R$ {valor_total}')
print (f'Modelo: R$ {escolha_modelo()} * Quantidade (c/desconto): {num_camisetas()} + frete: R$ {frete()}')





 



    
    

            
 












   

