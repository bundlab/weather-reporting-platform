from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import Base, engine, SessionLocal
from .models import Weather
from .weather import get_weather


app = FastAPI(title="Weather Reporting System")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/weather/{city}")
def fetch_weather(city: str, db: Session = Depends(get_db)):
    data = get_weather(city)
    weather = Weather(**data)
    db.add(weather)
    db.commit()
    return data

@app.get("/health")
def health_check():
    return {"status": "healthy"}