from flask import Blueprint, jsonify, request

from services import livro_service

livros_bp = Blueprint("livros", __name__, url_prefix="/livros")


@livros_bp.get("/")
def listar():
    return jsonify(livro_service.listar())


@livros_bp.get("/<codigo>")
def buscar(codigo: str):
    livro = livro_service.buscar(codigo)
    if not livro:
        return jsonify({"erro": "Livro não encontrado."}), 404
    return jsonify(livro)


@livros_bp.post("/")
def cadastrar():
    dados = request.get_json(silent=True) or {}
    try:
        livro = livro_service.cadastrar(dados)
        return jsonify(livro), 201
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400


@livros_bp.put("/<codigo>")
def editar(codigo: str):
    dados = request.get_json(silent=True) or {}
    try:
        livro = livro_service.editar(codigo, dados)
        return jsonify(livro)
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400


@livros_bp.delete("/<codigo>")
def remover(codigo: str):
    try:
        livro_service.remover(codigo)
        return jsonify({"mensagem": "Livro removido com sucesso."})
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400
