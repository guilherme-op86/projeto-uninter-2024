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



















