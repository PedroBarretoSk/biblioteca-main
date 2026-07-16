import json
import os

from models.livro import Livro
from models.aluno import Aluno
from models.emprestimo import Emprestimo

_BASE = os.path.join(os.path.dirname(__file__), "..", "data")

_LIVROS_FILE = os.path.join(_BASE, "livros.json")
_ALUNOS_FILE = os.path.join(_BASE, "alunos.json")
_EMPRESTIMOS_FILE = os.path.join(_BASE, "emprestimos.json")
_HISTORICO_FILE = os.path.join(_BASE, "historico.json")

livros: list[Livro] = []
alunos: list[Aluno] = []
emprestimos: list[Emprestimo] = []
historico: list[dict] = []


def _garantir_pasta() -> None:
    os.makedirs(_BASE, exist_ok=True)


def carregar_dados() -> None:
    _garantir_pasta()
    _carregar_livros()
    _carregar_alunos()
    _carregar_emprestimos()
    _carregar_historico()


def _carregar_livros() -> None:
    if not os.path.exists(_LIVROS_FILE):
        return
    with open(_LIVROS_FILE, "r", encoding="utf-8") as f:
        for item in json.load(f):
            livros.append(Livro.from_dict(item))


def _carregar_alunos() -> None:
    if not os.path.exists(_ALUNOS_FILE):
        return
    with open(_ALUNOS_FILE, "r", encoding="utf-8") as f:
        for item in json.load(f):
            alunos.append(Aluno.from_dict(item))


def _carregar_emprestimos() -> None:
    if not os.path.exists(_EMPRESTIMOS_FILE):
        return
    with open(_EMPRESTIMOS_FILE, "r", encoding="utf-8") as f:
        for item in json.load(f):
            emprestimos.append(Emprestimo.from_dict(item))


def _carregar_historico() -> None:
    if not os.path.exists(_HISTORICO_FILE):
        return
    with open(_HISTORICO_FILE, "r", encoding="utf-8") as f:
        historico.extend(json.load(f))


def salvar_livros() -> None:
    _garantir_pasta()
    with open(_LIVROS_FILE, "w", encoding="utf-8") as f:
        json.dump([l.to_dict() for l in livros], f, indent=4, ensure_ascii=False)


def salvar_alunos() -> None:
    _garantir_pasta()
    with open(_ALUNOS_FILE, "w", encoding="utf-8") as f:
        json.dump([a.to_dict() for a in alunos], f, indent=4, ensure_ascii=False)


def salvar_emprestimos() -> None:
    _garantir_pasta()
    with open(_EMPRESTIMOS_FILE, "w", encoding="utf-8") as f:
        json.dump([e.to_dict() for e in emprestimos], f, indent=4, ensure_ascii=False)


def salvar_historico() -> None:
    _garantir_pasta()
    with open(_HISTORICO_FILE, "w", encoding="utf-8") as f:
        json.dump(historico, f, indent=4, ensure_ascii=False)
