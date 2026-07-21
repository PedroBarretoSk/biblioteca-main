# Frontend Biblioteca (Angular)

Aplicacao web da Biblioteca desenvolvida em Angular.

Objetivo: apresentar dados, enviar formularios e consumir a API REST. As regras de negocio ficam no backend.

## Visao Geral

- Stack: Angular 22, TypeScript, RxJS, SCSS
- UI: layout moderno em estilo Bento, responsivo
- Porta padrao de desenvolvimento: 4200
- Integracao API: http://localhost:8000

## Arquitetura

Estrutura principal:

- src/app/core/models: contratos de dados
- src/app/core/services: chamadas HTTP para backend
- src/app/core/config: configuracoes globais da API
- src/app/features: paginas por contexto
- src/app/shared/components: componentes reutilizaveis (menu)

Roteamento da aplicacao:

- /dashboard
- /livros
- /alunos
- /emprestimos
- /historico
- /relatorios

## Padroes e Arquiteturas Utilizados

- Feature-First Organization: funcionalidades organizadas por contexto em `src/app/features/*`.
- Core/Shared Split: `core/` para contratos e servicos globais; `shared/` para componentes reutilizaveis.
- Service as API Gateway (client-side): servicos Angular centralizam chamadas HTTP, timeout e tratamento de erro.
- Model/DTO Contracts: interfaces TypeScript em `core/models` definem o contrato entre frontend e backend.
- Smart Page Components: paginas coordenam estado de tela e formularios; componentes compartilhados focam reutilizacao visual.
- Reactive Programming com RxJS: consumo HTTP e fluxo assincrono com `Observable`, `finalize`, `catchError`.
- State via Signals: estado local de UI com `signal(...)` para listas, loading e mensagens de erro.
- Lazy Loading de Rotas: carregamento sob demanda via `loadComponent` para reduzir custo inicial.
- UI Design System (Bento): tokens visuais e componentes de layout padronizados em `src/styles.scss`.
- Responsividade Mobile-First: grid adaptativo para formularios e tabelas em desktop e mobile.

Decisoes arquiteturais importantes:

- Frontend sem regra de negocio de dominio: validacao critica e regras de processo estao no backend.
- Separacao de preocupacoes: pagina exibe/interage, servico comunica, backend decide regra.
- Contrato HTTP estavel: facilita troca da camada de persistencia backend sem quebrar a aplicacao web.

## Integracao com Backend

Configuracao central em src/app/core/config/app-settings.ts:

- apiBaseUrl: http://localhost:8000
- requestTimeoutMs: 8000

O frontend consome os recursos:

- /livros
- /alunos
- /emprestimos
- /devolucoes
- /historico
- /relatorios

## Como Executar (Desenvolvimento)

No diretorio frontend:

1. Instalar dependencias:

npm install

2. Rodar aplicacao:

npm run start

Aplicacao disponivel em:

http://localhost:4200

Opcional (com proxy):

npm run start:proxy

## Build

Gerar build de producao:

npm run build

Build gerada em:

dist/

Build de desenvolvimento em watch:

npm run watch

## Testes

Executar testes:

npm run test

## Fluxo do Projeto

Exemplo: cadastro de livro

1. Usuario envia formulario em /livros
2. Frontend chama POST /livros/
3. Backend valida e persiste
4. Frontend atualiza listagem

## Observacoes

- O frontend nao deve conter regra de negocio critica.
- Validacoes de negocio sao aplicadas no backend.
- Para funcionamento completo, backend e frontend devem estar ativos simultaneamente.
