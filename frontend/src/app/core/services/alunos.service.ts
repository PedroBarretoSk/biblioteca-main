import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, catchError, throwError, TimeoutError, timeout } from 'rxjs';
import { appSettings } from '../config/app-settings';
import { Aluno, AlunoPayload } from '../models/aluno.model';

@Injectable({ providedIn: 'root' })
export class AlunosService {
  private readonly endpoint = `${appSettings.apiBaseUrl}/alunos`;

  constructor(private readonly http: HttpClient) {}

  list(): Observable<Aluno[]> {
    return this.http.get<Aluno[]>(`${this.endpoint}/`).pipe(
      timeout(appSettings.requestTimeoutMs),
      catchError((error) => this.handleError('Falha ao listar alunos', error))
    );
  }

  get(matricula: string): Observable<Aluno> {
    return this.http.get<Aluno>(`${this.endpoint}/${matricula}`).pipe(
      timeout(appSettings.requestTimeoutMs),
      catchError((error) => this.handleError('Falha ao buscar aluno', error))
    );
  }

  create(payload: AlunoPayload): Observable<Aluno> {
    return this.http.post<Aluno>(`${this.endpoint}/`, payload).pipe(
      timeout(appSettings.requestTimeoutMs),
      catchError((error) => this.handleError('Falha ao cadastrar aluno', error))
    );
  }

  update(matricula: string, payload: AlunoPayload): Observable<Aluno> {
    return this.http.put<Aluno>(`${this.endpoint}/${matricula}`, payload).pipe(
      timeout(appSettings.requestTimeoutMs),
      catchError((error) => this.handleError('Falha ao atualizar aluno', error))
    );
  }

  remove(matricula: string): Observable<void> {
    return this.http.delete<void>(`${this.endpoint}/${matricula}`).pipe(
      timeout(appSettings.requestTimeoutMs),
      catchError((error) => this.handleError('Falha ao remover aluno', error))
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
