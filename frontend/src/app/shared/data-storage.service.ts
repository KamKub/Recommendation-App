import {Injectable} from "@angular/core";
import {HttpClient} from "@angular/common/http";
import {map, tap} from "rxjs";
import {MoviePoster} from "../movies/movie-poster.model";
import {Movie} from "../movies/movie.model";

interface PosterDetails {
  poster_path: string;
  title: string;
}

@Injectable({providedIn: 'root'})
export class DataStorageService{
  constructor(private http: HttpClient) {}
  getPostersQuery(pageNumber: number) {
    return this.http.get<{ [key: string]: PosterDetails }>('api/tv_series', {
      params: {
        page: pageNumber
      }
    })
      .pipe(
        map(posters => {
          return Object.keys(posters).map(key => {
            const id = parseInt(key.replace('id', ''), 10);
            const details = posters[key];
            return new MoviePoster(id, details.title, details.poster_path);
          });
        }),
        tap(posters => {
          return posters
        })
      )
  }

  getMovieDetails(movieId: number) {
    return this.http.get<Movie>('api/tv_series_details', {
      params: {
        id: movieId
      }
    })
      .pipe(
      map(movie => {
        return movie
      })
    )
  }
}
