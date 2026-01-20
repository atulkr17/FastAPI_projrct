import os 
from dotenv import load_dotenv

load_dotenv()

class Seating:
    API_KEY = os.getenv('API_KEY' , 'demo-key')
    PROJECT_NAME = 'FastAPI' 
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'supersecret')
    REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379')
    JWT_ALGORITHM = 'HS256'
    MODAL_PATH = 'app/models/model.pkl'


seating = Seating()    