# 🏥 Advanced Lifestyle Health Advisor

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Gradio](https://img.shields.io/badge/Gradio-4.36.1-green.svg)](https://gradio.app)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.112.2-red.svg)](https://fastapi.tiangolo.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-sathya--rs6-black.svg)](https://github.com/sathya-rs6)

A comprehensive AI-powered health recommendation system with data storage, analytics, and personalized lifestyle suggestions. Built with advanced machine learning models and modern web technologies.

> **Developer**: [@sathya-rs6](https://github.com/sathya-rs6) | **Repository**: [lifestyle-health-advisor](https://github.com/sathya-rs6/lifestyle-health-advisor)

## ✨ Features

### 🎯 Core Functionality
- **AI-Powered Health Assessment**: Advanced machine learning model with 93.81% accuracy
- **Personalized Recommendations**: Tailored health suggestions based on individual profiles
- **Data Storage & Analytics**: SQLite database with health history tracking
- **User Dashboard**: Comprehensive health analytics and progress monitoring
- **Multi-Interface Support**: Web UI, REST API, and programmatic access

### 🏃‍♂️ Health Metrics Analyzed
- **Physical Activity**: Activity level assessment and recommendations
- **Stress Management**: Stress level analysis with coping strategies
- **Sleep Health**: Sleep disorder detection and improvement suggestions
- **Cardiovascular Health**: Heart rate and blood pressure monitoring
- **BMI & Weight Management**: Body composition analysis
- **Daily Activity**: Step counting and movement recommendations

### 📊 Advanced Features
- **User Profiles**: Save and manage multiple user profiles
- **Health History**: Track health metrics over time
- **Analytics Dashboard**: View trends and progress
- **Data Export**: Export health data for analysis
- **Risk Assessment**: Identify health risk factors
- **Progress Tracking**: Monitor health improvements

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/sathya-rs6/lifestyle-health-advisor.git
cd lifestyle-health-advisor
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run the application:**
```bash
# Basic version
python app.py

# Advanced version with data storage
python app_advanced.py
```

4. **Access the application:**
   - Web Interface: `http://localhost:7860`
   - API Documentation: `http://localhost:8000/docs`

## 🎮 Usage

### Web Interface
1. **Health Assessment Tab**: Fill in your health information and get personalized recommendations
2. **Dashboard Tab**: View your health history and analytics using your User ID
3. **Data Management Tab**: Manage users and export health data

### API Usage
```python
import requests

# Health suggestions
data = {
    "age": 30,
    "physical_activity_level": 5.0,
    "stress_level": 4.0,
    "gender": "Male",
    "heart_rate": 75.0,
    "blood_pressure": 120.0,
    "sleep_disorder": "None"
}

response = requests.post("http://localhost:8000/suggest", json=data)
print(response.json())
```

## 📁 Project Structure

```
lifestyle-health-advisor/
├── 📱 Frontend Applications
│   ├── app.py                    # Basic Gradio interface
│   ├── app_advanced.py           # Advanced interface with data storage
│   └── frontend/
│       └── index.html            # Alternative web interface
├── 🔧 Backend Services
│   ├── backend/
│   │   ├── main.py              # FastAPI server
│   │   ├── inference.py         # Model inference
│   │   ├── train_model.py       # Model training
│   │   └── artifacts/           # Trained models
│   └── database.py              # SQLite database management
├── 📊 Data & Analysis
│   ├── data_analysis.py         # Dataset analysis
│   ├── test_model.py            # Model testing
│   └── Sleep_health_and_lifestyle_dataset.csv
├── 🚀 System Files
│   ├── start_system.py          # System launcher
│   ├── requirements.txt         # Dependencies
│   └── README.md               # Documentation
└── 📋 Generated Files
    ├── health_data.db           # SQLite database (created on first run)
    └── sleep_health_analysis.png
```

## 🧠 Machine Learning Model

### Model Performance
- **Accuracy**: 93.81%
- **Dataset**: 374 health profiles
- **Features**: 12+ health and lifestyle metrics
- **Algorithm**: Advanced ensemble learning

### Training Data
The model is trained on comprehensive health data including:
- Sleep quality and disorders
- Physical activity levels
- Stress indicators
- Cardiovascular metrics
- Lifestyle factors
- Demographic information

## 🗄️ Database Schema

### Users Table
- User profiles with personal information
- Registration timestamps
- Health preferences

### Health Records Table
- Individual health assessments
- Risk factors and positive factors
- Personalized suggestions
- Timestamp tracking

### Analytics Table
- Health metrics over time
- Trend analysis data
- Progress tracking

## 🔧 Development

### Running Tests
```bash
python test_model.py
```

### Training the Model
```bash
python backend/train_model.py
```

### Data Analysis
```bash
python data_analysis.py
```

### Database Management
```python
from database import HealthDatabase

# Initialize database
db = HealthDatabase()

# Create user
user_id = db.create_user("John Doe", age=30, gender="Male")

# Save health record
db.save_health_record(user_id, health_data)

# Get user dashboard
dashboard = db.get_user_health_history(user_id)
```

## 📈 API Endpoints

### Health Suggestions
**POST** `/suggest`
```json
{
    "age": 30,
    "physical_activity_level": 5.0,
    "stress_level": 4.0,
    "gender": "Male",
    "heart_rate": 75.0,
    "blood_pressure": 120.0,
    "sleep_disorder": "None"
}
```

### Model Predictions
**POST** `/predict`
```json
{
    "age": 30,
    "gender": "Male",
    "sleep_duration": 7.5,
    "quality_of_sleep": 8.0,
    "physical_activity_level": 5.0,
    "stress_level": 4.0,
    "bmi_category": "Normal",
    "heart_rate": 75.0,
    "daily_steps": 8000
}
```

## 🎨 Screenshots

### Health Assessment Interface
- Modern, responsive design
- Intuitive form layout
- Real-time suggestions
- Data storage options

### Analytics Dashboard
- Health history tracking
- Trend visualization
- Progress monitoring
- Export capabilities

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit your changes**: `git commit -m 'Add amazing feature'`
4. **Push to the branch**: `git push origin feature/amazing-feature`
5. **Open a Pull Request**

### Development Guidelines
- Follow PEP 8 style guidelines
- Add tests for new features
- Update documentation
- Ensure backward compatibility

## 📋 Roadmap

### Version 2.0
- [ ] Mobile app development
- [ ] Wearable device integration
- [ ] Advanced analytics with charts
- [ ] Multi-language support
- [ ] Cloud deployment options

### Version 3.0
- [ ] AI-powered health coaching
- [ ] Integration with health APIs
- [ ] Real-time health monitoring
- [ ] Community features
- [ ] Health challenges and gamification

## 🛡️ Security & Privacy

- **Local Data Storage**: All data stored locally in SQLite
- **No External Sharing**: Health data never leaves your system
- **Secure API**: Input validation and error handling
- **Privacy First**: No tracking or data collection

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Dataset**: Sleep Health and Lifestyle Dataset
- **Machine Learning**: Scikit-learn, Pandas, NumPy
- **Web Framework**: Gradio, FastAPI, Uvicorn
- **Data Visualization**: Matplotlib, Seaborn
- **Database**: SQLite3

## ⚠️ Disclaimer

This tool provides general health suggestions and should not replace professional medical advice. Always consult healthcare providers for medical concerns.

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/sathya-rs6/lifestyle-health-advisor/issues)
- **Discussions**: [GitHub Discussions](https://github.com/sathya-rs6/lifestyle-health-advisor/discussions)
- **Profile**: [GitHub Profile](https://github.com/sathya-rs6)

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=sathya-rs6/lifestyle-health-advisor&type=Date)](https://star-history.com/#sathya-rs6/lifestyle-health-advisor&Date)

---

**Made with ❤️ for better health and lifestyle management**
