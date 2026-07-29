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
    
   
    data_emp = livro_encontrado.data_emprestimo
    if isinstance(data_emp, str):
        data_emp = datetime.strptime(data_emp, "%d/%m/%Y %H:%M")

    dias_com_livro = (data_hoje - data_emp).days if data_emp else 0
    atraso = dias_com_livro - 7

    if atraso > 0:
       
        print(f"Livro em atraso há {atraso} dias.")
    else:
        atraso = 0
        print("Devolução dentro do prazo de 7 dias.")

    for registro in emprestimos:
        if registro['Livro'] == livro_encontrado and registro.get('data_devolucao', '') == '':
            aluno = registro['Aluno']
            if hasattr(aluno, 'emprestimos_ativos') and aluno.emprestimos_ativos > 0:
                aluno.emprestimos_ativos -= 1
            
            
            registro["data_devolucao"] = data_hoje.strftime("%d/%m/%Y %H:%M")
            registro["atrasou"] = "Sim" if atraso > 0 else "Não"
            registro["dias_atraso"] = atraso
            registro["id_livro"] = livro_encontrado.codigo
            registro["id_aluno"] = getattr(aluno, 'matricula', aluno)
            break

    livro_encontrado.disponivel = True
    livro_encontrado.data_emprestimo = None

    print(f"Sucesso! O livro '{livro_encontrado.titulo}' foi devolvido.")


def exibir_historico_devolucoes():
    print("\n========== HISTÓRICO DE DEVOLUÇÕES ==========")
    devolucoes = [reg for reg in emprestimos if reg.get('data_devolucao', '') != '']
    
    if not devolucoes:
        print("Nenhuma devolução registrada.")
        return

    for registro in devolucoes:
        aluno_nome = registro['Aluno'].nome if hasattr(registro['Aluno'], 'nome') else registro['Aluno']
        livro_titulo = registro['Livro'].titulo if hasattr(registro['Livro'], 'titulo') else registro['Livro']
        dias_atraso = registro.get('dias_atraso', 0)
        
        print(f"Aluno: {aluno_nome} | Livro: {livro_titulo} | Dias em atraso: {dias_atraso}")
