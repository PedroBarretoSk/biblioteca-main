from datetime import datetime

from models.emprestimo import Emprestimo
from repository import json_repository as repo
from services.historico_service import registrar

MAX_EMPRESTIMOS_ALUNO = 3


def listar() -> list[dict]:
    return [e.to_dict() for e in repo.emprestimos]


def listar_ativos() -> list[dict]:
    return [e.to_dict() for e in repo.emprestimos if e.data_devolucao is None]


def realizar(dados: dict) -> dict:
    matricula = str(dados.get("aluno_matricula", "")).strip()
    codigo = str(dados.get("livro_codigo", "")).strip()

    aluno = next((a for a in repo.alunos if a.matricula == matricula), None)
    if not aluno:
        raise ValueError("Aluno não encontrado.")

    livro = next((l for l in repo.livros if l.codigo == codigo), None)
    if not livro:
        raise ValueError("Livro não encontrado.")

    if not livro.disponivel:
        raise ValueError("Livro indisponível para empréstimo.")

    if aluno.emprestimos_ativos >= MAX_EMPRESTIMOS_ALUNO:
        raise ValueError(
            f"Aluno já possui {MAX_EMPRESTIMOS_ALUNO} empréstimos ativos."
        )

    novo_id = max((e.id for e in repo.emprestimos), default=0) + 1
    data = datetime.now().strftime("%d/%m/%Y %H:%M")

    emprestimo = Emprestimo(novo_id, matricula, codigo, data)
    repo.emprestimos.append(emprestimo)

    livro.disponivel = False
    aluno.emprestimos_ativos += 1
    aluno.total_emprestimos += 1

    repo.salvar_emprestimos()
    repo.salvar_livros()
    repo.salvar_alunos()

    registrar("emprestimo", f"Empréstimo: {aluno.nome} pegou [{codigo}] {livro.titulo}")
    return emprestimo.to_dict()
