import { NgIf, NgStyle } from '@angular/common';
import { Component } from '@angular/core';
import { RouterLink, RouterLinkActive } from '@angular/router';

@Component({
	selector: 'app-chatbot',
	standalone: true,
	imports: [
			NgIf,
			NgStyle,
			RouterLink,
			RouterLinkActive,
	],
	templateUrl: './chatbot.component.html',
	styleUrl: './chatbot.component.css'
})
export class ChatbotComponent { 

}
