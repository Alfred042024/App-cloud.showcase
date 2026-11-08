import { ComponentFixture, TestBed } from '@angular/core/testing';
import { ApiCalling } from './api-calling';

describe('ApiCalling', () => {
  let component: ApiCalling;
  let fixture: ComponentFixture<ApiCalling>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ApiCalling],
    }).compileComponents();

    fixture = TestBed.createComponent(ApiCalling);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
