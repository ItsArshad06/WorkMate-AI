import { Component, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClient, HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-resume',
  standalone: true,
  imports: [
    CommonModule,
    HttpClientModule
  ],
  templateUrl: './resume.html',
  styleUrl: './resume.css'
})
export class Resume {

  selectedFile: File | null = null;

  loading = false;

  analysis: any = null;


  constructor(
    private http: HttpClient,
    private cdr: ChangeDetectorRef
  ) {}



  onFileSelected(event: any) {

    this.selectedFile = event.target.files[0];

    this.analysis = null;

  }



  analyzeResume() {


    if (!this.selectedFile) {

      alert("Select a resume first");

      return;

    }


    this.loading = true;


    const formData = new FormData();


    formData.append(
      "file",
      this.selectedFile
    );


    const token =
      localStorage.getItem("access_token");



    this.http.post<any>(

      "http://127.0.0.1:8000/ai/resume",

      formData,

      {
        headers:{
          Authorization:
          `Bearer ${token}`
        }
      }

    )
    .subscribe({

      next:(res)=>{


        console.log(
          "Resume Result:",
          res
        );


        this.analysis = res;


        this.loading = false;


        this.cdr.detectChanges();


      },


      error:(err)=>{


        console.error(
          "Resume Error:",
          err
        );


        this.loading = false;


        this.cdr.detectChanges();


      }


    });


  }



  clearResume(){

    this.selectedFile = null;

    this.analysis = null;

  }

}