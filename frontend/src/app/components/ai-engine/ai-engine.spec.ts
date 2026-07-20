import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AiEngine } from './ai-engine';

describe('AiEngine', () => {
  let component: AiEngine;
  let fixture: ComponentFixture<AiEngine>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AiEngine],
    }).compileComponents();

    fixture = TestBed.createComponent(AiEngine);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
