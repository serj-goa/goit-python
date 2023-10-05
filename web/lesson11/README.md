alembic init alembic
alembic revision --autogenerate -m 'Init'
alembic upgrade head

uvicorn main:app --host localhost --port 8000 --reload