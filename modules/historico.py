from dados import livros, alunos, emprestimos

def listar_historico():
    while True:
        print("\n===== HISTÓRICO =====")
        print("1 - Exibir histórico" "\n2 - Consultar histórico" "\n3 - Consultar histórico do livro" "\n4 - Listar empréstimos ativos" "\n5 - Histórico de devoluções" "\n6 - Sair")

        opcao_historico = input("Opcao: ")

        if opcao_historico not in ("1", "2", "3", "4", "5", "6"):
            print("Opção inválida! Digite apenas 1, 2, 3, 4, 5 ou 6.")
            continue

        if opcao_historico == "1":
            exibir_historico_geral()

        elif opcao_historico == "2":
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
                    continuar = input("\nDeseja continuar? (S/N): ").upper()[0]
                    if continuar in ("S", "N"):
                        break
                    print("Opção inválida! Digite apenas S ou N.")

                if continuar == "N":
                    break

        elif opcao_historico == "3":
            historico_livro()

        elif opcao_historico == "4":
            listar_emprestimos_ativos()

        elif opcao_historico == "5":
            listar_devolucoes()

        elif opcao_historico == "6":
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

def historico_livro():
    if len(livros) == 0:
        print("\nNão há livros cadastrados.")
        return

    print("\nLivros cadastrados:")
    for livro in livros:
        print(f"Código: {livro.codigo} - Título: {livro.titulo}")

    codigo = input("\nDigite o código do livro: ").strip()

    pegou = []
    devolveu = []
    atrasou = []

    for registro in emprestimos:
        if registro["Livro"].codigo == codigo:
            nome_aluno = registro["Aluno"].nome
            pegou.append(nome_aluno)

            if registro.get("data_devolucao", "") != "":
                devolveu.append(nome_aluno)

            if registro.get("atrasou") == "Sim":
                atrasou.append(nome_aluno)

    if len(pegou) == 0:
        print("\nEste livro ainda não foi pego por ninguém.")
        return

    print(f"\nQuem já pegou: {', '.join(pegou)}")
    print(f"Quem já devolveu: {', '.join(devolveu) if devolveu else 'Ninguém'}")
    print(f"Quem já atrasou: {', '.join(atrasou) if atrasou else 'Ninguém'}")

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

def listar_devolucoes():
    tem_devolucao = False
    for registro in emprestimos:
        if registro.get("data_devolucao", "") != "":
            tem_devolucao = True
            break

    if not tem_devolucao:
        print("\nNão há devoluções realizadas no momento.")
        return

    print("\n===== HISTÓRICO DE DEVOLUÇÕES =====\n")

    for aluno in alunos:
        titulos = []

        for registro in emprestimos:
            if registro["Aluno"].matricula == aluno.matricula and registro.get("data_devolucao", "") != "":
                titulos.append(registro["Livro"].titulo)

        if len(titulos) > 0:
            print(f"Matrícula: {aluno.matricula}")
            print(f"Nome: {aluno.nome}")
            print(f"Devoluções: {', '.join(titulos[:4])}")
            print("-" * 100)

def aplicar_filtros(registros, aluno=None, livro=None, tipo=None):
    resultado = []

    for r in registros:
        if aluno is not None:
            if r.get("Aluno") is None or r["Aluno"].matricula != aluno.matricula:
                continue

        if livro is not None:
            if r.get("Livro") is None or r["Livro"].codigo != livro.codigo:
                continue

        if tipo == "ativo":
            if r.get("data_devolucao", "") != "":
                continue
        elif tipo == "devolucao":
            if r.get("data_devolucao", "") == "":
                continue
        elif tipo == "atraso":
            if r.get("atrasou") != "Sim":
                continue

        resultado.append(r)

    return resultado

def formatar_data(obj):
    if obj == "":
        return ""
    if hasattr(obj, "strftime"):
        return obj.strftime("%d/%m/%Y %H:%M")
    return str(obj)

