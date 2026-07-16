from flask import Flask
from flask_cors import CORS

from repository.json_repository import carregar_dados
from routes.livros import livros_bp
from routes.alunos import alunos_bp
from routes.emprestimos import emprestimos_bp
from routes.devolucoes import devolucoes_bp
from routes.historico import historico_bp
from routes.relatorios import relatorios_bp

app = Flask(__name__)
CORS(app)

carregar_dados()

app.register_blueprint(livros_bp)
app.register_blueprint(alunos_bp)
app.register_blueprint(emprestimos_bp)
app.register_blueprint(devolucoes_bp)
app.register_blueprint(historico_bp)
app.register_blueprint(relatorios_bp)

if __name__ == "__main__":
    app.run(debug=True, port=8000)
