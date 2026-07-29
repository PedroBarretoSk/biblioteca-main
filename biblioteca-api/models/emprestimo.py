class Emprestimo:
    def __init__(
        self,
        id: int,
        aluno_matricula: str,
        livro_codigo: str,
        data_emprestimo: str,
    ):
        self.id = id
        self.aluno_matricula = aluno_matricula
        self.livro_codigo = livro_codigo
        self.data_emprestimo = data_emprestimo
        self.data_devolucao: str | None = None
        self.atrasou: bool | None = None
        self.dias_atraso: int = 0

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "aluno_matricula": self.aluno_matricula,
            "livro_codigo": self.livro_codigo,
            "data_emprestimo": self.data_emprestimo,
            "data_devolucao": self.data_devolucao,
            "atrasou": self.atrasou,
            "dias_atraso": self.dias_atraso,
        }

    @staticmethod
    def from_dict(data: dict) -> "Emprestimo":
        emp = Emprestimo(
            data["id"],
            data["aluno_matricula"],
            data["livro_codigo"],
            data["data_emprestimo"],
        )
        emp.data_devolucao = data.get("data_devolucao")
        emp.atrasou = data.get("atrasou")
        emp.dias_atraso = data.get("dias_atraso", 0)
        return emp
