import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';

import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [
    CommonModule,
    FormsModule
  ],
  templateUrl: './login.html',
  styleUrl: './login.css'
})
export class Login {

  username = '';
  password = '';

  loading = false;

  constructor(
    private authService: AuthService,
    private router: Router
  ) {}

  login(): void {

    if (!this.username || !this.password) {

      alert("Please enter username and password.");

      return;

    }

    this.loading = true;

    this.authService.login({

      username: this.username,
      password: this.password

    }).subscribe({

      next: (response) => {

        console.log("Login Success:", response);

        localStorage.setItem(
          "access_token",
          response.access_token
        );

        localStorage.setItem(
          "user",
          JSON.stringify(response.user)
        );

        this.loading = false;

        this.router.navigate(['/dashboard']);

      },

      error: (error) => {

        this.loading = false;

        console.error(error);

        alert("Invalid username or password.");

      }

    });

  }

}