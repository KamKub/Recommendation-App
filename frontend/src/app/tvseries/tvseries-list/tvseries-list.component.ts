import {Component, OnDestroy, OnInit} from '@angular/core';
import {TVSeriesItemComponent} from "./tvseries-item/tvseries-item.component";
import {Subscription} from "rxjs";
import {TVSeriesService} from "../tvseries.service";
import {ActivatedRoute, Router} from "@angular/router";
import {NgForOf, NgStyle} from "@angular/common";
import {TvSeriesPoster} from "../tvseries-poster.model";

@Component({
  selector: 'app-tvseries-list',
  standalone: true,
  imports: [
    TVSeriesItemComponent,
    NgForOf,
    NgStyle
  ],
  templateUrl: './tvseries-list.component.html',
  styleUrl: './tvseries-list.component.css'
})
export class TVSeriesListComponent implements OnInit, OnDestroy{
  tvSeriesPosters: TvSeriesPoster[] = [];
  private subscription!: Subscription;

  constructor(private tvSeriesService: TVSeriesService, private router: Router, private route: ActivatedRoute) {
  }

  ngOnInit(): void {
    this.subscription = this.tvSeriesService.pageChanged
      .subscribe((
        tvSeriesPosters: TvSeriesPoster[]) => {
          this.tvSeriesPosters = tvSeriesPosters
        }
      )
  }

  ngOnDestroy(): void {
    this.subscription.unsubscribe()
  }

  onNextPage() {
    this.tvSeriesService.pageNumber++
    this.tvSeriesService.setPosters()
  }

  onPreviousPage() {
    this.tvSeriesService.pageNumber--
    this.tvSeriesService.setPosters()
  }

  getPageNumber(){
    return this.tvSeriesService.pageNumber
  }
}
