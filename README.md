# biblioteca-main

Projeto de biblioteca (monolito) com backend em Python e frontend em Angular + TypeScript.

## Estrutura

- Backend Python: raiz do projeto (main.py, models, modules, dados.py)
- Frontend Angular: pasta frontend

## Frontend

Para executar o frontend:

1. Entre na pasta frontend
2. Rode npm install
3. Rode npm run start

Para detalhes de arquitetura e integracao REST/mock, consulte frontend/README.md.

## Backend

1. Acesse a pasta do projeto
```bash
cd biblioteca-main
cd biblioteca-api
```

2. Instale as dependências 
```bash
pip install -r requirements.txt
```

3. Execute a aplicação 
```bash
python app.py
```
4. Acessando a aplicação
```bash
htpp://localhost:4200
```