def mostrar_registros(registros):
    if not registros:
        print("\nNenhum registro encontrado.")
        return

    for registro in registros:
        aluno = registro["Aluno"].nome
        livro = registro["Livro"].titulo
        data_emprestimo = formatar_data(registro.get("Data", ""))
        print(f"{aluno} fez um empréstimo do livro: {livro} em {data_emprestimo}")

        data_devolucao = registro.get("data_devolucao", "")
        if data_devolucao != "":
            data_devolucao = formatar_data(data_devolucao)
            if registro.get("atrasou") == "Sim":
                dias_atraso = registro.get("dias_atraso", "")
                print(f"{aluno} devolveu o livro: {livro} em {data_devolucao} com {dias_atraso} de atraso")
            else:
                print(f"{aluno} fez a devolução do livro: {livro} em {data_devolucao}")

        print("-" * 100)

def exibir_historico_geral():
    if len(emprestimos) == 0:
        print("\nNão há movimentações registradas.")
        return

    ativos = aplicar_filtros(emprestimos, tipo="ativo")
    devolucoes = aplicar_filtros(emprestimos, tipo="devolucao")
    atrasos = aplicar_filtros(emprestimos, tipo="atraso")

    print("\n===== HISTÓRICO GERAL DE MOVIMENTAÇÕES =====")
    print(f"Empréstimos: {len(ativos)} | Devolução: {len(devolucoes)} | Atrasos: {len(atrasos)}\n")
    mostrar_registros(emprestimos)

    while True:
        escolha = input("\nDeseja filtrar os resultados exibidos? (S/N): ").strip().upper()
        if escolha in ("S", "N"):
            break
        print("Opção inválida! Digite apenas S ou N.")

    if escolha == "N":
        return

    while True:
        print("\nEscolha o tipo de filtro:")
        print("1 - Busca por Aluno (nome ou matrícula)")
        print("2 - Busca por Livro (título ou código)")
        print("3 - Busca por Movimentações (emprestimos, devoluções, atrasos)")
        print("4 - Cancelar")

        opc = input("Opção: ").strip()
        if opc not in ("1", "2", "3", "4"):
            print("Opção inválida!")
            continue

        if opc == "4":
            break

        if opc == "1":
            if len(alunos) == 0:
                print("\nNão há alunos cadastrados.")
                continue
            aluno_sel = buscar_aluno_historico(alunos)
            filtrados = aplicar_filtros(emprestimos, aluno=aluno_sel)
            print(f"\nResultados filtrados por aluno: {aluno_sel.nome} ({aluno_sel.matricula})\n")
            mostrar_registros(filtrados)
            break

        if opc == "2":
            if len(livros) == 0:
                print("\nNão há livros cadastrados.")
                continue
            livro_sel = buscar_livro_historico(livros)
            filtrados = aplicar_filtros(emprestimos, livro=livro_sel)
            print(f"\nResultados filtrados pelo livro: {livro_sel.titulo} ({livro_sel.codigo})\n")
            mostrar_registros(filtrados)
            break

        if opc == "3":
            print("\nSelecione o tipo de movimentação:")
            print("1 - Empréstimos ativos")
            print("2 - Devoluções")
            print("3 - Atrasos")
            opc_tipo = input("Opção: ").strip()
            if opc_tipo == "1":
                filtrados = aplicar_filtros(emprestimos, tipo='ativo')
                print("\nResultados: Empréstimos ativos\n")
                mostrar_registros(filtrados)
                break
            elif opc_tipo == "2":
                filtrados = aplicar_filtros(emprestimos, tipo='devolucao')
                print("\nResultados: Devoluções\n")
                mostrar_registros(filtrados)
                break
            elif opc_tipo == "3":
                filtrados = aplicar_filtros(emprestimos, tipo='atraso')
                print("\nResultados: Atrasos\n")
                mostrar_registros(filtrados)
                break
            else:
                print("Opção inválida!")

def buscar_livro_historico(livros):
    while True:
        busca = input("Digite o título ou código do livro selecionado: ").strip()

        livro_encontrado = None
        for livro in livros:
            if busca == livro.codigo or busca.lower() in livro.titulo.lower():
                livro_encontrado = livro
                break

        if livro_encontrado is not None:
            return livro_encontrado
        else:
            print("Livro não encontrado. Tente novamente.")