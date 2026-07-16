from models.aluno import Aluno
from repository import json_repository as repo
from services.historico_service import registrar
from utils.validacoes import validar_matricula, validar_texto, validar_cpf, validar_telefone


def listar() -> list[dict]:
    return [a.to_dict() for a in repo.alunos]


def buscar(matricula: str) -> dict | None:
    aluno = _encontrar(matricula)
    return aluno.to_dict() if aluno else None


def cadastrar(dados: dict) -> dict:
    matricula = str(dados.get("matricula", "")).strip()
    nome = str(dados.get("nome", "")).strip()
    turma = str(dados.get("turma", "")).strip()
    cpf = str(dados.get("cpf", "")).strip()
    nome_mae = str(dados.get("nome_mae", "")).strip()
    telefone = str(dados.get("telefone", "")).strip()

    if not validar_matricula(matricula):
        raise ValueError("Matrícula inválida.")
    if not validar_texto(nome, 3):
        raise ValueError("Nome inválido.")
    if not validar_texto(turma):
        raise ValueError("Turma inválida.")
    if not validar_cpf(cpf):
        raise ValueError("CPF inválido.")

    tel = validar_telefone(telefone)
    if tel is None:
        raise ValueError("Telefone inválido.")

    if any(a.matricula == matricula for a in repo.alunos):
        raise ValueError(f"Já existe um aluno com a matrícula {matricula}.")

    cpf_limpo = cpf.replace(".", "").replace("-", "")
    if any(a.cpf == cpf_limpo for a in repo.alunos):
        raise ValueError("CPF já cadastrado.")

    aluno = Aluno(matricula, nome, turma, cpf_limpo, nome_mae, tel)
    repo.alunos.append(aluno)
    repo.salvar_alunos()
    registrar("cadastro", f"Aluno cadastrado: {matricula} - {nome}")
    return aluno.to_dict()


def editar(matricula: str, dados: dict) -> dict:
    aluno = _encontrar(matricula)
    if not aluno:
        raise ValueError("Aluno não encontrado.")

    nome = str(dados.get("nome", aluno.nome)).strip()
    turma = str(dados.get("turma", aluno.turma)).strip()
    nome_mae = str(dados.get("nome_mae", aluno.nome_mae)).strip()
    telefone = str(dados.get("telefone", aluno.telefone)).strip()

    if not validar_texto(nome, 3):
        raise ValueError("Nome inválido.")
    if not validar_texto(turma):
        raise ValueError("Turma inválida.")

    tel = validar_telefone(telefone)
    if tel is None:
        raise ValueError("Telefone inválido.")

    aluno.nome = nome
    aluno.turma = turma
    aluno.nome_mae = nome_mae
    aluno.telefone = tel

    repo.salvar_alunos()
    registrar("edicao", f"Aluno editado: {matricula} - {nome}")
    return aluno.to_dict()


def remover(matricula: str) -> None:
    aluno = _encontrar(matricula)
    if not aluno:
        raise ValueError("Aluno não encontrado.")

    if aluno.emprestimos_ativos > 0:
        raise ValueError("Aluno possui empréstimos ativos e não pode ser removido.")

    repo.alunos.remove(aluno)
    repo.salvar_alunos()
    registrar("exclusao", f"Aluno removido: {matricula} - {aluno.nome}")


def _encontrar(matricula: str) -> Aluno | None:
    for aluno in repo.alunos:
        if aluno.matricula == matricula:
            return aluno
    return None
