export interface Dashboard {
  total_livros: number;
  livros_disponiveis: number;
  livros_emprestados: number;
  total_alunos: number;
  emprestimos_ativos: number;
}

export interface RelatorioCategorias {
  categoria: string;
  total: number;
}
