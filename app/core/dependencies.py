from fastapi import Depends, Header, HTTPException
from app.core.securitu import verify_token
from app.core.config import seating

def get_api_key(api_key: str = Header(...)):
    if api_key != seating.API_KEY:
        raise HTTPException(status_code=403, detail="Could not validate API key")
    return api_key

def get_current_user(token: str = Header(...)):
    payload = verify_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    return payload 
