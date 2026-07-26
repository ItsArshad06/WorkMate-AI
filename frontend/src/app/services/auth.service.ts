import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  private apiUrl = 'http://127.0.0.1:8000/auth/login';

  constructor(
    private http: HttpClient
  ) {}

  login(data: any): Observable<any> {

    const body = new URLSearchParams();

    body.set('username', data.username);
    body.set('password', data.password);
    body.set('grant_type', 'password');

    return this.http.post(
      this.apiUrl,
      body.toString(),
      {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        }
      }
    );

  }

  saveUser(user: any): void {

    localStorage.setItem(
      'user',
      JSON.stringify(user)
    );

  }

  getUser(): any {

    const user = localStorage.getItem('user');

    if (!user) {

      return {
        username: 'admin',
        role: 'Admin'
      };

    }

    try {

      return JSON.parse(user);

    } catch {

      return {
        username: 'admin',
        role: 'Admin'
      };

    }

  }

  getToken(): string | null {

    return localStorage.getItem('access_token');

  }

  logout(): void {

    localStorage.removeItem('access_token');
    localStorage.removeItem('user');

  }

}