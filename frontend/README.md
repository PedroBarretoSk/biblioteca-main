# Frontend Angular

Frontend responsivo em Angular + TypeScript para o monolito da biblioteca, sem alterar regras do backend Python.

## Arquitetura

Estrutura principal:

- src/app/core/config: configuracao de API e modo mock
- src/app/core/models: contratos de dados (DTO/interfaces)
- src/app/core/services: camada de acesso HTTP/JSON
- src/app/features/livros/pages: pagina de listagem e CRUD de livros

Roteamento:

- rota principal redireciona para /livros

## Integracao API e JSON

A configuracao central esta em src/app/core/config/app-settings.ts.

- useMockData: true
	usa JSON local em public/mock/livros.json
- useMockData: false
	usa API REST em http://localhost:8000/api/livros

Operacoes implementadas no servico:

- GET: listagem
- POST: criacao
- PUT: atualizacao
- DELETE: remocao

## Executar

No diretorio frontend:

- npm install
- npm run start

Para usar proxy e evitar CORS no desenvolvimento:

- npm run start:proxy

Build de producao:

- npm run build

## Observacoes

- O backend Python atual nao foi alterado.
- O frontend foi preparado para consumir API nivel 2 (recursos + verbos HTTP) e tambem funcionar com JSON local inicialmente.
