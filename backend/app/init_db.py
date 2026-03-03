from app.database import Base, engine
from app.models import Weather

def init():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init()