import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, catchError, throwError, TimeoutError, timeout } from 'rxjs';
import { appSettings } from '../config/app-settings';
import { Emprestimo, EmprestimoPayload, DevolucaoPayload } from '../models/emprestimo.model';

@Injectable({ providedIn: 'root' })
export class EmprestimosService {
  private readonly endpointEmp = `${appSettings.apiBaseUrl}/emprestimos`;
  private readonly endpointDev = `${appSettings.apiBaseUrl}/devolucoes`;

  constructor(private readonly http: HttpClient) {}

  list(): Observable<Emprestimo[]> {
    return this.http.get<Emprestimo[]>(`${this.endpointEmp}/`).pipe(
      timeout(appSettings.requestTimeoutMs),
      catchError((error) => this.handleError('Falha ao listar empréstimos', error))
    );
  }

  listAtivos(): Observable<Emprestimo[]> {
    return this.http.get<Emprestimo[]>(`${this.endpointEmp}/ativos`).pipe(
      timeout(appSettings.requestTimeoutMs),
      catchError((error) => this.handleError('Falha ao listar empréstimos ativos', error))
    );
  }

  realizar(payload: EmprestimoPayload): Observable<Emprestimo> {
    return this.http.post<Emprestimo>(`${this.endpointEmp}/`, payload).pipe(
      timeout(appSettings.requestTimeoutMs),
      catchError((error) => this.handleError('Falha ao realizar empréstimo', error))
    );
  }

  devolver(payload: DevolucaoPayload): Observable<Emprestimo> {
    return this.http.post<Emprestimo>(`${this.endpointDev}/`, payload).pipe(
      timeout(appSettings.requestTimeoutMs),
      catchError((error) => this.handleError('Falha ao devolver livro', error))
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
