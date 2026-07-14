import { Routes } from '@angular/router';
import { LivrosPageComponent } from './features/livros/pages/livros-page.component';

export const routes: Routes = [
	{
		path: '',
		pathMatch: 'full',
		redirectTo: 'livros'
	},
	{
		path: 'livros',
		component: LivrosPageComponent
	},
	{
		path: '**',
		redirectTo: 'livros'
	}
];
