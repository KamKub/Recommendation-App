import {Component, OnDestroy, OnInit} from '@angular/core';
import {ActivatedRoute, Params, Router, RouterLink} from "@angular/router";
import {TVSeries} from "../tvseries.model";
import {TVSeriesService} from "../tvseries.service";
import {NgClass, NgForOf, NgIf} from "@angular/common";

@Component({
  selector: 'app-tvseries-detail',
  standalone: true,
  imports: [
    RouterLink,
    NgIf,
    NgForOf,
    NgClass
  ],
  templateUrl: './tvseries-detail.component.html',
  styleUrl: './tvseries-detail.component.css'
})
export class TVSeriesDetailComponent implements OnInit, OnDestroy{
  tvSeries: TVSeries | undefined
  id!: number

  constructor(private tvSeriesService: TVSeriesService, private route: ActivatedRoute , private router: Router) {
  }
  ngOnInit(): void {
    document.addEventListener('keydown', (event: KeyboardEvent) => {
      if (event.key === 'Escape') {
        this.router.navigate(['/tvseries'])
      }
    })
    this.route.params
      .subscribe((params: Params) => {
        this.id = +params['id']
        if(this.tvSeriesService.checkExistId(this.id)){
          this.tvSeriesService.getTVSeriesDetail(this.id).subscribe(
            series => {
              this.tvSeries = series;
            })
        }
        else{
          this.router.navigate(['/tvseries'])
        }
      })
  }

  ngOnDestroy(): void {
    document.removeEventListener('keydown', (event: KeyboardEvent) => {
      if (event.key === 'Escape') {
        this.router.navigate(['/tvseries'])
      }
    });
  }
}
