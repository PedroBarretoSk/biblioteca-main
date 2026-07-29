from flask import Blueprint, jsonify

from services import historico_service

historico_bp = Blueprint("historico", __name__, url_prefix="/historico")


@historico_bp.get("/")
def listar():
    return jsonify(historico_service.listar())
