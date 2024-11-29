import {Component, OnDestroy, OnInit} from '@angular/core';
import {ActivatedRoute, Params, Router, RouterLink} from "@angular/router";
import {Movie} from "../movie.model";
import {MoviesService} from "../movies.service";
import {NgClass, NgForOf, NgIf} from "@angular/common";

@Component({
  selector: 'app-movie-detail',
  standalone: true,
  imports: [
    RouterLink,
    NgIf,
    NgForOf,
    NgClass
  ],
  templateUrl: './movie-detail.component.html',
  styleUrl: './movie-detail.component.css'
})
export class MovieDetailComponent implements OnInit, OnDestroy{
  movie: Movie | undefined
  id!: number

  constructor(private movieService: MoviesService, private route: ActivatedRoute , private router: Router) {
  }
  ngOnInit(): void {
    document.addEventListener('keydown', (event: KeyboardEvent) => {
      if (event.key === 'Escape') {
        this.router.navigate(['/movies'])
      }
    })
    this.route.params
      .subscribe((params: Params) => {
        this.id = +params['id']
        if(this.movieService.checkExistId(this.id)){
          this.movieService.getMovieDetail(this.id).subscribe(
            movie => {
              this.movie = movie;
            })
        }
        else{
          this.router.navigate(['/movies'])
        }
      })
  }

  ngOnDestroy(): void {
    document.removeEventListener('keydown', (event: KeyboardEvent) => {
      if (event.key === 'Escape') {
        this.router.navigate(['/movies'])
      }
    });
  }
}
