# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 22:41:21 2023

@author: 1
"""

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import uvicorn
from typing import Union, Optional, Dict, Any, Coroutine
import uvicorn
from fastapi import Depends, FastAPI, HTTPException, status, Request, Response, encoders
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm, \
    OAuth2
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel
from jose import JWTError, jwt

app = FastAPI()
security = HTTPBasic()

class OAuth2PasswordBearerWithCookie(OAuth2):
    def __init__(
            self,
            token_url: str,
            scheme_name: Optional[str] = None,
            scopes: Optional[Dict[str, str]] = None,
            auto_error: bool = True,
    ):
        if not scopes:
            scopes = {}
        flows = OAuthFlowsModel(password={"tokenUrl": token_url, "scopes": scopes})
        super().__init__(flows=flows, scheme_name=scheme_name, auto_error=auto_error)
  

    async def __call__(self, request: Request) -> Optional[str]:
        authorization: str = request.cookies.get("Authorization") 