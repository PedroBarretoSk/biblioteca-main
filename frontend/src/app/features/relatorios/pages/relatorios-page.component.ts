import { CommonModule } from '@angular/common';
import { Component, OnInit, inject, signal } from '@angular/core';
import { finalize } from 'rxjs';
import { RelatoriosService } from '../../../core/services/relatorios.service';
import { Dashboard, RelatorioCategorias } from '../../../core/models/relatorio.model';
import { Aluno } from '../../../core/models/aluno.model';

@Component({
  selector: 'app-relatorios-page',
  imports: [CommonModule],
  templateUrl: './relatorios-page.component.html',
  styleUrl: './relatorios-page.component.scss'
})
export class RelatoriosPageComponent implements OnInit {
  private readonly relatoriosService = inject(RelatoriosService);

  protected readonly dashboard = signal<Dashboard | null>(null);
  protected readonly rankingAlunos = signal<Aluno[]>([]);
  protected readonly categorias = signal<RelatorioCategorias[]>([]);
  protected readonly loading = signal(false);
  protected readonly error = signal<string | null>(null);

  ngOnInit(): void {
    this.load();
  }

  protected load(): void {
    this.loading.set(true);
    this.error.set(null);

    this.relatoriosService.dashboard().subscribe({ next: (d) => this.dashboard.set(d) });
    this.relatoriosService.alunos().subscribe({ next: (a) => this.rankingAlunos.set(a) });
    this.relatoriosService.categorias()
      .pipe(finalize(() => this.loading.set(false)))
      .subscribe({
        next: (c) => this.categorias.set(c),
        error: (err: Error) => this.error.set(err.message)
      });
  }
}
