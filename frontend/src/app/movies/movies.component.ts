import {Component, OnInit} from '@angular/core';
import {RouterOutlet} from "@angular/router";
import {MoviesListComponent} from "./movies-list/movies-list.component";
import {DataStorageService} from "../shared/data-storage.service";
import {MoviesService} from "./movies.service";

@Component({
  selector: 'app-movies',
  standalone: true,
  imports: [
    RouterOutlet,
    MoviesListComponent
  ],
  templateUrl: './movies.component.html',
  styleUrl: './movies.component.css'
})
export class MoviesComponent implements OnInit{

  constructor(private dataStorageService:DataStorageService, private moviesService:MoviesService) {
  }
  ngOnInit(): void {
    this.moviesService.setPosters()
  }
}
