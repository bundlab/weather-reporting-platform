![Docker](https://img.shields.io/badge/Docker-Enabled-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Version](https://img.shields.io/badge/Release-v1.0.0-brightgreen)

# 🌦️ Weather Reporting System

A **modern, full-stack Weather Reporting System** built with **FastAPI**, **PostgreSQL**, and a **beautiful frontend UI**.  
This application fetches **real-time weather data**, stores historical records, and provides a clean API for integration.

> 🚀 Designed & built by **Abdullahi Bundi (Bundlab)**

---

## ✨ Features

✅ Real-time weather data (OpenWeather API)  
✅ City-based weather search  
✅ Weather history stored in PostgreSQL  
✅ RESTful API (FastAPI)  
✅ Modern, responsive UI  
✅ Docker & Docker Compose support  
✅ Production-ready & GitHub-ready  

---

## 🧠 Tech Stack

### Backend
- **FastAPI**
- **Python 3.10+**
- **SQLAlchemy**
- **PostgreSQL**
- **OpenWeather API**

### Frontend
- **HTML5**
- **CSS3 (Modern UI)**
- **JavaScript (Fetch API)**

### DevOps
- **Docker**
- **Docker Compose**

---

## 📁 Project Structure
weather-reporting-flatform/
│── backend/
│ ├── app/
│ │ ├── main.py
│ │ ├── config.py
│ │ ├── database.py
│ │ ├── models.py
│ │ ├── weather.py
│ ├── requirements.txt
│ └── Dockerfile
│
│── frontend/
│ ├── index.html
│ ├── style.css
│ └── script.js
│
│── docker-compose.yml
│── README.md
│── .gitignore


---

## 🔑 API Overview

| Method | Endpoint | Description |
|------|--------|------------|
| GET | `/weather/{city}` | Fetch & store real-time weather |

📘 Interactive Docs available at:

http://localhost:8000/docs


---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository
```bash
git clone https://github.com/bundlab/weather-reporting-system.git
cd weather-reporting-system
### 2️⃣ Add OpenWeather API Key

Edit docker-compose.yml:

OPENWEATHER_API_KEY: your_api_key_here

Get your API key from:
👉 https://openweathermap.org/api

## 🐳 Run with Docker (Recommended)
docker-compose up --build

✅ Backend runs on:

http://localhost:8000

✅ Frontend:

Open frontend/index.html in your browser
## 🖥️ Run Without Docker (Optional)
Backend
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
