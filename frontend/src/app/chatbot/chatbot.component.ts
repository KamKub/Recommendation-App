import { NgForOf, NgIf, NgClass, NgStyle } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RouterLink, RouterLinkActive } from '@angular/router';
import { ChatbotService } from '../shared/chatbot.service';

@Component({
	selector: 'app-chatbot',
	standalone: true,
	imports: [
			NgIf,
			NgForOf,
			NgClass,
			RouterLink,
			RouterLinkActive,
			FormsModule,
	],
	templateUrl: './chatbot.component.html',
	styleUrl: './chatbot.component.css'
})
export class ChatbotComponent { 
	inputText: string = '';
	isProcessing: boolean = false;
  messagesList: string[] = ['Hello! How can i help ?'];

	constructor(private chatbotService: ChatbotService) {
  }

  sendQuery() {
		if (this.isProcessing) 
			return;
    if (this.inputText) {
			this.isProcessing = true;
			this.messagesList.push(this.inputText);
			this.chatbotService.getChatbotResponse(this.inputText).subscribe(
				responseObj => {
					this.messagesList.push(this.formatText(responseObj.response));
					this.isProcessing = false;
				})
			this.inputText = '';
    }
  }

	formatText(inputText: string): string {
		return inputText.replace(/\n/g, '<br>');
	}
}