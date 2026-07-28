from dados import alunos, livros
 
class Relatorio:
    def __init__(self, listar_livros, listar_alunos):
        self.listar_livros = listar_livros
        self.listar_alunos = listar_alunos
 
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
            self.listar_alunos(),
            key=lambda aluno: aluno.total_emprestimos,
            reverse=True
        )
        if not ranking:
            print("Nenhum aluno cadastrado no momento.")
            return
        return ranking

    def alunos_atrasados(self):
        alunos_atrasados = [aluno for aluno in self.listar_alunos() if aluno.total_emprestimos_atrasados > 0]
        if not alunos_atrasados:
            print("Nenhum aluno com empréstimos atrasados no momento.")
            return
        return alunos_atrasados

        


 
def menu_relatorios():
    relatorio = Relatorio(lambda: livros, lambda: alunos)
    while True:
        print("\n--- Menu de Relatórios ---")
        print('1. Dashboard geral')
        print("2. Livros Disponíveis")
        print("3. Livros Emprestados")
        print("4. Ranking de Alunos")
        print("5. Atrasos")
        print("6. Histórico de Devolução")
     
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
                print("\n--- Alunos com Empréstimos Atrasados ---")
                for aluno in alunos_atrasados:
                    print(f"Nome: {aluno.nome}, Total de Empréstimos Atrasados: {aluno.total_emprestimos_atrasados}")
            
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")
