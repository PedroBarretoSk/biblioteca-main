import { CommonModule } from '@angular/common';
import { Component, OnInit, inject, signal } from '@angular/core';
import { FormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';
import { finalize } from 'rxjs';
import { Emprestimo } from '../../../core/models/emprestimo.model';
import { EmprestimosService } from '../../../core/services/emprestimos.service';

@Component({
  selector: 'app-emprestimos-page',
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './emprestimos-page.component.html',
  styleUrl: './emprestimos-page.component.scss'
})
export class EmprestimosPageComponent implements OnInit {
  private readonly fb = inject(FormBuilder);
  private readonly emprestimosService = inject(EmprestimosService);

  protected readonly emprestimos = signal<Emprestimo[]>([]);
  protected readonly loading = signal(false);
  protected readonly error = signal<string | null>(null);
  protected readonly tab = signal<'todos' | 'ativos'>('ativos');

  protected readonly empForm = this.fb.group({
    aluno_matricula: ['', Validators.required],
    livro_codigo: ['', Validators.required]
  });

  protected readonly devForm = this.fb.group({
    livro_codigo: ['', Validators.required]
  });

  ngOnInit(): void {
    this.load();
  }

  protected load(): void {
    this.loading.set(true);
    this.error.set(null);
    const req$ = this.tab() === 'ativos'
      ? this.emprestimosService.listAtivos()
      : this.emprestimosService.list();

    req$.pipe(finalize(() => this.loading.set(false))).subscribe({
      next: (items) => this.emprestimos.set(items),
      error: (err: Error) => this.error.set(err.message)
    });
  }

  protected setTab(tab: 'todos' | 'ativos'): void {
    this.tab.set(tab);
    this.load();
  }

  protected realizarEmprestimo(): void {
    if (this.empForm.invalid) { this.empForm.markAllAsTouched(); return; }
    this.loading.set(true);
    this.error.set(null);
    this.emprestimosService.realizar(this.empForm.getRawValue() as any)
      .pipe(finalize(() => this.loading.set(false)))
      .subscribe({
        next: () => { this.empForm.reset(); this.load(); },
        error: (err: Error) => this.error.set(err.message)
      });
  }

  protected devolver(): void {
    if (this.devForm.invalid) { this.devForm.markAllAsTouched(); return; }
    this.loading.set(true);
    this.error.set(null);
    this.emprestimosService.devolver(this.devForm.getRawValue() as any)
      .pipe(finalize(() => this.loading.set(false)))
      .subscribe({
        next: () => { this.devForm.reset(); this.load(); },
        error: (err: Error) => this.error.set(err.message)
      });
  }
}
