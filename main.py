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

def listar_projetos():
    print("\n=================================")
    print("       LISTAR PROJETOS")
    print("=================================")

    if not  projetos:
        print("Nenhum projeto cadastrado!")
        return
    for projeto in projetos:
        print(f"Código:{projeto['codigo']}")
        print(f"Nome:{projeto['nome']}")
        print(f"Cliente:{projeto['cliente']}")
        print(f"Status:{projeto['status']}")
        print(f"Data:{projeto['data']}")
        print("-------------------------------------")
def buscar_projeto():
    print("\n==================================")
    print("     BUSCAR PROJETO")
    print("====================================")

    codigo = input("Digite o codigo do projeto: ")

    for projeto in projetos:
            print("Projeto encontrado!")
            print(f"Código:{projeto['codigo']}")
            print(f"Nome:{projeto['nome']}")
            print(f"Cliente:{projeto['cliente']}")
            print(f"Status:{projeto['status']}")
            print(f"Data:{projeto['data']}")
            return
    print("/nProjeto não encontrado.")

def alterar_status():
    print("\n==================================")
    print("     ALTERAR STATUS")
    print("=================================")

    codigo = input("Digite o codigo do projeto: ")

    for projeto in projetos:
        print(f"Projeto:{projeto['nome']}")
        print(f"Status atual:{projeto['status']}")

        novo_status = input("Digite o novo status atual: ")
        projeto['status'] = novo_status

        print("\nProjeto alterado com sucesso!")
        return
    print("\nProjeto não encontrado.")

def main():
    print("Sistema iniciado!")
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_projeto()

        elif opcao == "2":
            listar_projetos()

        elif opcao == "3":
            buscar_projeto()

        elif opcao == "4":
            alterar_status()

        elif opcao == "0":
            print("Saindo do sistema!")
            break
        else:
            print("Opção invalida!")

if __name__ == "__main__":
    main()