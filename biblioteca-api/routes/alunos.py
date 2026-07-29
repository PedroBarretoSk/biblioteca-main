from flask import Blueprint, jsonify, request

from services import aluno_service

alunos_bp = Blueprint("alunos", __name__, url_prefix="/alunos")


@alunos_bp.get("/")
def listar():
    return jsonify(aluno_service.listar())


@alunos_bp.get("/<matricula>")
def buscar(matricula: str):
    aluno = aluno_service.buscar(matricula)
    if not aluno:
        return jsonify({"erro": "Aluno não encontrado."}), 404
    return jsonify(aluno)


@alunos_bp.post("/")
def cadastrar():
    dados = request.get_json(silent=True) or {}
    try:
        aluno = aluno_service.cadastrar(dados)
        return jsonify(aluno), 201
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400


@alunos_bp.put("/<matricula>")
def editar(matricula: str):
    dados = request.get_json(silent=True) or {}
    try:
        aluno = aluno_service.editar(matricula, dados)
        return jsonify(aluno)
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400


@alunos_bp.delete("/<matricula>")
def remover(matricula: str):
    try:
        aluno_service.remover(matricula)
        return jsonify({"mensagem": "Aluno removido com sucesso."})
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400
