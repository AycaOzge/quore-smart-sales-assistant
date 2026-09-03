import os
import requests
from flask import current_app

class AIServiceError(Exception):
    pass

class AIService:
    @staticmethod
    def yanit_uret(mesaj, gecmis=None):
        api_key = current_app.config.get('GROQ_API_KEY')
        if not api_key:
            raise AIServiceError("Groq API anahtarı bulunamadı!")

        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        business_context = current_app.config.get('BUSINESS_CONTEXT', 'Yardımcı bir yapay zekâ asistanısın.')

        messages = [
            {"role": "system", "content": business_context}
        ]

        if gecmis:
            for m in gecmis:
                messages.append(m)

        messages.append({"role": "user", "content": mesaj})

        payload = {
            "model": "openai/gpt-oss-20b",
            "messages": messages,
            "temperature": 0.7
        }

        try:
            response = requests.post(url, json=payload, headers=headers, timeout=10)
            if response.status_code != 200:
                raise AIServiceError(f"Groq API hatası: {response.text}")
            
            data = response.json()
            return data['choices'][0]['message']['content']
        except Exception as e:
            raise AIServiceError(f"Yapay zekâ servisi çalıştırılamadı: {str(e)}")