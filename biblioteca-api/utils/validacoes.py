def validar_codigo(codigo: str) -> bool:
    codigo = codigo.strip()
    return bool(codigo) and codigo.isnumeric()


def validar_texto(texto: str, minimo: int = 2) -> bool:
    texto = texto.strip()
    return bool(texto) and not texto.isnumeric() and len(texto) >= minimo


def validar_matricula(matricula: str) -> bool:
    return bool(matricula.strip())


def validar_cpf(cpf: str) -> bool:
    cpf = cpf.replace(".", "").replace("-", "").strip()
    return len(cpf) == 11 and cpf.isdigit()


def validar_telefone(telefone: str) -> str | None:
    tel = (
        telefone.replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
        .strip()
    )
    if not tel.isdigit():
        return None
    if len(tel) not in (10, 11):
        return None
    return tel
