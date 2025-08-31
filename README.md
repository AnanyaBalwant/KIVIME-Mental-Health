# 🧠 MindCare - Mental Healthcare Companion

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.1.2-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PWA](https://img.shields.io/badge/PWA-Ready-orange.svg)](https://web.dev/progressive-web-apps/)

A comprehensive mental health companion web application that provides stress detection, therapeutic activities, and AI-powered mental health support. Built with Flask and designed as a Progressive Web App (PWA).

## ✨ Features

### 🎯 Core Functionality
- **Stress Level Detection**: ML-powered stress assessment using vital signs
- **AI Mental Health Chatbot**: Gemini-powered conversational support
- **Personal Journal**: Mood tracking and thought recording
- **Music Therapy**: Relaxing audio with nature sounds
- **Yoga & Exercise Guide**: Step-by-step yoga poses and instructions
- **Interactive Games & Quizzes**: Focus and attention improvement activities

### 🔐 User Management
- Secure user registration and authentication
- Personalized user experience with session management
- Individual journal storage per user

### 📱 Progressive Web App
- Installable on mobile and desktop devices
- Offline capability with service workers
- Responsive design for all screen sizes

### 🎨 Modern UI/UX
- Bootstrap-based responsive design
- Multiple color themes and customization options
- Smooth animations and transitions
- Mobile-first approach

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Google Gemini API key (for chatbot functionality)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/MindCare-MentalHealthcare.git
   cd MindCare-MentalHealthcare
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Create a .env file or set environment variables
   export GEMINI_API_KEY="your_gemini_api_key_here"
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open your browser**
   Navigate to `http://localhost:5000`

## 🏗️ Project Structure

```
MindCare-MentalHealthcare/
├── app.py                 # Main Flask application
├── chatbot.py            # AI chatbot implementation
├── requirements.txt      # Python dependencies
├── Procfile             # Heroku deployment configuration
├── static/              # Static assets (CSS, JS, images)
│   ├── assets/         # Main assets and vendor libraries
│   ├── css/            # Custom stylesheets
│   ├── js/             # JavaScript files
│   ├── sounds/         # Audio files for music therapy
│   ├── yoga/           # Yoga pose GIFs and images
│   └── manifest.json   # PWA manifest
├── templates/           # HTML templates
│   ├── base.html       # Base template
│   ├── index.html      # Homepage
│   ├── journal.html    # Journal interface
│   ├── music.html      # Music player
│   ├── exercises.html  # Yoga and exercise guide
│   ├── stress.html     # Stress detection form
│   └── quizandgame.html # Games and quizzes
├── journals/            # User journal storage
└── users.json          # User database
```

## 🎮 Features in Detail

### 🧘‍♀️ Stress Detection
- Input vital signs (sleep, blood pressure, respiration, heart rate)
- Machine learning model predicts stress levels
- Personalized recommendations based on results

### 💬 AI Chatbot
- Powered by Google Gemini AI
- Mental health conversation support
- Safety filters and empathetic responses
- Professional help recommendations when needed

### 📝 Personal Journal
- Daily mood tracking with emoji selection
- Private thought recording
- Entry management (create, view, delete)
- User-specific storage

### 🎵 Music Therapy
- Nature sounds (rain, beach, birds)
- Ambient music for relaxation
- Custom audio player with controls
- Background music for stress relief

### 🧘‍♂️ Yoga & Exercise
- Step-by-step yoga pose instructions
- Animated GIF demonstrations
- Breathing techniques
- Morning routine recommendations

### 🎯 Games & Quizzes
- Focus improvement activities
- Attention training exercises
- Interactive learning modules
- Progress tracking

## 🔧 Configuration

### Environment Variables
```bash
GEMINI_API_KEY=your_gemini_api_key_here
FLASK_ENV=development
SECRET_KEY=your_secret_key_here
```

### API Keys
- **Google Gemini**: Required for chatbot functionality
- Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

## 🚀 Deployment

### Heroku
The project includes a `Procfile` for easy Heroku deployment:

```bash
# Install Heroku CLI
heroku create your-app-name
git push heroku main
```

### Other Platforms
- **Vercel**: Supports Python applications
- **Railway**: Easy Python deployment
- **DigitalOcean App Platform**: Scalable hosting

## 🛠️ Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap
- **AI**: Google Gemini API
- **Machine Learning**: scikit-learn, NumPy
- **Database**: JSON-based storage
- **Authentication**: Flask-Login
- **PWA**: Service Workers, Manifest

## 📱 PWA Features

- **Installable**: Add to home screen on mobile/desktop
- **Offline Support**: Service worker caching
- **Responsive**: Works on all device sizes
- **Fast Loading**: Optimized assets and caching

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 Python style guidelines
- Add comments for complex logic
- Test your changes thoroughly
- Update documentation as needed

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Bootstrap**: UI framework and components
- **Google Gemini**: AI chatbot capabilities
- **Flask**: Web framework
- **Open Source Community**: Various libraries and tools

## 📞 Support

If you have any questions or need help:

- **Issues**: [GitHub Issues](https://github.com/yourusername/MindCare-MentalHealthcare/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/MindCare-MentalHealthcare/discussions)
- **Email**: your.email@example.com

## 🔮 Roadmap

- [ ] Enhanced ML models for stress detection
- [ ] Integration with wearable devices
- [ ] Community features and support groups
- [ ] Professional therapist matching
- [ ] Mobile app development
- [ ] Multi-language support

## ⚠️ Disclaimer

This application is designed to provide mental health support and information but is not a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of qualified health providers with questions about medical conditions.

---

**Made with ❤️ for mental health awareness and support**

*If you find this project helpful, please give it a ⭐ star on GitHub!* 