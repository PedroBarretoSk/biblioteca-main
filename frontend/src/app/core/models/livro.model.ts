export interface Livro {
  id: number;
  titulo: string;
  autor: string;
  anoPublicacao: number;
  disponivel: boolean;
}

export interface LivroPayload {
  titulo: string;
  autor: string;
  anoPublicacao: number;
  disponivel: boolean;
}
