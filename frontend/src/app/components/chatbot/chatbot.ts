import { Component, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import {
  HttpClient,
  HttpClientModule,
  HttpHeaders
} from '@angular/common/http';

import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-chatbot',
  standalone: true,
  imports: [
    CommonModule,
    FormsModule,
    HttpClientModule
  ],
  templateUrl: './chatbot.html',
  styleUrl: './chatbot.css'
})
export class Chatbot {

  message = '';

  messages: any[] = [
    {
      sender: 'ai',
      text: '👋 Hello! I am WorkMate AI. Ask me anything about employees, attendance, leaves or dashboard insights.'
    }
  ];

  constructor(
    private http: HttpClient,
    private authService: AuthService,
    private cdr: ChangeDetectorRef
  ) {}

  sendMessage(): void {

    if (!this.message.trim()) {
      return;
    }

    const userMessage = this.message.trim();

    // Show user message
    this.messages.push({
      sender: 'user',
      text: userMessage
    });

    // Clear input
    this.message = '';

    // Show thinking message
    this.messages.push({
      sender: 'ai',
      text: '⏳ WorkMate AI is thinking...'
    });

    const loadingIndex = this.messages.length - 1;

    this.cdr.detectChanges();

    const token = this.authService.getToken();

    const headers = new HttpHeaders({
      Authorization: `Bearer ${token}`
    });

    this.http.post<any>(
      'http://127.0.0.1:8000/ai/chat',
      {
        message: userMessage
      },
      {
        headers
      }
    ).subscribe({

      next: (res) => {

        this.messages[loadingIndex] = {
          sender: 'ai',
          text: res.reply
        };

        this.cdr.detectChanges();

        setTimeout(() => {
          const body = document.querySelector('.chat-body');

          if (body) {
            body.scrollTop = body.scrollHeight;
          }
        }, 50);

      },

      error: (err) => {

        this.messages[loadingIndex] = {
          sender: 'ai',
          text: '❌ ' + (err.error?.detail || 'Unable to contact WorkMate AI.')
        };

        this.cdr.detectChanges();

      }

    });

  }

}