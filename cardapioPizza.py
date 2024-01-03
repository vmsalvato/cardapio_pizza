import sys

item = {}
opcao = ()
busca = ()

def exibe_menu():
    print('-' * 5)
    print('[1] Adicionar pizza no cardápio')
    print('[2] Consultar pizza')
    print('[3] Alterar pizza do cardápio')
    print('[4] Excluir pizza do cardápio')
    print('[5] Exibir cardápio completo')
    print('[6] Exportar cardápio para arquivo texto')
    print('[7] SAIR ')
    print('-' * 5)
    opcoes()

def opcoes():
    while True:
        opcao = str(input('Digite um valor: '))
        if opcao == '1':
            cardapio_cadastrar()
        if opcao == '2':
            cardapio_consulta()
        if opcao == '3':
            cardapio_alterar()
        if opcao == '4':  
            cardapio_remover()
        if opcao == '5':  
            cardapio_exibir()
        if opcao == '6':  
            cardapio_salvar()
        if opcao == '7':  
            sys.exit()
        else:
            print('Insira um valor válido!')
 
def cardapio_cadastrar():
    
        codigo = input('Digite um código para a pizza: ')
        pizza = input('Digite o nome da pizza: ')
        ingredientes = input('Digite os ingredientes da pizza: ')
        preco = input('Digite um preço para a pizza: ')

        cardapio = []
        cardapio.append(pizza)
        cardapio.append(ingredientes)
        cardapio.append(preco)
        item.update({codigo: cardapio})

        escolha_menu()

def cardapio_consulta():
    consulta = input('Digite o código da pizza: ')
    if consulta in item:
        print(f"Código da pizza: {consulta}")
        print(item[consulta])
    else:
        print('Não encontrado!')
    escolha_menu()
  
def cardapio_alterar():
    alterar = input('Digite o código da pizza a ser alterada: ')
    if alterar in item:
        print(item[alterar])
        escolha = input('Digite qual informação deseja alterar:\n[1] Código\n[2] Pizza\n[3] Ingredientes\n[4] Preço')
        if escolha == '1': 
            codigo = input('Digite um novo código para a pizza: ')
            item[codigo] = item.pop(alterar)
            print("Alterado com sucesso!")
            escolha_menu()

        elif escolha == '2': 
            pizza = input('Digite um novo nome para a pizza: ')
            item[alterar].remove(item[alterar][0])
            item[alterar].insert(0, pizza)
            print("Alterado com sucesso!")
            escolha_menu()

        elif escolha == '3': 
            ingrediente = input('Digite um novo ingrediente: ')
            item[alterar].remove(item[alterar][1])
            item[alterar].insert(1, ingrediente)
            print("Alterado com sucesso!")
            escolha_menu()
        
        elif escolha == '4': 
            preco = input('Digite um novo preço: ')
            item[alterar].remove(item[alterar][2])
            item[alterar].insert(2, preco)
            print("Alterado com sucesso!")
            escolha_menu()
        
        else:
            print("Valor não reconhecido!")
            escolha = input('Digite qual informação deseja alterar:\n[1] Código\n[2] Pizza\n[3] Ingredientes\n[4] Preço')
    else:
        print('Não encontrado!')
  
      
    escolha_menu()

def cardapio_remover():
    deletar = input('Digite o código da pizza a ser deletada: ')
    if deletar in item:
        del item[deletar]
        print('Dado deletado!')
    else:
        print('Valor não encontrado!')
    
    escolha_menu()

def cardapio_exibir():
    print(f'O cardapio atual é: ')
    cardapio.append(item)
    print(cardapio)
    cardapio.clear()

    escolha_menu()

def cardapio_salvar():
    with open ('cardapio.txt', 'w') as arquivo:
       for valor in item.values():
        arquivo.write(str(valor) + '\n')
    arquivo.close()
    print('Arquivo .txt exportado!')
    escolha_menu()

def escolha_menu():
    print('-' * 5)
    while True:
        escolha = str(input('Digite [1] para voltar ao menu, ou [0] para sair: '))
        if escolha == '1':
            exibe_menu()
        if escolha == '0':
            sys.exit()
        else: 
            print('Insira um valor válido!')
            print('-' * 5)

nome = str(input('Digite seu nome: '))

print('-' * 5)
print(f'Olá {nome}, seja bem-vindo! Escolha uma das opções do menu para continuar.')
exibe_menu()
print('-' * 5)
