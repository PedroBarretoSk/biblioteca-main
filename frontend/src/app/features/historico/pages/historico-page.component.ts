import { CommonModule } from '@angular/common';
import { Component, OnInit, inject, signal } from '@angular/core';
import { finalize } from 'rxjs';
import { Historico } from '../../../core/models/historico.model';
import { HistoricoService } from '../../../core/services/historico.service';

@Component({
  selector: 'app-historico-page',
  imports: [CommonModule],
  templateUrl: './historico-page.component.html',
  styleUrl: './historico-page.component.scss'
})
export class HistoricoPageComponent implements OnInit {
  private readonly historicoService = inject(HistoricoService);

  protected readonly historico = signal<Historico[]>([]);
  protected readonly loading = signal(false);
  protected readonly error = signal<string | null>(null);

  ngOnInit(): void {
    this.load();
  }

  protected load(): void {
    this.loading.set(true);
    this.error.set(null);
    this.historicoService.list().pipe(finalize(() => this.loading.set(false))).subscribe({
      next: (items) => this.historico.set([...items].reverse()),
      error: (err: Error) => this.error.set(err.message)
    });
  }
}
