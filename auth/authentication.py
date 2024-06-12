from fastapi import HTTPException, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from auth.token_services import token_service
from jwt import PyJWTError

class AuthenticationService:
    security = HTTPBearer()

    def get_current_user(self, credentials: HTTPAuthorizationCredentials = Depends(security)):
        credentials_exception = HTTPException(
            status_code=401,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

        token = credentials.credentials

        try:
            payload = token_service.decode_access_token(token)

            if payload is None:
                raise credentials_exception

            return payload
        except PyJWTError:
            raise credentials_exception

authentication_service = AuthenticationService()