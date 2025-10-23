# 👧🏼 Noor – Your Personal AI Assistant

A voice-activated AI assistant with webcam integration, powered by Google's Gemini AI, Groq's Whisper, and ElevenLabs text-to-speech. Noor can see through your webcam, listen to your voice commands, and respond naturally with a witty personality.

## ✨ Features

- 🎤 **Voice Recognition**: Continuous listening mode with automatic speech-to-text using Groq's Whisper model
- 👁️ **Vision Capabilities**: Webcam integration with real-time image analysis using Llama Vision model
- 🗣️ **Natural Speech**: High-quality text-to-speech responses using ElevenLabs (with gTTS fallback)
- 🤖 **Intelligent Agent**: Powered by Google's Gemini 2.0 Flash with LangGraph for tool orchestration
- 🖥️ **Modern UI**: Beautiful Gradio interface with live webcam feed and chat interface
- 🔄 **Real-time Processing**: Seamless conversation flow with automatic tool calling

## 🛠️ Tech Stack

- **AI Models**: 
  - Google Gemini 2.0 Flash (main reasoning)
  - Groq Whisper Large V3 (speech-to-text)
  - Meta Llama 4 Maverick 17B (vision analysis)
  - ElevenLabs (text-to-speech)
- **Frameworks**: 
  - LangChain & LangGraph (agent orchestration)
  - Gradio (web interface)
  - OpenCV (webcam capture)
- **Audio Processing**: 
  - SpeechRecognition
  - PyDub
  - gTTS (fallback TTS)

## 📋 Prerequisites

- Python 3.13 or higher
- Webcam
- Microphone
- API Keys for:
  - Google Gemini API
  - Groq API
  - ElevenLabs API

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ParamnoorSingh15/Param-AI-Assistant.git
   cd Param-AI-Assistant
   ```

2. **Install uv (if not already installed)**
   ```bash
   pip install uv
   ```

3. **Install dependencies**
   ```bash
   uv sync
   ```

   Or using pip:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the root directory:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   GOOGLE_API_KEY=your_google_gemini_api_key_here
   ELEVEN_LABS_API_KEY=your_elevenlabs_api_key_here
   ```

   **Getting API Keys:**
   - **Groq API**: Sign up at [console.groq.com](https://console.groq.com)
   - **Google Gemini**: Get your key at [ai.google.dev](https://ai.google.dev)
   - **ElevenLabs**: Create account at [elevenlabs.io](https://elevenlabs.io)

## 🎮 Usage

1. **Start the application**
   ```bash
   python main.py
   ```

2. **Access the interface**
   - The app will launch at `http://localhost:7860`
   - A shareable link will also be generated for remote access

3. **Using Noor**
   - Click "Start Camera" to activate the webcam feed
   - The assistant automatically starts listening when the app loads
   - Speak your questions or commands
   - Noor will respond with voice and text
   - Say "goodbye" to end the conversation

## 💡 Example Interactions

- **Vision queries**: "What do you see?", "How many people are in front of me?", "What color is my shirt?"
- **General questions**: "What's the weather like?", "Tell me a joke", "What's 25 times 17?"
- **Exit command**: "Goodbye" (ends the session)

## 📁 Project Structure

```
Param-AI-Assistant/
├── main.py                 # Gradio UI and main application
├── ai_agent.py            # LangGraph agent with Gemini
├── speech_to_text.py      # Audio recording and transcription
├── text_to_speech.py      # TTS with ElevenLabs and gTTS
├── tools.py               # Webcam capture and vision analysis
├── pyproject.toml         # Project dependencies
├── .env                   # API keys (not in git)
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## 🔧 Configuration

### Webcam Settings
Modify in `main.py`:
```python
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
camera.set(cv2.CAP_PROP_FPS, 30)
```

### Voice Settings
Adjust in `speech_to_text.py`:
```python
def record_audio(file_path, timeout=20, phrase_time_limit=20):
```

### AI Personality
Customize Noor's behavior in `ai_agent.py`:
```python
system_prompt = """You are Noor - a witty, clever, and helpful assistant..."""
```

## 🎨 Features in Detail

### Voice Recognition
- Automatic ambient noise adjustment
- Configurable timeout and phrase limits
- High-quality MP3 audio encoding
- Groq Whisper for accurate transcription

### Vision Analysis
- Automatic webcam detection (tries indices 0-3)
- Base64 image encoding for API transmission
- Context-aware image analysis with Llama Vision
- Seamless integration with conversational flow

### Text-to-Speech
- Primary: ElevenLabs with natural voice (ZF6FPAbjXT4488VcRRnw)
- Fallback: Google Text-to-Speech (gTTS)
- Cross-platform audio playback (Windows, macOS, Linux)

### Agent Intelligence
- Automatic tool selection based on query context
- No permission asking - proactive webcam usage
- Natural, witty responses in Noor's personality
- ReAct pattern for reasoning and acting

## 🐛 Troubleshooting

**Webcam not detected:**
- Ensure no other application is using the webcam
- Check camera permissions in your OS settings
- Try different camera indices in `tools.py`

**Audio issues:**
- Verify microphone permissions
- Check default audio input/output devices
- Install system audio dependencies (e.g., `portaudio` on Linux)

**API errors:**
- Verify all API keys are correct in `.env`
- Check API rate limits and quotas
- Ensure stable internet connection

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

**Paramnoor Singh**
- GitHub: [@ParamnoorSingh15](https://github.com/ParamnoorSingh15)

## 🙏 Acknowledgments

- Google Gemini for powerful language understanding
- Groq for lightning-fast inference
- ElevenLabs for natural voice synthesis
- LangChain team for excellent agent frameworks
- Gradio for the beautiful UI framework

---

**Note**: This project requires active API keys and may incur costs based on usage. Please review the pricing of each service before extensive use.
