import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TVSeriesComponent } from './tvseries.component';

describe('TVSeriesComponent', () => {
  let component: TVSeriesComponent;
  let fixture: ComponentFixture<TVSeriesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [TVSeriesComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(TVSeriesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
