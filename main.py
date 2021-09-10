from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
app = FastAPI(dependencies=[Depends(oauth2_scheme)])

@app.get("/items/")
async def read_items(token: str):
    return {"token": token}