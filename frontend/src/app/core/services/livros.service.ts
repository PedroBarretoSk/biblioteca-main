import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, TimeoutError, catchError, throwError, timeout } from 'rxjs';
import { appSettings } from '../config/app-settings';
import { Livro, LivroPayload } from '../models/livro.model';

@Injectable({ providedIn: 'root' })
export class LivrosService {
  private readonly endpoint = `${appSettings.apiBaseUrl}/livros`;

  constructor(private readonly http: HttpClient) {}

  list(): Observable<Livro[]> {
    return this.http.get<Livro[]>(`${this.endpoint}/`).pipe(
      timeout(appSettings.requestTimeoutMs),
      catchError((error) => this.handleError('Falha ao listar livros', error))
    );
  }

 
  getByCodigo(codigo: string): Observable<Livro> {
    return this.http.get<Livro>(`${this.endpoint}/${codigo}`).pipe(
      timeout(appSettings.requestTimeoutMs),
      catchError((error) => this.handleError('Falha ao buscar livro por código', error))
    );
  }

 
  getByAutor(autor: string): Observable<Livro[]> {
    return this.http.get<Livro[]>(`${this.endpoint}?autor=${autor}`).pipe(
      timeout(appSettings.requestTimeoutMs),
      catchError((error) => this.handleError('Falha ao buscar livro por autor', error))
    );
  }

 
  getByCategoria(categoria: string): Observable<Livro[]> {
    return this.http.get<Livro[]>(`${this.endpoint}?categoria=${categoria}`).pipe(
      timeout(appSettings.requestTimeoutMs),
      catchError((error) => this.handleError('Falha ao buscar livro por categoria', error))
    );
  }

 
  getByTitulo(titulo: string): Observable<Livro[]> {
    return this.http.get<Livro[]>(`${this.endpoint}?titulo=${titulo}`).pipe(
      timeout(appSettings.requestTimeoutMs),
      catchError((error) => this.handleError('Falha ao buscar livro por título', error))
    );
  }

  create(payload: LivroPayload): Observable<Livro> {
    return this.http.post<Livro>(`${this.endpoint}/`, payload).pipe(
      timeout(appSettings.requestTimeoutMs),
      catchError((error) => this.handleError('Falha ao cadastrar livro', error))
    );
  }

  update(codigo: string, payload: LivroPayload): Observable<Livro> {
    return this.http.put<Livro>(`${this.endpoint}/${codigo}`, payload).pipe(
      timeout(appSettings.requestTimeoutMs),
      catchError((error) => this.handleError('Falha ao atualizar livro', error))
    );
  }

  remove(codigo: string): Observable<void> {
    return this.http.delete<void>(`${this.endpoint}/${codigo}`).pipe(
      timeout(appSettings.requestTimeoutMs),
      catchError((error) => this.handleError('Falha ao remover livro', error))
    );
  }

  private handleError(baseMessage: string, error: unknown): Observable<never> {
    if (error instanceof TimeoutError) {
      return throwError(() => new Error(`${baseMessage}: tempo de requisicao excedido.`));
    }
    const message = error instanceof Error ? error.message : 'erro desconhecido';
    return throwError(() => new Error(`${baseMessage}: ${message}`));
  }
}