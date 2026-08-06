import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { InterviewService } from '../../services/interview';

@Component({
  selector: 'app-interview',
  standalone: true,
  imports: [
    CommonModule,
    FormsModule
  ],
  templateUrl: './interview.html',
  styleUrl: './interview.css'
})
export class Interview {

  constructor(
    private interviewService: InterviewService
  ) {}

  candidateName = '';

  position = '';

  interviewStarted = false;

  interviewCompleted = false;

  loading = false;

  currentQuestionIndex = 0;

  answer = '';

  evaluation: any = null;

  answers: {
    question: string;
    answer: string;
  }[] = [];

  questions: string[] = [];

  startInterview() {

    if (!this.candidateName.trim() || !this.position.trim()) {

      alert('Please enter Candidate Name and Position.');

      return;

    }

    this.loading = true;

    this.interviewService.startInterview(

      this.candidateName,

      this.position

    ).subscribe({

      next: (response: any) => {

        this.questions = response.questions;

        this.interviewStarted = true;

        this.interviewCompleted = false;

        this.currentQuestionIndex = 0;

        this.answer = '';

        this.answers = [];

        this.loading = false;

      },

      error: () => {

        this.loading = false;

        alert('Unable to start interview.');

      }

    });

  }

  nextQuestion() {

    if (!this.answer.trim()) {

      alert('Please answer the current question.');

      return;

    }

    this.answers.push({

      question: this.currentQuestion,

      answer: this.answer

    });

    this.answer = '';

    if (this.currentQuestionIndex < this.questions.length - 1) {

      this.currentQuestionIndex++;

    }

    else {

      this.loading = true;

      this.interviewService.evaluateInterview(

        this.candidateName,

        this.position,

        this.answers

      ).subscribe({

        next: (response: any) => {

          this.loading = false;

          this.evaluation = response;

          this.interviewCompleted = true;

        },

        error: () => {

          this.loading = false;

          alert('Evaluation failed.');

        }

      });

    }

  }

  get currentQuestion(): string {

    return this.questions[this.currentQuestionIndex];

  }

  get progress(): number {

    return Math.round(

      ((this.currentQuestionIndex + 1) / this.questions.length) * 100

    );

  }

}