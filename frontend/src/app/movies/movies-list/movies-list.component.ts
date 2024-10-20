import {Component, OnDestroy, OnInit} from '@angular/core';
import {MovieItemComponent} from "./movie-item/movie-item.component";
import {Subscription} from "rxjs";
import {MoviesService} from "../movies.service";
import {ActivatedRoute, Router} from "@angular/router";
import {NgForOf, NgStyle} from "@angular/common";
import {MoviePoster} from "../movie-poster.model";
import {DataStorageService} from "../../shared/data-storage.service";

@Component({
  selector: 'app-movies-list',
  standalone: true,
  imports: [
    MovieItemComponent,
    NgForOf,
    NgStyle
  ],
  templateUrl: './movies-list.component.html',
  styleUrl: './movies-list.component.css'
})
export class MoviesListComponent implements OnInit, OnDestroy{
  moviePosters: MoviePoster[] = [];
  private subscription!: Subscription;

  constructor(private movieService: MoviesService, private router: Router, private route: ActivatedRoute) {
  }

  ngOnInit(): void {
    this.subscription = this.movieService.pageChanged
      .subscribe((
        moviePosters: MoviePoster[]) => {
          this.moviePosters = moviePosters
        }
      )
  }

  ngOnDestroy(): void {
    this.subscription.unsubscribe()
  }

  onNextPage() {
    this.movieService.pageNumber++
    this.movieService.setPosters()
  }

  onPreviousPage() {
    this.movieService.pageNumber--
    this.movieService.setPosters()
  }

  getPageNumber(){
    return this.movieService.pageNumber
  }
}
