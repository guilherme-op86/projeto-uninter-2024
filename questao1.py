'''O programa em questão calcula o parcelamento de uma eventual compra, já incluindo no valor final a 
respectiva taxa de juros'''
print('Bem-vindos à loja do Guilherme')
valorDoPedido = float(input('Digite aqui o valor do pedido: R$ '))
quantidadeParcelas = int(input('Digite aqui a quantidade de parcelas desejadas: '))

'''Na segunda parte estabelecemos as parcelas e as respectivas taxas de juros '''
if (quantidadeParcelas < 4):
    juros= 0
    
elif ( 4 <= quantidadeParcelas < 6):
    juros= 4/100

elif ( 6 <= quantidadeParcelas < 9):
    juros= 8/100

elif ( 9 <= quantidadeParcelas < 13):
   juros= 16/100  
else:
    juros= 32/100

'''Por fim, efetuamos os cálculos do pagamento do valor do pedido, informando o valor da parcela e o
montante, já acrescidos da taxa de juros correspondente.'''
valorDaParcela  =valorDoPedido * (1 + juros) / quantidadeParcelas
valorTotalParcelado = valorDaParcela * quantidadeParcelas

print(f"O valor de cada parcela é de: R${valorDaParcela: .2f}")
print(f'O valor total da compra é de: R${valorTotalParcelado: .2f}')



















'''nesta primeira parte foram definidas as variáveis que serão utilizadas no desenvolvivento do código.
o valor do pedido é um número com ponto flutuante, enquanto a quantidade de parcelas é um númeiro inteiro'''
'''print('Bem-vindos à loja do Guilherme Oliveira de Paula')
valorDoPedido = float(input('Digite aqui o valor do pedido: R$ '))
quantidadeParcelas = int(input('Digite aqui a quantidade de parcelas desejadas: '))'''

'''Nesta parte foram elaborados os cálculos das parcelas e valor total do pedido. Utilizou-se valores exatos
 na divisão das parcelas para que os cálculos possam ser facilmente compreendidos pelos eventuais clientes'''
'''if (quantidadeParcelas < 4):
    valorDaParcela  = valorDoPedido // quantidadeParcelas
    valorTotalParcelado = valorDaParcela * quantidadeParcelas
    
elif ( 4 <= quantidadeParcelas < 6):
    valorDaParcela  =valorDoPedido * (1 + 4/100) // quantidadeParcelas
    valorTotalParcelado = valorDaParcela * quantidadeParcelas

elif ( 6 <= quantidadeParcelas < 9):
    valorDaParcela  =valorDoPedido * (1 + 8/100) // quantidadeParcelas
    valorTotalParcelado = valorDaParcela * quantidadeParcelas

elif ( 9 <= quantidadeParcelas < 13):
   valorDaParcela  =valorDoPedido * (1 + 16/100) // quantidadeParcelas
   valorTotalParcelado = valorDaParcela * quantidadeParcelas
   
else:
    valorDaParcela  =valorDoPedido * (1 + 32/100) // quantidadeParcelas
    valorTotalParcelado = valorDaParcela * quantidadeParcelas'''

'''Aqui imprimimos uma mensagem de boas vindas para tornar aexperiência mais amigável para o cliente.
Por fim, serão exibidas na tela uma mensagem com o valor exato de cada parcela, já levando em consideração
a respectiva taxa de juros (quando houver), assim como o valor total da compra tealizada'''
'''print('Bem-vindos à loja do Guilherme Oliveira de Paula')
print(f"O valor de cada parcela é de: R${valorDaParcela}")
print(f'O valor total da compra é de: R${valorTotalParcelado}')'''