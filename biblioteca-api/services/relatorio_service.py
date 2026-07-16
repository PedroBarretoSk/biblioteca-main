from repository import json_repository as repo


def dashboard() -> dict:
    total_livros = len(repo.livros)
    disponiveis = sum(1 for l in repo.livros if l.disponivel)
    emprestados = total_livros - disponiveis
    total_alunos = len(repo.alunos)
    emprestimos_ativos = sum(1 for e in repo.emprestimos if e.data_devolucao is None)

    return {
        "total_livros": total_livros,
        "livros_disponiveis": disponiveis,
        "livros_emprestados": emprestados,
        "total_alunos": total_alunos,
        "emprestimos_ativos": emprestimos_ativos,
    }


def livros() -> list[dict]:
    return [l.to_dict() for l in repo.livros]


def alunos() -> list[dict]:
    return sorted(
        [a.to_dict() for a in repo.alunos],
        key=lambda a: a["total_emprestimos"],
        reverse=True,
    )


def categorias() -> list[dict]:
    contagem: dict[str, int] = {}
    for livro in repo.livros:
        contagem[livro.categoria] = contagem.get(livro.categoria, 0) + 1

    return [
        {"categoria": cat, "total": total}
        for cat, total in sorted(contagem.items(), key=lambda x: x[1], reverse=True)
    ]
