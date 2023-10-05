from fastapi import FastAPI

import src.router.contacts as contacts


app = FastAPI()

app.include_router(contacts.router, prefix='/contacts')
