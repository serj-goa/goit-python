from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routes import auth, contacts, users
from src.middlewares.middlewares import ban_ips_middleware, limit_access_by_ip, startup_event, user_agent_ban_middleware


origins = ['https://localhost:3000']

app = FastAPI()

app.include_router(auth.router, prefix='/api')
app.include_router(contacts.router, prefix='/api')
app.include_router(users.router, prefix='/api')

app.add_event_handler('startup', startup_event)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.middleware('http')(limit_access_by_ip)
app.middleware('http')(ban_ips_middleware)
app.middleware('http')(user_agent_ban_middleware)
