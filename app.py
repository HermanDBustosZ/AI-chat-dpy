from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import aiRouter  # Asegúrate que la carpeta se llame 'routers' y contenga 'aiRouter.py'

app = FastAPI()

# Habilita CORS si vas a conectarte desde frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Origen
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar el router del chatbot
app.include_router(aiRouter.router)

@app.get("/")
def index():
    return {"Message": "API running"}