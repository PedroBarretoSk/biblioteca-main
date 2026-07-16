import { Component, OnInit, inject, signal } from '@angular/core';
import { RelatoriosService } from '../../../core/services/relatorios.service';
import { Dashboard } from '../../../core/models/relatorio.model';

@Component({
  selector: 'app-dashboard-page',
  templateUrl: './dashboard-page.component.html',
  styleUrl: './dashboard-page.component.scss'
})
export class DashboardPageComponent implements OnInit {
  private readonly relatoriosService = inject(RelatoriosService);

  protected readonly dados = signal<Dashboard | null>(null);
  protected readonly loading = signal(false);
  protected readonly error = signal<string | null>(null);

  ngOnInit(): void {
    this.loading.set(true);
    this.relatoriosService.dashboard().subscribe({
      next: (d) => { this.dados.set(d); this.loading.set(false); },
      error: (err: Error) => { this.error.set(err.message); this.loading.set(false); }
    });
  }
}
