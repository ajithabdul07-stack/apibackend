from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import router
import os 

app = FastAPI()

origins = os.getenv("ALLOWED_ORIGINS", "*").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api")


# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def home():
#     return {"message": "Hello from FastAPI on Vercel"}

