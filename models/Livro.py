class Livro:
    def __init__(self, codigo: str, titulo: str, autor: str, categoria: str):
        self.codigo = str(codigo).strip()
        self.titulo = str(titulo).strip()
        self.autor = str(autor).strip()
        self.categoria = str(categoria).strip()
        self.disponivel = True

    def exibir_detalhes(self):
        status = "Disponível" if self.disponivel else "Indisponível"
        print(f"[{self.codigo}] {self.titulo} - Autor: {self.autor} | Cat: {self.categoria} | Status: {status}")


    def transformar_dict(self):
        return {
            "codigo": self.codigo,
            "titulo": self.titulo,
            "autor": self.autor,
            "categoria": self.categoria,
            "disponivel": self.disponivel
        }

    @staticmethod
    def from_dict(dados: dict):
        livro = Livro(dados["codigo"], dados["titulo"], dados["autor"], dados["categoria"])
        livro.disponivel = dados.get("disponivel", True)
        return livro