import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, catchError, throwError, TimeoutError, timeout } from 'rxjs';
import { appSettings } from '../config/app-settings';
import { Historico } from '../models/historico.model';

@Injectable({ providedIn: 'root' })
export class HistoricoService {
  private readonly endpoint = `${appSettings.apiBaseUrl}/historico`;

  constructor(private readonly http: HttpClient) {}

  list(): Observable<Historico[]> {
    return this.http.get<Historico[]>(`${this.endpoint}/`).pipe(
      timeout(appSettings.requestTimeoutMs),
      catchError((error) => this.handleError('Falha ao listar histórico', error))
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
