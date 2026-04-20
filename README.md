# 🤖 AI Voice Agent

> A full-stack web application that triggers real, intelligent outbound phone calls powered by **Vapi AI** — with a sleek dark-mode UI built on Flask.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0.3-black?logo=flask)
![Vapi AI](https://img.shields.io/badge/Vapi-AI%20Voice-purple)
![License](https://img.shields.io/badge/License-MIT-green)

---

## ✨ Features

- 📞 **Outbound AI Calls** — Trigger real phone calls via the [Vapi AI](https://vapi.ai) API
- 🎙️ **Dynamic Message Types** — Choose from Sales, Support, or Default call personas
- 🌐 **Modern UI** — Glassmorphism dark-mode design with smooth animations
- ✅ **Phone Validation** — E.164 format validation on both frontend and backend
- 🔒 **Secure Config** — Credentials stored safely in `.env` (never committed to git)
- 🚀 **Production Ready** — Gunicorn support for deployment

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | HTML5, Vanilla CSS, Vanilla JavaScript |
| Backend | Python, Flask |
| AI Voice | Vapi AI API |
| Deployment | Gunicorn |

---

## 📁 Project Structure

```
ai-voice-agent/
├── app.py                  # Flask backend & Vapi API integration
├── requirements.txt        # Python dependencies
├── .env                    # 🔒 Your secret credentials (NOT committed)
├── .gitignore              # Ignores venv, .env, __pycache__
├── templates/
│   └── index.html          # Main UI page
└── static/
    ├── css/
    │   └── style.css       # Dark mode glassmorphism styles
    └── js/
        └── main.js         # Frontend logic & API calls
```

---

## ⚡ Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/manndoshi15/ai-voice-agent.git
cd ai-voice-agent
```

### 2. Create & Activate Virtual Environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory:
```env
VAPI_API_KEY=your_vapi_api_key_here
VAPI_ASSISTANT_ID=your_assistant_id_here
VAPI_PHONE_NUMBER_ID=your_phone_number_id_here
```

> 💡 Get your credentials from the [Vapi Dashboard](https://dashboard.vapi.ai)

### 5. Run the Application
```bash
python app.py
```

Open your browser at: **[http://localhost:5000](http://localhost:5000)**

---

## 🎯 How It Works

1. Enter a phone number in **E.164 format** (e.g., `+911234567890`)
2. Select a **Message Type**: Default, Sales, or Support
3. Click **"Call Now"**
4. Vapi AI initiates the call with your configured AI assistant
5. The recipient receives a real phone call from your AI agent!

### Message Types

| Type | First Message |
|------|--------------|
| Default | *"Hello! I'm your AI voice assistant. How can I help you today?"* |
| Sales | *"Hi! I'm calling to check if you'd like to renew your AI subscription."* |
| Support | *"Hello! I'm calling because your support ticket has been resolved..."* |

---

## 🌍 Production Deployment (Gunicorn)

For production, use Gunicorn instead of Flask's dev server:

```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

---

## 🔐 Security Notes

- **Never commit your `.env` file** — it's listed in `.gitignore`
- Rotate your Vapi API key if it gets exposed
- Use environment variables or a secrets manager in production

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

<p align="center">Built with ❤️ using Flask & Vapi AI</p>
