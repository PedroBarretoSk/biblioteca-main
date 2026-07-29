export interface Emprestimo {
  id: number;
  aluno_matricula: string;
  livro_codigo: string;
  data_emprestimo: string;
  data_devolucao: string | null;
  atrasou: boolean | null;
  dias_atraso: number;
}

export interface EmprestimoPayload {
  aluno_matricula: string;
  livro_codigo: string;
}

export interface DevolucaoPayload {
  livro_codigo: string;
}
