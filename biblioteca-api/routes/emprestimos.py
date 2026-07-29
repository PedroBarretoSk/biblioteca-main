from flask import Blueprint, jsonify, request

from services import emprestimo_service

emprestimos_bp = Blueprint("emprestimos", __name__, url_prefix="/emprestimos")


@emprestimos_bp.get("/")
def listar():
    return jsonify(emprestimo_service.listar())


@emprestimos_bp.get("/ativos")
def listar_ativos():
    return jsonify(emprestimo_service.listar_ativos())


@emprestimos_bp.post("/")
def realizar():
    dados = request.get_json(silent=True) or {}
    try:
        emprestimo = emprestimo_service.realizar(dados)
        return jsonify(emprestimo), 201
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400
