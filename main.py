projetos = []

def exibir_menu():
    print("\n===================================")
    print("       CONTROLE DE PROJETOS")
    print("===================================")
    print("1 - Cadastrar projeto")
    print("2 - Listar projetos")
    print("3 - Buscar projeto")
    print("4 - Alterar status")
    print("5 - Remover projeto")
    print("0 - Sair")
    print("===================================")

def cadastrar_projeto():
    print("\n===================================")
    print("        CADASTRAR PROJETO")
    print("===================================")

    codigo = input("Digite o codigo do projeto: ")
    nome = input("Digite o nome do projeto: ")
    cliente = input("Digite o cliente do projeto: ")
    status = input("Digite o status do projeto: ")
    data = input("Digite o data do projeto: ")

    projeto = {
        "codigo": codigo,
        "nome": nome,
        "cliente": cliente,
        "status": status,
        "data": data
    }
    projetos.append(projeto)
    print("Projeto cadastrado com sucesso!")

def main():
    print("Sistema iniciado!")
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_projeto()
        elif opcao == "0":
            print("Saindo do sistema!")
            break
        else:
            print("Opção invalida!")

if __name__ == "__main__":
    main()