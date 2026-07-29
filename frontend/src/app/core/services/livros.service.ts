import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, TimeoutError, catchError, map, of, switchMap, throwError, timeout } from 'rxjs';
import { appSettings } from '../config/app-settings';
import { Livro, LivroPayload } from '../models/livro.model';

@Injectable({ providedIn: 'root' })
export class LivrosService {
  private readonly endpoint = `${appSettings.apiBaseUrl}/livros`;
  private mockData: Livro[] | null = null;

  constructor(private readonly http: HttpClient) {}

  list(): Observable<Livro[]> {
    if (appSettings.useMockData) {
      return this.ensureMockData();
    }

    return this.http.get<Livro[]>(this.endpoint).pipe(
      timeout(appSettings.requestTimeoutMs),
      catchError((error) => this.handleError('Falha ao listar livros', error))
    );
  }

  create(payload: LivroPayload): Observable<Livro> {
    if (appSettings.useMockData) {
      return this.ensureMockData().pipe(
        map((items) => {
          const nextId = items.length ? Math.max(...items.map((item) => item.id)) + 1 : 1;
          const novo: Livro = { id: nextId, ...payload };
          this.mockData = [...items, novo];
          return novo;
        })
      );
    }

    return this.http.post<Livro>(this.endpoint, payload).pipe(
      timeout(appSettings.requestTimeoutMs),
      catchError((error) => this.handleError('Falha ao cadastrar livro', error))
    );
  }

  update(id: number, payload: LivroPayload): Observable<Livro> {
    if (appSettings.useMockData) {
      return this.ensureMockData().pipe(
        switchMap((items) => {
          const index = items.findIndex((item) => item.id === id);
          if (index < 0) {
            return throwError(() => new Error('Livro nao encontrado para atualizacao.'));
          }

          const atualizado: Livro = { id, ...payload };
          const next = [...items];
          next[index] = atualizado;
          this.mockData = next;
          return of(atualizado);
        })
      );
    }

    return this.http.put<Livro>(`${this.endpoint}/${id}`, payload).pipe(
      timeout(appSettings.requestTimeoutMs),
      catchError((error) => this.handleError('Falha ao atualizar livro', error))
    );
  }

  remove(id: number): Observable<void> {
    if (appSettings.useMockData) {
      return this.ensureMockData().pipe(
        map((items) => {
          this.mockData = items.filter((item) => item.id !== id);
          return void 0;
        })
      );
    }

    return this.http.delete<void>(`${this.endpoint}/${id}`).pipe(
      timeout(appSettings.requestTimeoutMs),
      catchError((error) => this.handleError('Falha ao remover livro', error))
    );
  }

  private ensureMockData(): Observable<Livro[]> {
    if (this.mockData) {
      return of(this.mockData);
    }

    return this.http.get<Livro[]>('/mock/livros.json').pipe(
      map((items) => items ?? []),
      map((items) => {
        this.mockData = items;
        return items;
      }),
      catchError((error) => this.handleError('Falha ao carregar mock de livros', error))
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
