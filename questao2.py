
'''Nesta primeira parte foi definido o acumulador para somar o valor dos pedidos, assim como um menu que
será impresso na tela para auxiliar os clientes em suas escolhas'''
soma= 0
print('------ Bem-vindo à loja de marmitas do Guilherme ------' )
print('------------------------------ Cardápio ------------------------------')
print('----------------------------------------------------------------------')
print('---| Tamanho | Bife Acebolado (BA) | Filé de Frango (FF) |---')
print('---|    P    |      R$ 16.00       |      R$ 15.00       |---')
print('---|    M    |      R$ 18.00       |      R$ 17.00       |---')
print('---|    G    |      R$ 22.00       |      R$ 21.00       |---')

'''Aqui foram criadas mensagens de aviso caso o cliente erre os códigos referentes ao sabor e tamanho 
das marmitas, mantendo o loop enquanto estes requisitos não forem cumpridos
Após a escolha do sabor e tamanho das marmitas é perguntado ao cliente se ele gostaria de encerrar o pedido.
Se a resposta for negativa, o código volta ao início, gerando assim a opção de pedir quantas marmitas o
 cliente quiser.
O acumulador definido no início do código é aqui utilizado, fazendo a soma do valor dos pedidos eventualmente
realizados'''
while True:
    marmita= input('Digite aqui o sabor da marmita (BA/FF): ').upper()
    if (marmita != 'BA' and marmita != 'FF'):
        print('Sabor inválido, tente novamente!')
        continue
     
    tamanho= input('Digite o tamanho da marmita(P/M/G): ').upper()
    if (tamanho != 'P' and tamanho != 'M' and tamanho != 'G'):
        print ('Tamanho inválido, tente novamente!')
        continue

    elif (marmita == 'BA' and tamanho == 'P'):
        valor = 16
        soma+=valor
        print (f'Você pediu um Bife Acebolado no tamanho P: R$ {valor}')
        pergunta= input('Deseja mais alguma coisa(S/N)? ').upper()
        if(pergunta == 'S'):
         continue 
        else:break
    
    elif (marmita == 'BA' and tamanho == 'M'):
        valor = 18
        soma+=valor
        print (f'Você pediu Bife Acebolado no tamanho M: R$ {valor}')
        pergunta= input('Deseja mais alguma coisa(S/N)? ').upper()
        if(pergunta == 'S'):
            continue
        else: break

    elif (marmita == 'BA' and tamanho == 'G'):
        valor = 22
        soma+=valor
        print (f'Você pediu Bife Acebolado no tamanho M: R$ {valor}')
        pergunta= input('Deseja mais alguma coisa(S/N)? ').upper()
        if(pergunta == 'S'):
            continue
        else: break

    elif (marmita == 'FF' and tamanho == 'P'):
        valor = 15
        soma+=valor
        print (f'Você pediu Filé de Frango no tamanho P: R$ {valor}')
        pergunta= input('Deseja mais alguma coisa(S/N)? ').upper()
        if(pergunta == 'S'):
            continue
        else: break

    elif (marmita == 'FF' and tamanho == 'M'):
        valor = 17
        soma+=valor
        print (f'Você pediu Filé de Frango no tamanho M: R$ {valor}')
        pergunta= input('Deseja mais alguma coisa(S/N)? ').upper()
        if(pergunta == 'S'):
            continue
        else: break

    elif (marmita == 'FF' and tamanho == 'G'):
        valor = 21
        soma+=valor
        print (f'Você pediu Filé de Frango no tamanho G: R$ {valor}')
        pergunta= input('Deseja mais alguma coisa(S/N)? ').upper()
        if(pergunta == 'S'):
            continue
        else: break
'''Por fim, é impresso na tela o valor total do pedido realizado'''
valor_total = soma 
print (f'O valor total do pedido é: R$ {valor_total}')
    
    

    


    

    


    
    











   

    

    
        



        

    
    
    
        


    

    
    
       



    
    
    

        
        
           
   
        
   
    

    
    
       


    


         

     
      




    

    






    