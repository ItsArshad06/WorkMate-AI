import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';

import { AuthService } from '../../services/auth.service';


@Component({
 selector:'app-login',
 standalone:true,
 imports:[
  FormsModule
 ],
 templateUrl:'./login.html',
 styleUrl:'./login.css'
})


export class Login{


 username="";
 password="";

 loading=false;


 constructor(
  private authService:AuthService,
  private router:Router
 ){}



 login(){


  this.loading=true;


  this.authService.login({

    username:this.username,
    password:this.password

  })
  .subscribe({

    next:(response)=>{


      console.log(
       "LOGIN RESPONSE",
       response
      );


      localStorage.setItem(
       "access_token",
       response.access_token
      );


      this.authService.saveUser({

        username:this.username,
        role:"Admin"

      });


      this.loading=false;


      this.router.navigate([
       "/dashboard"
      ]);


    },


    error:(err)=>{


      console.error(
       err
      );


      this.loading=false;


      alert(
       "Invalid username or password"
      );


    }


  });


 }


}