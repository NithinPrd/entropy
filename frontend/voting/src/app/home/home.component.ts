import { Component } from '@angular/core';
import { HeaderComponent } from "../header/header.component";
import { MatCard, MatCardHeader, MatCardSubtitle, MatCardTitle } from "@angular/material/card"

@Component({
    selector: 'app-home',
    standalone: true,
    templateUrl: './home.component.html',
    styleUrl: './home.component.scss',
    imports: [HeaderComponent, MatCard, MatCardTitle, MatCardHeader, MatCardSubtitle]
})
export class HomeComponent {
  year: string = ""
  state: string = ""

  constructor() {
    this.year = "2024"
    this.state = "Tamil Nadu"
  }
}
