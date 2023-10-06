#### Run alembic migrations:  
`alembic init alembic`   
`alembic revision --autogenerate -m 'Init'`   
`alembic upgrade head`   

#### Run server:   
`uvicorn main:app --host localhost --port 8000 --reload`