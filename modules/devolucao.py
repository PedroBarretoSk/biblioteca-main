from datetime import datetime
from dados import livros, emprestimos

def devolver_livro():
    print("\n========== DEVOLVER LIVRO ==========")
    codigo = input("Digite o código do livro: ").strip()

    livro_encontrado = None
    for livro in livros:
        if str(livro.codigo) == codigo:
            livro_encontrado = livro
            break
    
    if livro_encontrado is None:
        print("Erro: Livro não encontrado.")
        return
        
    if livro_encontrado.disponivel:
        print("Aviso: Este livro já está na prateleira.")
        return

    data_hoje = datetime.now()
    dias_com_livro = (data_hoje - livro_encontrado.data_emprestimo).days
    atraso = dias_com_livro - 7

    if atraso > 0:
        print(f"Atenção: Devolvido com {atraso} dia(s) de atraso!")
    else:
        atraso = 0
        print("Devolução dentro do prazo de 7 dias.")

    for registro in emprestimos:
        if registro['Livro'] == livro_encontrado and registro.get('data_devolucao', '') == '':
            aluno = registro['Aluno']
            if aluno.emprestimos_ativos > 0:
                aluno.emprestimos_ativos -= 1
            
            registro["data_devolucao"] = data_hoje.strftime("%d/%m/%Y %H:%M")
            registro["atrasou"] = "Sim" if atraso > 0 else "Não"
            registro["dias_atraso"] = f"{atraso} dia(s)"
            registro["id_livro"] = livro_encontrado.codigo
            registro["id_aluno"] = aluno.matricula
            break

    livro_encontrado.disponivel = True
    livro_encontrado.data_emprestimo = None

    print(f"Sucesso! O livro '{livro_encontrado.titulo}' foi devolvido.")
