# Biblioteca API (Backend)

API REST da Biblioteca em Python com Flask.

Objetivo: centralizar toda a regra de negocio no backend (camada de services), mantendo rotas enxutas e frontend apenas como consumidor HTTP.

## Visao Geral

- Stack: Python, Flask, Flask-CORS
- Persistencia: JSON em disco (pasta data)
- Porta padrao: 8000
- Arquivo de entrada: app.py

## Arquitetura

Estrutura principal:

- app.py: bootstrap da API, CORS e registro de blueprints
- models/: entidades de dominio
- services/: regras de negocio e validacoes de fluxo
- repository/: leitura e escrita de dados JSON
- routes/: endpoints REST (sem regra de negocio)
- utils/: validacoes reutilizaveis

Fluxo de requisicao:

1. Route recebe HTTP
2. Service valida e aplica regras
3. Repository persiste/consulta JSON
4. Service retorna resposta para a Route

## Padroes e Arquiteturas Utilizados

- Arquitetura em Camadas (Layered Architecture): separacao clara entre `routes`, `services`, `repository` e `models`.
- Service Layer Pattern: toda regra de negocio fica em `services/`; `routes/` apenas orquestram request/response HTTP.
- Repository Pattern: `repository/json_repository.py` encapsula persistencia e acesso aos arquivos JSON.
- Domain Model Pattern: entidades (`Livro`, `Aluno`, `Emprestimo`) representam o dominio com `to_dict/from_dict`.
- Single Responsibility Principle (SRP): cada modulo tem responsabilidade unica (validar, persistir, expor endpoint etc.).
- Fail Fast Validation: validacoes de entrada e regras de fluxo retornam erro cedo via `ValueError`.
- REST API Style: recursos expostos por endpoints padronizados por contexto (`/livros`, `/alunos`, ...).
- History as Audit Trail: `historico` funciona como trilha de auditoria de eventos de negocio (nao apagavel por fluxo normal).

Decisoes arquiteturais importantes:

- Frontend sem regra de negocio critica: regra centralizada no backend para manter consistencia.
- Persistencia simples em JSON: adequada para ambiente academico/POC; pode evoluir para banco relacional sem alterar contrato HTTP.
- Blueprint por contexto: modularizacao de rotas Flask para facilitar evolucao por dominio.

## Regras de Negocio (Resumo)

Livro:

- codigo unico
- titulo, autor e categoria obrigatorios
- disponivel inicia como true
- nao permite codigo duplicado

Aluno:

- matricula unica
- nome e turma obrigatorios
- CPF e telefone validados

Emprestimo:

- aluno deve existir
- livro deve existir
- livro precisa estar disponivel
- limite de 3 emprestimos ativos por aluno
- ao emprestar: livro.disponivel = false

Devolucao:

- exige emprestimo ativo
- ao devolver: livro.disponivel = true
- calcula atraso com prazo de 7 dias

Historico:

- registra cadastro, edicao, exclusao, emprestimo e devolucao
- historico nao e apagado

Relatorios:

- somente leitura dos dados cadastrados

## Endpoints

Livros:

- GET /livros/
- GET /livros/{codigo}
- POST /livros/
- PUT /livros/{codigo}
- DELETE /livros/{codigo}

Alunos:

- GET /alunos/
- GET /alunos/{matricula}
- POST /alunos/
- PUT /alunos/{matricula}
- DELETE /alunos/{matricula}

Emprestimos:

- GET /emprestimos/
- GET /emprestimos/ativos
- POST /emprestimos/

Devolucoes:

- POST /devolucoes/

Historico:

- GET /historico/

Relatorios:

- GET /relatorios/dashboard
- GET /relatorios/livros
- GET /relatorios/alunos
- GET /relatorios/categorias

## Como Executar (Desenvolvimento)

No diretorio biblioteca-api:

1. Criar ambiente virtual:

Windows (PowerShell):

python -m venv .venv

2. Ativar ambiente:

Windows (PowerShell):

.\.venv\Scripts\Activate.ps1

3. Instalar dependencias:

pip install -r requirements.txt

4. Rodar servidor:

python app.py

API disponivel em:

http://127.0.0.1:8000

## Build e Deploy

Esta API nao possui etapa de build obrigatoria (e interpretada em Python).

Para producao:

- use um servidor WSGI (ex.: gunicorn ou waitress)
- desative debug=True
- configure CORS para dominios especificos

## Dados Persistidos

A pasta data armazena:

- livros.json
- alunos.json
- emprestimos.json
- historico.json

Se os arquivos nao existirem, sao criados automaticamente conforme uso da aplicacao.
