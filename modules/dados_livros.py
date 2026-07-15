import json
import os
from dados import livros
from models.Livro import Livro

LIVROS = "livros.json"

def salvar_livros():
    try:
        with open(LIVROS, "w", encoding="utf-8") as f:
            json.dump([livro.transformar_dict() for livro in livros], f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Erro ao salvar livros: {e}")

def carregar_livros():
    if not os.path.exists(LIVROS):
        return

    try:
        with open(LIVROS, "r", encoding="utf-8") as f:
            dados = json.load(f)
            livros.clear()
            for item in dados:
                livros.append(Livro.from_dict(item))
    except Exception as e:
        print(f"Erro ao carregar livros: {e}")