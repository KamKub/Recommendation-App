import {Component, OnInit} from '@angular/core';
import {RouterOutlet} from "@angular/router";
import {TVSeriesListComponent} from "./tvseries-list/tvseries-list.component";
import {DataStorageService} from "../shared/data-storage.service";
import {TVSeriesService} from "./tvseries.service";

@Component({
  selector: 'app-tvseries',
  standalone: true,
  imports: [
    RouterOutlet,
    TVSeriesListComponent
  ],
  templateUrl: './tvseries.component.html',
  styleUrl: './tvseries.component.css'
})
export class TVSeriesComponent implements OnInit{

  constructor(private dataStorageService:DataStorageService, private tvSeriesService:TVSeriesService) {
  }
  ngOnInit(): void {
    this.tvSeriesService.setPosters()
  }
}
