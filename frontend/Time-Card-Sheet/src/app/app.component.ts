import { Component, OnInit } from '@angular/core';
import { UserService } from './user.service';
import { ProviderAst } from '@angular/compiler';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
  
})
export class AppComponent implements OnInit {
  input;

   constructor(private userService:UserService){} 

  ngOnInit(){
    this.input={
      username: '',
      
      password: '',
      email: '',


    };
  }
    registerUser (){
      this.userService.registerUser(this.input).subscribe(
        response => {
          alert('User ' + this.input.username + ' has been created')

        },
        error => console.log('error', error)
      );

    }


    onLogin (){
      this.userService.loginUser(this.input).subscribe(
        response => {
          alert('User ' + this.input.username + ' logged.')

        },
        error => console.log('error', error)
      );

    }



  }

