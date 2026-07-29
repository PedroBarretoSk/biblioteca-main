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
  protected readonly editingId = signal<number | null>(null);

  protected readonly livroForm = this.formBuilder.group({
    titulo: ['', [Validators.required, Validators.minLength(2)]],
    autor: ['', [Validators.required, Validators.minLength(2)]],
    anoPublicacao: [new Date().getFullYear(), [Validators.required, Validators.min(0)]],
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
    const id = this.editingId();

    this.loading.set(true);
    this.error.set(null);

    const request$ = id === null ? this.livrosService.create(payload) : this.livrosService.update(id, payload);

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
    this.editingId.set(livro.id);
    this.livroForm.patchValue({
      titulo: livro.titulo,
      autor: livro.autor,
      anoPublicacao: livro.anoPublicacao,
      disponivel: livro.disponivel
    });
  }

  protected cancelEdit(): void {
    this.editingId.set(null);
    this.livroForm.reset({
      titulo: '',
      autor: '',
      anoPublicacao: new Date().getFullYear(),
      disponivel: true
    });
  }

  protected remove(id: number): void {
    this.loading.set(true);
    this.error.set(null);

    this.livrosService
      .remove(id)
      .pipe(finalize(() => this.loading.set(false)))
      .subscribe({
        next: () => this.loadLivros(),
        error: (err: Error) => this.error.set(err.message)
      });
  }

  protected trackById(_: number, livro: Livro): number {
    return livro.id;
  }

  private buildPayload(): LivroPayload {
    const formValue = this.livroForm.getRawValue();

    return {
      titulo: (formValue.titulo ?? '').trim(),
      autor: (formValue.autor ?? '').trim(),
      anoPublicacao: Number(formValue.anoPublicacao ?? 0),
      disponivel: Boolean(formValue.disponivel)
    };
  }
}
