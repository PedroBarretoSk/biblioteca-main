from flask import Blueprint, jsonify

from services import relatorio_service

relatorios_bp = Blueprint("relatorios", __name__, url_prefix="/relatorios")


@relatorios_bp.get("/dashboard")
def dashboard():
    return jsonify(relatorio_service.dashboard())


@relatorios_bp.get("/livros")
def livros():
    return jsonify(relatorio_service.livros())


@relatorios_bp.get("/alunos")
def alunos():
    return jsonify(relatorio_service.alunos())


@relatorios_bp.get("/categorias")
def categorias():
    return jsonify(relatorio_service.categorias())
