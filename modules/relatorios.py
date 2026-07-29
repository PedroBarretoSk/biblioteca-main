from dados import alunos, livros, emprestimos

class Relatorio:
    def __init__(self, listar_livros, listar_alunos, listar_emprestimos):
        self.listar_livros = listar_livros
        self.listar_alunos = listar_alunos
        self.listar_emprestimos = listar_emprestimos

    def livros_disponiveis(self):
        livros_disponiveis = [livro for livro in self.listar_livros() if livro.disponivel]
        if not livros_disponiveis:
            print("Nenhum livro disponível no momento.")
            return
        return livros_disponiveis

    def livros_emprestados(self):
        livros_emprestados = [livro for livro in self.listar_livros() if not livro.disponivel]
        if not livros_emprestados:
            print("Nenhum livro emprestado no momento.")
            return
        return livros_emprestados

    def ranking_alunos(self):
        ranking = sorted(
        ranking = sorted(
            self.listar_alunos(),
            key=lambda aluno: aluno.total_emprestimos,
            reverse=True
        )
        if not ranking:
        if not ranking:
            print("Nenhum aluno cadastrado no momento.")
            return
        return ranking

    def alunos_atrasados(self):
        atrasados = [reg for reg in self.listar_emprestimos() if reg.get("atrasou") == "Sim"]
        if not atrasados:
            print("Nenhum aluno com atraso no momento.")
            return
        return atrasados
    
    def livros_mais_emprestados(self):
        emprestimos = self.listar_emprestimos()
        if not emprestimos:
            print("Nenhum empréstimo registrado no momento.")
            return
        livros_count = {}
        for reg in emprestimos:
            livro = reg.get("Livro")
            if livro:
                livros_count[livro.titulo] = livros_count.get(livro.titulo, 0) + 1
        livros_mais_emprestados = sorted(livros_count.items(), key=lambda x: x[1], reverse=True)
        return livros_mais_emprestados

    def alunos_leitores(self):
        alunos_leitores = [aluno for aluno in self.listar_alunos() if aluno.total_emprestimos > 0]
        if not alunos_leitores:
            print("Nenhum aluno realizou empréstimos no momento.")
            return
        return alunos_leitores

    def estaticas_categorias(self):
        livros = self.listar_livros()
        if not livros:
            print("Nenhum livro cadastrado no momento.")
            return
        categorias_count = {}
        for livro in livros:
            categoria = livro.categoria
            categorias_count[categoria] = categorias_count.get(categoria, 0) + 1
        return categorias_count

    def estatistica_livros(self):
        emprestimos = self.listar_emprestimos()
        if not emprestimos:
            print("Nenhum empréstimo registrado no momento.")
            return
        livros_count = {}
        for reg in emprestimos:
            livro = reg.get("Livro")
            if livro:
                livros_count[livro] = livros_count.get(livro, 0) + 1
        return livros_count

        


def menu_relatorios():
    relatorio = Relatorio(lambda: livros, lambda: alunos, lambda: emprestimos)
    while True:
        print("\n--- Menu de Relatórios ---")
        print('1. Dashboard geral')
        print("2. Livros Disponíveis")
        print("3. Livros Emprestados")
        print("4. Ranking de Alunos")
        print("5. Atrasos")
        print("6. Livros Mais Emprestados")
        print("7. Alunos Leitores")
        print("8. Estatísticas por Categoria")
        print("9. Estatísticas de Livros")

        print("0. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            total_livros = len(livros)
            total_alunos = len(alunos)
            livros_disponiveis = len([livro for livro in livros if livro.disponivel])
            livros_emprestados = len([livro for livro in livros if not livro.disponivel])
            print("\n--- Dashboard Geral ---")
            print(f"Total de Livros: {total_livros}")
            print(f"Total de Alunos: {total_alunos}")
            print(f"Livros Disponíveis: {livros_disponiveis}")
            print(f"Livros Emprestados: {livros_emprestados}")

        elif opcao == "2":
            livros_disponiveis = relatorio.livros_disponiveis()
            if livros_disponiveis:
                print("\n--- Livros Disponíveis ---")
                for livro in livros_disponiveis:
                    print(f"Título: {livro.titulo}, Autor: {livro.autor}, Categoria: {livro.categoria}")

        elif opcao == "3":
            livros_emprestados = relatorio.livros_emprestados()
            if livros_emprestados:
                print("\n--- Livros Emprestados ---")
                for livro in livros_emprestados:
                    print(f"Título: {livro.titulo}, Autor: {livro.autor}, Categoria: {livro.categoria}")

        elif opcao == "4":
            ranking_alunos = relatorio.ranking_alunos()
            if ranking_alunos:
                print("\n--- Ranking de Alunos ---")
                for aluno in ranking_alunos:
                    print(f"Nome: {aluno.nome}, Total de Empréstimos: {aluno.total_emprestimos}")

        elif opcao == "5":
            alunos_atrasados = relatorio.alunos_atrasados()
            if alunos_atrasados:
                print("\n--- Alunos com Atrasos ---")
                for reg in alunos_atrasados:
                    print(f"Nome: {reg['Aluno'].nome}, Livro: {reg['Livro'].titulo}, Dias de Atraso: {reg['dias_atraso']}")

        elif opcao == '6':
            livros_mais_emprestados = relatorio.livros_mais_emprestados()
            if livros_mais_emprestados:
                print("\n--- Livros Mais Emprestados ---")
                for titulo, count in livros_mais_emprestados:
                    print(f"Título: {titulo}, Total de Empréstimos: {count}")

        elif opcao == '7':
            alunos_leitores = relatorio.alunos_leitores()
            if alunos_leitores:
                print("\n--- Alunos Leitores ---")
                for aluno in alunos_leitores:
                    print(f"Nome: {aluno.nome}, Total de Empréstimos: {aluno.total_emprestimos}")

        elif opcao == '8':
            categorias_count = relatorio.estaticas_categorias()
            if categorias_count:
                print("\n--- Estatísticas por Categoria ---")
                for categoria, count in categorias_count.items():
                    print(f"Categoria: {categoria}, Total de Livros: {count}")

        elif opcao == '9':
            livros_estatistica = relatorio.estatistica_livros()
            if livros_estatistica:
                print("\n--- Estatísticas de Livros ---")
                for livro, count in livros_estatistica.items():
                    print(f"Título: {livro.titulo}: {count} emprestados")
           
        elif opcao == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")
