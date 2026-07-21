from dados import livros, alunos, emprestimos

def listar_historico():
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
                    print(f"Matrícula: {aluno.matricula} - Nome: {aluno.nome}")

                aluno_encontrado = buscar_aluno_historico(alunos)
                exibir_historico_aluno(aluno_encontrado)

                while True:
                    continuar = input("\nDeseja continuar? (S/N): ").upper()
                    if continuar in ("S", "N"):
                        break
                    print("Opção inválida! Digite apenas S ou N.")

                if continuar == "N":
                    break

        elif opcao_historico == "2":
            listar_emprestimos_ativos()

        elif opcao_historico == "3":
            break


def buscar_aluno_historico(alunos):
    while True:
        busca = input("Digite o nome ou matrícula do aluno selecionado: ").strip()

        aluno_encontrado = None
        for aluno in alunos:
            if busca == aluno.matricula or busca.lower() in aluno.nome.lower():
                aluno_encontrado = aluno
                break

        if aluno_encontrado is not None:
            return aluno_encontrado
        else:
            print("Aluno não encontrado. Tente novamente.")


def exibir_historico_aluno(aluno):
    emprestimos_aluno = []

    for registro in emprestimos:
        if registro["Aluno"].matricula == aluno.matricula:
            emprestimos_aluno.append(registro)

    ativos = []
    devolvidos = []
    atrasados = []
    todos_titulos = []

    for registro in emprestimos_aluno:
        titulo = registro["Livro"].titulo
        todos_titulos.append(titulo)

        data_formatada = registro["Data"].strftime("%d/%m/%Y %H:%M")
        data_devolucao = registro.get("data_devolucao", "")

        if data_devolucao == "":
            ativos.append(f"{titulo} (desde {data_formatada})")
        else:
            devolvidos.append(titulo)
        
        if registro.get("atrasou") == "Sim":
            atrasados.append(f"{titulo} ({registro.get('dias_atraso', '')})")

    print(f"\nMatrícula: {aluno.matricula}" f"\nAluno: {aluno.nome}")

    if len(ativos) > 0:
        print(f"\nLivro(s) com emprestimos ativos: {'  |  '.join(ativos[:4])}")
    else:
        print("\nLivro(s) com emprestimos ativos: Nenhum")
    
    if len(devolvidos) > 0:
        print(f"Livro(s) devolvidos: {'  |  '.join(devolvidos)}")
    else:
        print("Livro(s) devolvidos: Nenhum")

    if len(atrasados) > 0:
        print(f"Livro(s) em atraso: {'  |  '.join(atrasados)}")
    else:
        print("Livro(s) em atraso: Nenhum")
    
    print(f"\nHistorico de livros: ({len(emprestimos_aluno)})")

    if len(emprestimos_aluno) > 0:
        print("\nUltimos 4 livros:\n")
        for titulo in reversed(todos_titulos[-4:]):
            print(f"* {titulo}")
    else:
        print("\nEste aluno não pegou nemhum livro emprestado")

def listar_emprestimos_ativos():
    tem_ativo = False
    for registro in emprestimos:
        if registro.get("data_devolucao", "") == "":
            tem_ativo = True
            break

    if not tem_ativo:
        print("\nNão há empréstimos ativos no momento.")
        return

    print("\n===== EMPRÉSTIMOS ATIVOS =====\n")

    for aluno in alunos:
        titulos = []

        for registro in emprestimos:
            if registro["Aluno"].matricula == aluno.matricula and registro.get("data_devolucao", "") == "":
                titulos.append(registro["Livro"].titulo)

        if len(titulos) > 0:
            print(f"Matrícula: {aluno.matricula}")
            print(f"Nome: {aluno.nome}")
            print(f"Emprestimos ativos: {', '.join(titulos[:4])}")
            print("-" * 100)