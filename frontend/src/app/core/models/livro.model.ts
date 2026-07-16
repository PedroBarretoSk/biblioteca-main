export interface Livro {
  codigo: string;
  titulo: string;
  autor: string;
  categoria: string;
  disponivel: boolean;
}

export interface LivroPayload {
  codigo?: string;
  titulo: string;
  autor: string;
  categoria: string;
  disponivel: boolean;
}
