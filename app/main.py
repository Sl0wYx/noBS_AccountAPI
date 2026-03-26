from fastapi import FastAPI, Depends

from app.routers import accounts
from app.routers import stats
from app.routers import online
from app.routers import recieve_message
app = FastAPI()

app.include_router(accounts.router)
app.include_router(stats.router)
app.include_router(online.router)
app.include_router(recieve_message.router)



