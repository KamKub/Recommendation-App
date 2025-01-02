import {Injectable} from "@angular/core";
import {Subject} from "rxjs";
import {TvSeriesPoster} from "./tvseries-poster.model";
import {DataStorageService} from "../shared/data-storage.service";
import {TVSeries} from "./tvseries.model";

@Injectable({providedIn: 'root'})
export class TVSeriesService{
  pageChanged = new Subject<TvSeriesPoster[]>();
  pageNumber:number = 0;
  private tvSeriesPosters: TvSeriesPoster[] = [];

  constructor(private dataStorageService: DataStorageService) {
  }

  setPosters() {
    this.dataStorageService.getPostersQuery(this.pageNumber).subscribe(tvSeriesPosters => {
      this.tvSeriesPosters = tvSeriesPosters
      this.pageChanged.next(this.tvSeriesPosters.slice())
    })
  }

  getTVSeriesDetail(id: number){
    return this.dataStorageService.getTVSeriesDetails(id)
  }

  checkExistId(id: number){
    return this.tvSeriesPosters.some(series => series.id === id)
  }
}
