import { CommonModule } from '@angular/common';
import { Component, OnInit, inject, signal } from '@angular/core';
import { FormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';
import { finalize } from 'rxjs';
import { Aluno, AlunoPayload } from '../../../core/models/aluno.model';
import { AlunosService } from '../../../core/services/alunos.service';

@Component({
  selector: 'app-alunos-page',
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './alunos-page.component.html',
  styleUrl: './alunos-page.component.scss'
})
export class AlunosPageComponent implements OnInit {
  private readonly fb = inject(FormBuilder);
  private readonly alunosService = inject(AlunosService);

  protected readonly alunos = signal<Aluno[]>([]);
  protected readonly loading = signal(false);
  protected readonly error = signal<string | null>(null);
  protected readonly editingMatricula = signal<string | null>(null);

  protected readonly form = this.fb.group({
    matricula: ['', Validators.required],
    nome: ['', [Validators.required, Validators.minLength(3)]],
    turma: ['', Validators.required],
    cpf: ['', Validators.required],
    nome_mae: ['', Validators.required],
    telefone: ['', Validators.required]
  });

  ngOnInit(): void {
    this.load();
  }

  protected load(): void {
    this.loading.set(true);
    this.error.set(null);
    this.alunosService.list().pipe(finalize(() => this.loading.set(false))).subscribe({
      next: (items) => this.alunos.set(items),
      error: (err: Error) => this.error.set(err.message)
    });
  }

  protected submit(): void {
    if (this.form.invalid) { this.form.markAllAsTouched(); return; }

    const v = this.form.getRawValue();
    const matricula = this.editingMatricula();
    this.loading.set(true);
    this.error.set(null);

    const req$ = matricula
      ? this.alunosService.update(matricula, v as AlunoPayload)
      : this.alunosService.create(v as AlunoPayload);

    req$.pipe(finalize(() => this.loading.set(false))).subscribe({
      next: () => { this.cancelEdit(); this.load(); },
      error: (err: Error) => this.error.set(err.message)
    });
  }

  protected startEdit(aluno: Aluno): void {
    this.editingMatricula.set(aluno.matricula);
    this.form.patchValue(aluno);
    this.form.get('matricula')?.disable();
  }

  protected cancelEdit(): void {
    this.editingMatricula.set(null);
    this.form.reset();
    this.form.get('matricula')?.enable();
  }

  protected remove(matricula: string): void {
    if (!confirm('Remover aluno?')) return;
    this.loading.set(true);
    this.alunosService.remove(matricula).pipe(finalize(() => this.loading.set(false))).subscribe({
      next: () => this.load(),
      error: (err: Error) => this.error.set(err.message)
    });
  }
}
