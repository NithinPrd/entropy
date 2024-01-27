import { Component } from '@angular/core';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatIconModule, MatIconRegistry } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';

@Component({
  selector: 'app-header',
  standalone: true,
  imports: [MatToolbarModule, MatIconModule, MatButtonModule],
  templateUrl: './header.component.html',
  styleUrl: './header.component.scss'
})
export class HeaderComponent {
  user = 'John'

  constructor(private matIconRegistry: MatIconRegistry) {
    this.matIconRegistry.addSvgIcon(
      'voting-logo-main',
      '../../assets/voting-logo-main.svg'
    )
  }

}
