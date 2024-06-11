from fastapi import FastAPI
from app.routers.router import routers

app = FastAPI()
app.include_router(router=routers)