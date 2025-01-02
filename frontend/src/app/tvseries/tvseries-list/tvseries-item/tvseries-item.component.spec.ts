import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TVSeriesItemComponent } from './tvseries-item.component';

describe('TVSeriesItemComponent', () => {
  let component: TVSeriesItemComponent;
  let fixture: ComponentFixture<TVSeriesItemComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [TVSeriesItemComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(TVSeriesItemComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
