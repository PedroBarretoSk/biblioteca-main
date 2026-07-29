from flask import Blueprint, jsonify, request

from services import devolucao_service

devolucoes_bp = Blueprint("devolucoes", __name__, url_prefix="/devolucoes")


@devolucoes_bp.post("/")
def devolver():
    dados = request.get_json(silent=True) or {}
    try:
        resultado = devolucao_service.devolver(dados)
        return jsonify(resultado)
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400
