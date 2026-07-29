import { CommonModule } from '@angular/common';
import { Component, OnInit, inject, signal } from '@angular/core';
import { FormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';
import { finalize } from 'rxjs';
import { Livro, LivroPayload } from '../../../core/models/livro.model';
import { LivrosService } from '../../../core/services/livros.service';

@Component({
  selector: 'app-livros-page',
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './livros-page.component.html',
  styleUrl: './livros-page.component.scss'
})
export class LivrosPageComponent implements OnInit {
  private readonly formBuilder = inject(FormBuilder);

  protected readonly livros = signal<Livro[]>([]);
  protected readonly loading = signal(false);
  protected readonly error = signal<string | null>(null);
  protected readonly editingCodigo = signal<string | null>(null);

  protected readonly livroForm = this.formBuilder.group({
    codigo: ['', Validators.required],
    titulo: ['', [Validators.required, Validators.minLength(2)]],
    autor: ['', [Validators.required, Validators.minLength(2)]],
    categoria: ['', Validators.required],
    disponivel: [true]
  });

  constructor(private readonly livrosService: LivrosService) {}

  ngOnInit(): void {
    this.loadLivros();
  }

  protected loadLivros(): void {
    this.loading.set(true);
    this.error.set(null);

    this.livrosService
      .list()
      .pipe(finalize(() => this.loading.set(false)))
      .subscribe({
        next: (items) => this.livros.set(items),
        error: (err: Error) => this.error.set(err.message)
      });
  }

  protected submit(): void {
    if (this.livroForm.invalid) {
      this.livroForm.markAllAsTouched();
      return;
    }

    const payload = this.buildPayload();
    const codigo = this.editingCodigo();

    this.loading.set(true);
    this.error.set(null);

    const request$ = codigo === null
      ? this.livrosService.create(payload)
      : this.livrosService.update(codigo, payload);

    request$
      .pipe(finalize(() => this.loading.set(false)))
      .subscribe({
        next: () => {
          this.cancelEdit();
          this.loadLivros();
        },
        error: (err: Error) => this.error.set(err.message)
      });
  }

  protected startEdit(livro: Livro): void {
    this.editingCodigo.set(livro.codigo);
    this.livroForm.patchValue({
      codigo: livro.codigo,
      titulo: livro.titulo,
      autor: livro.autor,
      categoria: livro.categoria,
      disponivel: livro.disponivel
    });
    this.livroForm.get('codigo')?.disable();
  }

  protected cancelEdit(): void {
    this.editingCodigo.set(null);
    this.livroForm.reset({ titulo: '', autor: '', categoria: '', codigo: '', disponivel: true });
    this.livroForm.get('codigo')?.enable();
  }

  protected remove(codigo: string): void {
    if (!confirm('Remover livro?')) return;
    this.loading.set(true);
    this.error.set(null);

    this.livrosService
      .remove(codigo)
      .pipe(finalize(() => this.loading.set(false)))
      .subscribe({
        next: () => this.loadLivros(),
        error: (err: Error) => this.error.set(err.message)
      });
  }

  private buildPayload(): LivroPayload {
    const v = this.livroForm.getRawValue();
    return {
      codigo: (v.codigo ?? '').trim(),
      titulo: (v.titulo ?? '').trim(),
      autor: (v.autor ?? '').trim(),
      categoria: (v.categoria ?? '').trim(),
      disponivel: Boolean(v.disponivel)
    };
  }
}
