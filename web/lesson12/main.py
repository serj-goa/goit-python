from fastapi import FastAPI

from src.routes import auth, contacts


app = FastAPI()

app.include_router(auth.router, prefix='/api')
app.include_router(contacts.router, prefix='/api')
