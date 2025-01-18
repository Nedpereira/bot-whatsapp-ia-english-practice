from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_WHATSAPP_NUMBER = os.getenv('TWILIO_WHATSAPP_NUMBER')

if not all([TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_WHATSAPP_NUMBER, GEMINI_API_KEY]):
    raise ValueError("As credenciais não foram configuradas corretamente no arquivo .env")

app = Flask(__name__)

@app.route("/webhook", methods=['POST'])
def webhook():
    try:
        mensagem_recebida = request.form.get('Body')
        numero_remetente = request.form.get('From')

        if not mensagem_recebida or not numero_remetente:
            return "Mensagem inválida", 400

        print(f"Mensagem recebida de {numero_remetente}: {mensagem_recebida}")

        resposta = gerar_resposta(mensagem_recebida) # Gera uma resposta usando o Gemini

        print(f"Resposta gerada: {resposta}")

        resp = MessagingResponse()
        resp.message(resposta)
        return str(resp)
    except Exception as e:
        print(f"Erro ao processar mensagem: {e}")
        return str(MessagingResponse().message("Desculpe, ocorreu um erro. Tente novamente mais tarde."))

def gerar_resposta(mensagem):
    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(
             f"""
        You are an English teaching assistant named Lily. I am a beginner learning English, practicing on WhatsApp.
        Your task is to help me improve my English. Please respond following these rules:

        1. Respond to my message in English naturally, to continue the conversation.
        2. If there are mistakes in my message, provide a **separate correction**.
        3. Include an **intuitive pronunciation guide** for your response that a beginner can easily understand (e.g., "Hai" for "Hi").
        4. Translate your response to Portuguese for better understanding.
        5. Always continue the conversation by asking a friendly and relevant question to encourage me to practice more.

        Respond **only** in this format, without adding extra lines or additional text:
        *message:* <Your response in English>  
        *correção:* <Corrections if needed>  
        *pronúncia:* <Intuitive pronunciation of your response>  
        *tradução:* <Translation to Portuguese>  

        User message: {mensagem}
        """
        )

        return response.text
    except Exception as e:
        print(f"Erro ao gerar resposta: {e}")
        return "Desculpa, não consegui processar sua mensagem."
    
if __name__ == "__main__":
    app.run(debug=True)