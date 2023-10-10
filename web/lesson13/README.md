1. Run docker-compose   
`docker-compose up`

2. Create db

3. Run alembic migrations:  
`alembic init alembic`   
`alembic revision --autogenerate -m 'Init'`   
`alembic upgrade head`

4. Run server:   
`uvicorn main:app --host localhost --port 8000 --reload`