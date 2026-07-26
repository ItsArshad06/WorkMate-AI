import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface LoginRequest {

  username: string;
  password: string;

}

export interface LoginResponse {

  access_token: string;
  token_type: string;

  user: {

    username: string;
    full_name: string;
    role: string;

  };

}


@Injectable({
  providedIn: 'root'
})
export class AuthService {


  private apiUrl = 'http://127.0.0.1:8000/auth/login';


  constructor(
    private http: HttpClient
  ) {}


  login(
    data: LoginRequest
  ): Observable<LoginResponse> {

    return this.http.post<LoginResponse>(
      this.apiUrl,
      data
    );

  }


  logout(): void {

    localStorage.removeItem(
      "access_token"
    );

    localStorage.removeItem(
      "user"
    );

  }


  getUser(){

    const user = localStorage.getItem(
      "user"
    );

    return user
      ? JSON.parse(user)
      : null;

  }


  isLoggedIn(){

    return !!localStorage.getItem(
      "access_token"
    );

  }

}