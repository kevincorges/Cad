#Kevin Cordeiro Borges
#Linguagem de programação python.

def busca_por_nome(nome, vetor_usuarios,vetor_idades ):
    for i in range (len(vetor_usuarios)):
        if vetor_usuarios[i] == nome:
            return nome,vetor_idades[i],i
    return -1,-1,-1

def excluir(exclusão,vetor_usuarios,vetor_idades):
    nome, _, indice = busca_por_nome(exclusão, vetor_usuarios,vetor_idades)
    if indice > -1:
        vetor_usuarios.pop(indice)
        vetor_idades.pop(indice)
        for i in range(indice, len(vetor_usuarios)-1):
            vetor_usuarios[i] = vetor_usuarios[i+1]
            vetor_idades[i] = vetor_idades[i+1]
        return vetor_usuarios, vetor_idades
    return -1,-1

menu = int(input(""" O que você deseja fazer?
                    [1] - Cadastrar novo usuário
                    [2] - Listar todos os usuários cadastrados
                    [3] - Sair do sistema
                    [4] - Buscar usuário
                    [5] - Excluir usuário
                    resposta: """))

vetor_usuarios = []
vetor_idades = []
while menu != 3:
    if menu == 1:
        quantidade_usuarios = int(input('Quantos usuários você deseja cadastrar? '))
        for usuario in range (quantidade_usuarios):
            nome = input('Digite o nome do usuario: ')
            idade = int(input('Digite a idade do usuário: '))
            print(f"Usuário {nome} de idade {idade} anos cadastrado!")
            vetor_usuarios.append(nome)
            vetor_idades.append(idade)
     
        menu = int(input(""" O que você deseja fazer?
                 [1] - Cadastrar novo usuário
                 [2] - Listar todos os usuários cadastrados
                 [3] - Sair do sistema
                 [4] - Buscar usuário  
                 [5] - Excluir usuário      
                 resposta: """))
    elif menu == 2:
        if not vetor_usuarios and not vetor_idades:
            print("Ainda não há cadastros!")
            menu = int(input(""" O que você deseja fazer?
                 [1] - Cadastrar novo usuário
                 [2] - Listar todos os usuários cadastrados
                 [3] - Sair do Sistema
                 [4] - Buscar usuário
                 [5] - Excluir usuário
                 resposta: """))
        else:
            for i in range(len(vetor_usuarios)):
                nome = vetor_usuarios[i]
                idade = vetor_idades[i]
                print("{}. Nome: {}  -  Idade {} anos".format(i+1, nome, idade))

            menu = int(input(""" O que você deseja fazer?
                    [1] - Cadastrar novo usuário
                    [2] - Listar todos os usuários cadastrados
                    [3] - Sair do sistema
                    [4] - Buscar usuário
                    [5] - Excluir usuário
                    resposta: """))
    elif menu == 4:
        usuario = input("Digite o nome do usuário que você deseja buscar: ")
        resultado_busca = busca_por_nome(usuario, vetor_usuarios,vetor_idades)
        if resultado_busca[2] != -1:
            print("O usuário {}, de idade {} anos foi encontrado na posição {}".format(resultado_busca[0], resultado_busca[1], resultado_busca[2]))
        else:
            print("Usuário não encontrado!")
        menu = int(input(""" O que você deseja fazer?
                 [1] - Cadastrar novo usuário
                 [2] - Listar todos os usuários cadastrados
                 [3] - Sair do Sistema
                 [4] - Buscar usuário
                 [5] - Excluir usuário
                 resposta: """))
        
    elif menu == 5:
        exclusão = input("Digite o nome do usuário que você deseja remover: ")
        resultado_exclusão = excluir(exclusão, vetor_usuarios,vetor_idades)
        if resultado_exclusão[0] == -1:
            print("Usuário não encontrado! Por favor, verifique o nome e tente novamente.")
        else:
            print("Usuário removido com sucesso!")
        
        menu = int(input(""" O que você deseja fazer?
                    [1] - Cadastrar novo usuário
                    [2] - Listar todos os usuários cadastrados
                    [3] - Sair do sistema
                    [4] - Buscar usuário
                    [5] - Excluir usuário
                    resposta: """))
        
    else:
        print("Por favor, digite uma opção válida!")
        menu = int(input(""" O que você deseja fazer?
                 [1] - Cadastrar novo usuário
                 [2] - Listar todos os usuários cadastrados
                 [3] - Sair do Sistema
                 [4] - Buscar usuário
                 [5] - Excluir usuário
                 resposta: """))
if menu == 3:
    print("Sistema encerrado!")