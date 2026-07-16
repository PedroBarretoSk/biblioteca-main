import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, catchError, throwError, TimeoutError, timeout } from 'rxjs';
import { appSettings } from '../config/app-settings';
import { Dashboard, RelatorioCategorias } from '../models/relatorio.model';
import { Livro } from '../models/livro.model';
import { Aluno } from '../models/aluno.model';

@Injectable({ providedIn: 'root' })
export class RelatoriosService {
  private readonly endpoint = `${appSettings.apiBaseUrl}/relatorios`;

  constructor(private readonly http: HttpClient) {}

  dashboard(): Observable<Dashboard> {
    return this.http.get<Dashboard>(`${this.endpoint}/dashboard`).pipe(
      timeout(appSettings.requestTimeoutMs),
      catchError((error) => this.handleError('Falha ao carregar dashboard', error))
    );
  }

  livros(): Observable<Livro[]> {
    return this.http.get<Livro[]>(`${this.endpoint}/livros`).pipe(
      timeout(appSettings.requestTimeoutMs),
      catchError((error) => this.handleError('Falha ao carregar relatório de livros', error))
    );
  }

  alunos(): Observable<Aluno[]> {
    return this.http.get<Aluno[]>(`${this.endpoint}/alunos`).pipe(
      timeout(appSettings.requestTimeoutMs),
      catchError((error) => this.handleError('Falha ao carregar relatório de alunos', error))
    );
  }

  categorias(): Observable<RelatorioCategorias[]> {
    return this.http.get<RelatorioCategorias[]>(`${this.endpoint}/categorias`).pipe(
      timeout(appSettings.requestTimeoutMs),
      catchError((error) => this.handleError('Falha ao carregar relatório de categorias', error))
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
