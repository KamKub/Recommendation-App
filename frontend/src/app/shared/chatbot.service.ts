import {Injectable} from "@angular/core";
import {HttpClient} from "@angular/common/http";

@Injectable({providedIn: 'root'})
export class ChatbotService{
  constructor(private http: HttpClient) {}

  getChatbotResponse(userQuery: string) {
    const body = { query: userQuery }
    return this.http.post<{ response: string}>('api/chatbot', body)
  }
}
