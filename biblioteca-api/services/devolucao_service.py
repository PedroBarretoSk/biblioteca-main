from datetime import datetime

from repository import json_repository as repo
from services.historico_service import registrar

PRAZO_DIAS = 7


def devolver(dados: dict) -> dict:
    codigo = str(dados.get("livro_codigo", "")).strip()

    livro = next((l for l in repo.livros if l.codigo == codigo), None)
    if not livro:
        raise ValueError("Livro não encontrado.")

    if livro.disponivel:
        raise ValueError("Este livro já está na prateleira.")

    emprestimo = next(
        (e for e in repo.emprestimos if e.livro_codigo == codigo and e.data_devolucao is None),
        None,
    )
    if not emprestimo:
        raise ValueError("Empréstimo ativo não encontrado.")

    aluno = next(
        (a for a in repo.alunos if a.matricula == emprestimo.aluno_matricula), None
    )

    data_emp = datetime.strptime(emprestimo.data_emprestimo, "%d/%m/%Y %H:%M")
    data_dev = datetime.now()
    dias = (data_dev - data_emp).days
    atraso = max(0, dias - PRAZO_DIAS)

    emprestimo.data_devolucao = data_dev.strftime("%d/%m/%Y %H:%M")
    emprestimo.atrasou = atraso > 0
    emprestimo.dias_atraso = atraso

    livro.disponivel = True
    if aluno and aluno.emprestimos_ativos > 0:
        aluno.emprestimos_ativos -= 1

    repo.salvar_emprestimos()
    repo.salvar_livros()
    if aluno:
        repo.salvar_alunos()

    msg = f"Devolução: [{codigo}] {livro.titulo}"
    if atraso > 0:
        msg += f" — {atraso} dia(s) de atraso"
    registrar("devolucao", msg)
    return emprestimo.to_dict()
