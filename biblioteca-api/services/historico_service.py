from datetime import datetime

from repository import json_repository as repo


def listar() -> list[dict]:
    return list(repo.historico)


def registrar(tipo: str, descricao: str) -> None:
    entrada = {
        "id": len(repo.historico) + 1,
        "tipo": tipo,
        "descricao": descricao,
        "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
    }
    repo.historico.append(entrada)
    repo.salvar_historico()
