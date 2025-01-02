import { Routes } from '@angular/router';
import {TVSeriesComponent} from "./tvseries/tvseries.component";
import {TVSeriesDetailComponent} from "./tvseries/tvseries-detail/tvseries-detail.component";
import { ChatbotComponent } from './chatbot/chatbot.component';

export const routes: Routes = [
  { path: ' ', redirectTo: '/', pathMatch: 'full'},
  { path: 'chatbot', component: ChatbotComponent},
  { path: 'tvseries', component: TVSeriesComponent, children: [
      { path: ':id', component: TVSeriesDetailComponent},
    ]},
];
