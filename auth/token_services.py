from datetime import datetime, timedelta
import jwt
from jwt import PyJWTError
from fastapi import HTTPException

import os

SECRET_KEY = os.getenv("SECRET_KEY") or "secret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1

class TokenService:
    def create_access_token(self, data: dict):
        to_encode = data.copy()
        expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": int(expire.timestamp())})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    
    def decode_access_token(self, token: str):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            return payload
        except PyJWTError:
            raise HTTPException(status_code=401, detail="Could not validate credentials")


token_service = TokenService()