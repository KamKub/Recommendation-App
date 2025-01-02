import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TVSeriesDetailComponent } from './tvseries-detail.component';

describe('TVSeriesDetailComponent', () => {
  let component: TVSeriesDetailComponent;
  let fixture: ComponentFixture<TVSeriesDetailComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [TVSeriesDetailComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(TVSeriesDetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
