class Livro:
    def __init__(self, codigo: str, titulo: str, autor: str, categoria: str):
        self.codigo = str(codigo).strip()
        self.titulo = str(titulo).strip()
        self.autor = str(autor).strip()
        self.categoria = str(categoria).strip()
        self.disponivel = True

    def to_dict(self) -> dict:
        return {
            "codigo": self.codigo,
            "titulo": self.titulo,
            "autor": self.autor,
            "categoria": self.categoria,
            "disponivel": self.disponivel,
        }

    @staticmethod
    def from_dict(data: dict) -> "Livro":
        livro = Livro(data["codigo"], data["titulo"], data["autor"], data["categoria"])
        livro.disponivel = data.get("disponivel", True)
        return livro
