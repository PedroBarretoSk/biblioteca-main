class Aluno:
    def __init__(
        self,
        matricula: str,
        nome: str,
        turma: str,
        cpf: str,
        nome_mae: str,
        telefone: str,
    ):
        self.matricula = str(matricula).strip()
        self.nome = str(nome).strip()
        self.turma = str(turma).strip()
        self.cpf = str(cpf).strip()
        self.nome_mae = str(nome_mae).strip()
        self.telefone = str(telefone).strip()
        self.emprestimos_ativos = 0
        self.total_emprestimos = 0

    def to_dict(self) -> dict:
        return {
            "matricula": self.matricula,
            "nome": self.nome,
            "turma": self.turma,
            "cpf": self.cpf,
            "nome_mae": self.nome_mae,
            "telefone": self.telefone,
            "emprestimos_ativos": self.emprestimos_ativos,
            "total_emprestimos": self.total_emprestimos,
        }

    @staticmethod
    def from_dict(data: dict) -> "Aluno":
        aluno = Aluno(
            data["matricula"],
            data["nome"],
            data["turma"],
            data["cpf"],
            data["nome_mae"],
            data["telefone"],
        )
        aluno.emprestimos_ativos = data.get("emprestimos_ativos", 0)
        aluno.total_emprestimos = data.get("total_emprestimos", 0)
        return aluno
