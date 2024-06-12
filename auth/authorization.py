
from fastapi import HTTPException, Depends
from auth.authentication import authentication_service

class AuthorizationService:
    def check_role(self, role: str):
        def _check_role(current_user: dict = Depends(authentication_service.get_current_user)):
            if current_user.get("role") != role:
                raise HTTPException(status_code=403, detail="You don't have enough permissions")
            return current_user

        return _check_role

authorization_service = AuthorizationService()
