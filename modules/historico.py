def listar_historico(livros, alunos, emprestimos):
    while True:
        print("\n===== HISTÓRICO =====")
        print("1 - Consultar histórico" "\n2 - Listar empréstimos ativos" "\n3 - Sair")

        opcao_historico = input("Opcao: ")

        if opcao_historico not in ("1", "2", "3"):
            print("Opção inválida! Digite apenas 1, 2 ou 3.")
            continue

        if opcao_historico == "1":
            if len(alunos) == 0:
                print("\nNão há alunos cadastrados.")
                continue

            while True:
                print("\nAlunos cadastrados:")
                for aluno in alunos:
                    print(f"ID: {aluno['id']} - Nome: {aluno['nome']}")

                aluno_encontrado = buscar_aluno(alunos)
                exibir_historico_aluno(aluno_encontrado, livros, emprestimos)

                while True:
                    continuar = input("\nDeseja continuar? (S/N): ").upper()
                    if continuar in ("S", "N"):
                        break
                    print("Opção inválida! Digite apenas S ou N.")

                if continuar == "N":
                    break

        elif opcao_historico == "2":
            listar_emprestimos_ativos(livros, alunos, emprestimos)

        elif opcao_historico == "3":
            break


def buscar_aluno(alunos):
    while True:
        busca = input("Digite o nome ou id do aluno selecionado: ")

        aluno_encontrado = None
        for aluno in alunos:
            if (busca.isdigit() and aluno["id"] == int(busca)) or \
               (busca.lower() in aluno["nome"].lower()):
                aluno_encontrado = aluno
                break

        if aluno_encontrado is not None:
            return aluno_encontrado
        else:
            print("Aluno não encontrado. Tente novamente.")


def exibir_historico_aluno(aluno, livros, emprestimos):
    emprestimos_aluno = []

    for emprestimo in emprestimos:
        if emprestimo["id_aluno"] == aluno["id"]:
            emprestimos_aluno.append(emprestimo)

    ativos = []
    devolvidos = []
    atrasados = []
    todos_titulos = []

    for emprestimo in emprestimos_aluno:
        titulo = "Livro desconhecido"
        for livro in livros:
            if livro["id"] == emprestimo["id_livro"]:
                titulo = livro["titulo"]
                break

        todos_titulos.append(titulo)

        data_formatada = emprestimo["data_emprestimo"].strftime("%d/%m/%Y %H:%M")

        if emprestimo["data_devolucao"] == "":
            ativos.append(f"{titulo} (desde {data_formatada})")
        else:
            devolvidos.append(titulo)

        if emprestimo["atrasou"] == "Sim":
            atrasados.append(f"{titulo} ({emprestimo['dias_atraso']})")

    print(f"\nID: {aluno['id']}")
    print(f"Aluno: {aluno['nome']}")

    if len(ativos) > 0:
        print(f"\nLivro(s) com emprestimo ativo: {' | '.join(ativos[:4])}")
    else:
        print("\nLivro(s) com emprestimo ativo: Nenhum")

    if len(devolvidos) > 0:
        print(f"Livro(s) devolvidos: {' | '.join(devolvidos)}")
    else:
        print("Livro(s) devolvidos: Nenhum")

    if len(atrasados) > 0:
        print(f"Livro(s) em atraso: {' | '.join(atrasados)}")
    else:
        print("Livro(s) em atraso: Nenhum")

    print(f"\nHistorico de livros: ({len(emprestimos_aluno)})")

    if len(emprestimos_aluno) > 0:
        print("       Ultimos 4 livros:\n")
        for titulo in reversed(todos_titulos[-4:]):
            print(f"* {titulo}")
    else:
        print("       Este aluno ainda não pegou nenhum livro emprestado.")


def listar_emprestimos_ativos(livros, alunos, emprestimos):
    tem_ativo = False
    for emprestimo in emprestimos:
        if emprestimo["data_devolucao"] == "":
            tem_ativo = True
            break

    if not tem_ativo:
        print("\nNão há empréstimos ativos no momento.")
        return

    print("\n===== EMPRÉSTIMOS ATIVOS =====\n")

    for aluno in alunos:
        titulos = []

        for emprestimo in emprestimos:
            if emprestimo["id_aluno"] == aluno["id"] and emprestimo["data_devolucao"] == "":
                for livro in livros:
                    if livro["id"] == emprestimo["id_livro"]:
                        titulos.append(livro["titulo"])
                        break

        if len(titulos) > 0:
            print(f"ID: {aluno['id']}")
            print(f"Nome: {aluno['nome']}")
            print(f"Emprestimos ativos: {', '.join(titulos[:4])}")
            print("-" * 97)