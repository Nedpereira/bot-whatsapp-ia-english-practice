# Bot de Prática de Inglês no WhatsApp com IA 🤖

# PT
Este repositório contém o código-fonte de um bot de WhatsApp que utiliza inteligência artificial (IA) para ajudar usuários a praticar inglês. O bot foi desenvolvido usando:

# En
This repository contains the source code for a WhatsApp bot that uses artificial intelligence (AI) to help users practice English. The bot was developed using:

- **Twilio**: Para gerenciar as mensagens do WhatsApp.
- **Ngrok**: Para expor o servidor local e receber mensagens em tempo real.
- **Python e Flask**: Para criar a lógica do bot e a API.
- **Gemini API**: Para gerar respostas inteligentes e corrigir erros de inglês.

# PT
O bot atua como um assistente de ensino de inglês, corrigindo erros, fornecendo pronúncias intuitivas e traduções para facilitar o aprendizado.

# En
The bot acts as an English teaching assistant, providing corrections, intuitive pronunciations, and translations to facilitate learning.

## Pré-requisitos

Antes de começar, você precisará ter instalado:

- [Python 3.x](https://www.python.org/downloads/)
- [Pip](https://pip.pypa.io/en/stable/installation/) (gerenciador de pacotes do Python)
- [Ngrok](https://ngrok.com/download) (para expor o servidor local)
- Uma conta no [Twilio](https://www.twilio.com/try-twilio) (para gerenciar mensagens do WhatsApp)
- Uma chave de API do [Google Gemini](https://ai.google.dev/) (para a IA)

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/Nedpereira/bot-whatsapp-ia-english-practice.git

2. Navegue até o diretório do projeto:
   ```bash
   cd bot-whatsapp-ia-english-practice

3. Crie um ambiente virtual (venv) para isolar as dependências do projeto:
   ```bash
   python -m venv venv

4. Ative o ambiente virtual:
   No Windows:
    ```bash
    venv\Scripts\activate
    ```
    no MacOS/Linux:
    ```bash
    source venv/bin/activate

5. Instale as dependências:
   ```bash
   pip install -r requirements.txt

6. Crie um arquivo .env na raiz do projeto e adicione suas credenciais:
   ```bash
   TWILIO_ACCOUNT_SID=seu_account_sid
   TWILIO_AUTH_TOKEN=seu_auth_token
   TWILIO_WHATSAPP_NUMBER=whatsapp:+seu_numero_twilio
   GEMINI_API_KEY=sua_chave_gemini
   
*Observação*: Não compartilhe o arquivo .env publicamente, pois ele contém informações sensíveis.

7. Inicie o servidor Flask:
   ```bash
   python bot.py
   
*Observação*: Por padrão, o Flask roda na porta 5000. Se você alterar a porta no código, certifique-se de usar a porta correta nas próximas etapas.

8. Inicie o Ngrok para expor o servidor local:
   ```bash
   ngrok http 5000

*O Ngrok gerará uma URL pública (por exemplo, https://abcd1234.ngrok.io). Copie essa URL.*

9. Configure o webhook no Twilio:
   Acesse o Console do Twilio.
   Vá para o menu "WhatsApp" > "Sandbox".
   Cole a URL do Ngrok seguida de /webhook no campo "When a message comes in" (ex: https://abcd1234.ngrok.io/webhook).
   Salve as configurações.

## Como usar

1. Envie uma mensagem para o número do WhatsApp configurado no Twilio.
2. O bot responderá com:
   - Uma resposta em inglês.
   - Correções de erros (se houver).
   - Uma pronúncia intuitiva.
   - Uma tradução para o português.
   - Uma pergunta para continuar a conversa.

## Exemplo de Conversa

 Você:
   ```bash
   Hello, how are you?
   ```

 Bot:
  ```bash
  *message:* Hi! I'm doing great, thank you! How about you?  
  *correção:* No mistakes.  
  *pronúncia:* Hai! Aim duing greit, thenk yu! Hau abaute yu?  
  *tradução:* Oi! Estou ótimo, obrigada! E você?  
  ```

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
