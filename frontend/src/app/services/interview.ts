import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class InterviewService {

  private http = inject(HttpClient);

  private apiUrl = 'http://127.0.0.1:8000/ai';

  startInterview(
    candidateName: string,
    position: string
  ): Observable<any> {

    return this.http.post(

      `${this.apiUrl}/interview/start`,

      {

        candidate_name: candidateName,

        position

      }

    );

  }

  evaluateInterview(
    candidateName: string,
    position: string,
    answers: any[]
  ): Observable<any> {

    return this.http.post(

      `${this.apiUrl}/interview/evaluate`,

      {

        candidate_name: candidateName,

        position,

        answers

      }

    );

  }

}