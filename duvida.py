'''while True:
    nome= input('Digite aqui o seu nome: ')
    if (nome != 'Guilherme' and nome != 'Laura'):
        print ('Nome inválido, tente novamente!')
        continue
    senha= input ('Digite aqui a sua senha: ')
    if (senha != 'boneca' and senha != 'carro'):
        print(' Acesso negado, tente novamente!')
        continue
    else: print ('Acesso permitido!')
    break'''

'''def borda(s1):
    tam= len(s1)
    if tam:
        print('+','-' * tam,'+')
        print('|',s1,'|')
        print('+','-' * tam,'+')'''


'''def soma(x, y, z):
    res= x+y+z
    print(res)'''






#help (print)

# Exigência de CÓDIGO 1
'''print("Bem vindos à empresa do ChatGPT")

# Exigência de CÓDIGO 2
# Número de RU: 1234567
id_global = 1234567
lista_funcionarios = []

# Exigência de CÓDIGO 3
def cadastrar_funcionario(id):
    nome = input("Digite o nome do funcionário: ")
    setor = input("Digite o setor do funcionário: ")
    salario = float(input("Digite o salário do funcionário: "))
    
    funcionario = {
        'id': id,
        'nome': nome,
        'setor': setor,
        'salario': salario
    }
    
    lista_funcionarios.append(funcionario.copy())
    
    print(f"Funcionário {nome} cadastrado com sucesso!")

# Exigência de CÓDIGO 4
def consultar_funcionarios():
    while True:
        print("\nMenu Consultar Funcionários:")
        print("1. Consultar Todos")
        print("2. Consultar por Id")
        print("3. Consultar por Setor")
        print("4. Retornar ao menu principal")
        
        opcao = input("Escolha uma opção (1/2/3/4): ").strip()
        
        if opcao == '1':
            if not lista_funcionarios:
                print("Não há funcionários cadastrados.")
            else:
                print("\nFuncionários cadastrados:")
                for funcionario in lista_funcionarios:
                    print(funcionario)
        
        elif opcao == '2':
            id_consulta = int(input("Digite o ID do funcionário que deseja consultar: "))
            encontrado = False
            for funcionario in lista_funcionarios:
                if funcionario['id'] == id_consulta:
                    print("\nFuncionário encontrado:")
                    print(funcionario)
                    encontrado = True
                    break
            if not encontrado:
                print(f"Funcionário com ID {id_consulta} não encontrado.")
        
        elif opcao == '3':
            setor_consulta = input("Digite o nome do setor que deseja consultar: ").strip().lower()
            encontrados = []
            for funcionario in lista_funcionarios:
                if funcionario['setor'].lower() == setor_consulta:
                    encontrados.append(funcionario)
            
            if not encontrados:
                print(f"Não há funcionários cadastrados no setor {setor_consulta}.")
            else:
                print(f"\nFuncionários no setor '{setor_consulta}':")
                for funcionario in encontrados:
                    print(funcionario)
        
        elif opcao == '4':
            print("Retornando ao menu principal...")
            return
        
        else:
            print("Opção inválida. Por favor, escolha uma opção válida (1, 2, 3 ou 4).")

# Exigência de CÓDIGO 5
def remover_funcionario():
    while True:
        id_remover = int(input("Digite o ID do funcionário que deseja remover: "))
        encontrado = False
        for funcionario in lista_funcionarios:
            if funcionario['id'] == id_remover:
                lista_funcionarios.remove(funcionario)
                print(f"Funcionário com ID {id_remover} removido com sucesso.")
                encontrado = True
                break
        if not encontrado:
            print(f"ID {id_remover} inválido. Não foi encontrado nenhum funcionário com esse ID.")

# Exemplo de uso do menu principal (para demonstrar a interação completa)
while True:
    print("\nMenu Principal:")
    print("1. Cadastrar Funcionário")
    print("2. Consultar Funcionários")
    print("3. Remover Funcionário")
    print("4. Sair")
    
    escolha = input("Escolha uma opção (1/2/3/4): ").strip()
    
    if escolha == '1':
        cadastrar_funcionario(id_global)
        id_global += 1  # Incrementa o ID global após cada cadastro
    elif escolha == '2':
        consultar_funcionarios()
    elif escolha == '3':
        remover_funcionario()
    elif escolha == '4':
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida (1, 2, 3 ou 4).")'''


'''for expoente in range (7,11):
    print('%-2d%12d' % (expoente, 10**expoente))'''

first= int(input('Digite o priemeiro número: '))
second= int(input('Digite o segundo número: '))

print('Máximo: ', max(first, second))
print('Mínimo: ', min(first, second))