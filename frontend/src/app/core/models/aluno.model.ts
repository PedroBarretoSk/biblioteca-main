export interface Aluno {
  matricula: string;
  nome: string;
  turma: string;
  cpf: string;
  nome_mae: string;
  telefone: string;
  emprestimos_ativos: number;
  total_emprestimos: number;
}

export interface AlunoPayload {
  matricula?: string;
  nome: string;
  turma: string;
  cpf: string;
  nome_mae: string;
  telefone: string;
}
