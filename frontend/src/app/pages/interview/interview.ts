import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-interview',
  standalone: true,
  imports: [
    CommonModule,
    FormsModule
  ],
  templateUrl: './interview.html',
  styleUrl: './interview.css',
})
export class Interview {

  candidateName = '';

  position = '';

  interviewStarted = false;

  interviewCompleted = false;

  currentQuestionIndex = 0;

  answer = '';

  answers: {
    question: string;
    answer: string;
  }[] = [];

  questions = [
    'Tell me about yourself.',
    'Why do you want to join our company?',
    'Describe a difficult project you completed.',
    'What are your strengths and weaknesses?',
    'Where do you see yourself in five years?'
  ];

  startInterview() {

    if (!this.candidateName.trim() || !this.position.trim()) {

      alert('Please enter Candidate Name and Position.');

      return;

    }

    this.interviewStarted = true;

    this.interviewCompleted = false;

    this.currentQuestionIndex = 0;

    this.answer = '';

    this.answers = [];

  }

  nextQuestion() {

    if (!this.answer.trim()) {

      alert('Please answer the current question before continuing.');

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

      this.interviewCompleted = true;

      console.log('Interview Answers');

      console.table(this.answers);

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