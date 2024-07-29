'''Variáveis que serão utilizadas durante a execução do programa '''
lista_funcionarios= []
id_global= 4903898

'''função que cadastra funcionários e utiliza como contador o id global'''
def cadastrar_funcionario(id_global):
    print('-' *20, 'Menu Cadastrar Funcionário', '-' * 24)
    nome = input('Entre com o nome do funcionário: ')
    setor = input('Digite o setor em que o funcionário trabalha: ')
    salario = float(input('Digite o salário do funcionário: R$ '))
    
    funcionario = {'ID': id_global, 'Nome': nome, 'Setor': setor, 'Salário': salario}

    lista_funcionarios.append(funcionario.copy())
    print(f'Funcionário {nome} foi castrado.')
    print(funcionario)
    
'''função que gera um menu para consulta dos funcionários de acordo com os dados cadastrados anteriormente '''   
def consultar_funcionarios():
    while True:
        print('-' *20, 'Menu Consultar Funcionário', '-' * 24)
        print('1 - Consultar todos')
        print('2 - Consultar por ID')
        print('3 - Consultar por setor')
        print('4 - Retornar ao menu')
        opcao= input('Digite a opção desejada: ')
        if (opcao == '1'):
            print(lista_funcionarios) 

        elif (opcao == '2'):
            id_ref = int(input('Digite o ID do funcionário que deseja pesquisar: '))
            for funcionario in lista_funcionarios:
              if (id_ref == funcionario ['ID']):
               print (funcionario)    

        elif (opcao == '3'):
            setor_ref = input('Digite o setor do funcionário que deseja pesquisar: ')
            for funcionario in lista_funcionarios:
             if (setor_ref == funcionario['Setor']):
                print(funcionario)

        elif (opcao == '4'):
           print('Retornando ao Menu Principal...')
           return
        
        else:
           print('A opção digitada é inválida, tente novamente!')

'''função que apaga o funcionário que foi selecionado pelo respectivo ID'''
def remover_funcionario():
    while True:
        print('-' *20, 'Menu Remover Funcionário', '-' * 24)
        id_ref= int(input('Digite o ID do funcionário que pretende remover: '))
        for funcionario in lista_funcionarios:
         if (id_ref == funcionario['ID']):
          lista_funcionarios.remove(funcionario)
          print(f'Funcionário {id_ref} removido com sucesso')
         else:
          print('O ID digitado é inválido, tente novamente!')
         return 
     
'''Programa principal, que gera um menu com as opções de escolhas dentro do programa'''
while True:
    print('Bem vindos à empresa do Guilherme Oliveira de Paula')
    print('-' * 60)
    print('-' *20, 'Menu Pincipal', '-' * 24)
    print('Escolha a opção desejada:')
    print('1 - Cadastrar funcionários')
    print('2 - Consultar funcionário (s)')
    print('3 - Remover funcionário')
    print('4 - Sair')

    opcao = input('Digite a opção desejada: ')
    if(opcao == '1'):
      cadastrar_funcionario(id_global)
      id_global+=1
    elif(opcao == '2'):
      consultar_funcionarios()
    elif (opcao == '3'):
      remover_funcionario()
    elif (opcao == '4'):
      print ('Saindo do programa...')
      break
    else:
      (print('Opção digitada é inválida, tente novamente!')) 
      
    
      



        
           

   
        



                 