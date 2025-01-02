import {Component, Input} from '@angular/core';
import {RouterLink, RouterLinkActive} from "@angular/router";
import {TvSeriesPoster} from "../../tvseries-poster.model";

@Component({
  selector: 'app-tvseries-item',
  standalone: true,
  imports: [
    RouterLink,
    RouterLinkActive
  ],
  templateUrl: './tvseries-item.component.html',
  styleUrl: './tvseries-item.component.css'
})
export class TVSeriesItemComponent {
  @Input() tvSeriesPoster!: TvSeriesPoster;
}
