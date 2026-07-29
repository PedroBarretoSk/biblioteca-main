from models.livro import Livro
from repository import json_repository as repo
from services.historico_service import registrar
from utils.validacoes import validar_codigo, validar_texto


def listar() -> list[dict]:
    return [l.to_dict() for l in repo.livros]


def buscar(codigo: str) -> dict | None:
    livro = _encontrar(codigo)
    return livro.to_dict() if livro else None


def cadastrar(dados: dict) -> dict:
    codigo = str(dados.get("codigo", "")).strip()
    titulo = str(dados.get("titulo", "")).strip()
    autor = str(dados.get("autor", "")).strip()
    categoria = str(dados.get("categoria", "")).strip()

    if not validar_codigo(codigo):
        raise ValueError("Código inválido. Use apenas números positivos.")
    if not validar_texto(titulo):
        raise ValueError("Título inválido.")
    if not validar_texto(autor):
        raise ValueError("Autor inválido.")
    if not validar_texto(categoria):
        raise ValueError("Categoria inválida.")

    if any(l.codigo == codigo for l in repo.livros):
        raise ValueError(f"Já existe um livro com o código {codigo}.")

    if any(
        l.titulo.lower() == titulo.lower() and l.autor.lower() == autor.lower()
        for l in repo.livros
    ):
        raise ValueError(f'O livro "{titulo}" do autor "{autor}" já está cadastrado.')

    livro = Livro(codigo, titulo, autor, categoria)
    repo.livros.append(livro)
    repo.salvar_livros()
    registrar("cadastro", f"Livro cadastrado: [{codigo}] {titulo}")
    return livro.to_dict()


def editar(codigo: str, dados: dict) -> dict:
    livro = _encontrar(codigo)
    if not livro:
        raise ValueError("Livro não encontrado.")

    titulo = str(dados.get("titulo", livro.titulo)).strip()
    autor = str(dados.get("autor", livro.autor)).strip()
    categoria = str(dados.get("categoria", livro.categoria)).strip()
    disponivel = bool(dados.get("disponivel", livro.disponivel))

    if not validar_texto(titulo):
        raise ValueError("Título inválido.")
    if not validar_texto(autor):
        raise ValueError("Autor inválido.")
    if not validar_texto(categoria):
        raise ValueError("Categoria inválida.")

    livro.titulo = titulo
    livro.autor = autor
    livro.categoria = categoria
    livro.disponivel = disponivel

    repo.salvar_livros()
    registrar("edicao", f"Livro editado: [{codigo}] {titulo}")
    return livro.to_dict()


def remover(codigo: str) -> None:
    livro = _encontrar(codigo)
    if not livro:
        raise ValueError("Livro não encontrado.")

    repo.livros.remove(livro)
    repo.salvar_livros()
    registrar("exclusao", f"Livro removido: [{codigo}] {livro.titulo}")


def _encontrar(codigo: str) -> Livro | None:
    for livro in repo.livros:
        if livro.codigo == codigo:
            return livro
    return None
