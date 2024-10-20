import {Injectable} from "@angular/core";
import {Subject} from "rxjs";
import {MoviePoster} from "./movie-poster.model";
import {DataStorageService} from "../shared/data-storage.service";
import {Movie} from "./movie.model";

@Injectable({providedIn: 'root'})
export class MoviesService{
  pageChanged = new Subject<MoviePoster[]>();
  pageNumber:number = 0;
  private moviePosters: MoviePoster[] = [];

  constructor(private dataStorageService: DataStorageService) {
  }

  setPosters() {
    this.dataStorageService.getPostersQuery(this.pageNumber).subscribe(moviePosters => {
      this.moviePosters = moviePosters
      this.pageChanged.next(this.moviePosters.slice())
    })
  }

  getMovieDetail(id: number){
    return this.dataStorageService.getMovieDetails(id)
  }

  checkExistId(id: number){
    return this.moviePosters.some(movie => movie.id === id)
  }
}
