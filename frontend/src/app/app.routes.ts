import { Routes } from '@angular/router';

export const routes: Routes = [
  {
    path: '',
    pathMatch: 'full',
    redirectTo: 'dashboard'
  },
  {
    path: 'dashboard',
    loadComponent: () =>
      import('./features/dashboard/pages/dashboard-page.component').then(
        (m) => m.DashboardPageComponent
      )
  },
  {
    path: 'livros',
    loadComponent: () =>
      import('./features/livros/pages/livros-page.component').then(
        (m) => m.LivrosPageComponent
      )
  },
  {
    path: 'alunos',
    loadComponent: () =>
      import('./features/alunos/pages/alunos-page.component').then(
        (m) => m.AlunosPageComponent
      )
  },
  {
    path: 'emprestimos',
    loadComponent: () =>
      import('./features/emprestimos/pages/emprestimos-page.component').then(
        (m) => m.EmprestimosPageComponent
      )
  },
  {
    path: 'historico',
    loadComponent: () =>
      import('./features/historico/pages/historico-page.component').then(
        (m) => m.HistoricoPageComponent
      )
  },
  {
    path: 'relatorios',
    loadComponent: () =>
      import('./features/relatorios/pages/relatorios-page.component').then(
        (m) => m.RelatoriosPageComponent
      )
  },
  {
    path: '**',
    redirectTo: 'dashboard'
  }
];
