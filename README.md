![CI](https://github.com/bundlab/weather-reporting-platform/actions/workflows/ci.yml/badge.svg)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![Nginx](https://img.shields.io/badge/Nginx-ReverseProxy-darkgreen)
![Python](https://img.shields.io/badge/Python-3.11-yellow)
![License](https://img.shields.io/badge/License-MIT-brightgreen)
![Release](https://img.shields.io/github/v/release/bundlab/weather-reporting-platform)
![Last Commit](https://img.shields.io/github/last-commit/bundlab/weather-reporting-platform)
![Repo Size](https://img.shields.io/github/repo-size/bundlab/weather-reporting-platform)
![Stars](https://img.shields.io/github/stars/bundlab/weather-reporting-platform?style=social)

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
---bash 
weather-reporting-platform/
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

## ⚙️ Installation & Setup

1️⃣ Clone Repository
```bash
git clone https://github.com/bundlab/weather-reporting-system.git
cd weather-reporting-system

2️⃣ Add OpenWeather API Key

Edit docker-compose.yml:

OPENWEATHER_API_KEY: your_api_key_here

Get your API key from:
👉 https://openweathermap.org/api