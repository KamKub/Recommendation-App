import { Routes } from '@angular/router';
import {MoviesComponent} from "./movies/movies.component";
import {MovieDetailComponent} from "./movies/movie-detail/movie-detail.component";
import { ChatbotComponent } from './chatbot/chatbot.component';

export const routes: Routes = [
  { path: ' ', redirectTo: '/', pathMatch: 'full'},
  { path: 'chatbot', component: ChatbotComponent},
  { path: 'movies', component: MoviesComponent, children: [
      { path: ':id', component: MovieDetailComponent},
    ]},
];
