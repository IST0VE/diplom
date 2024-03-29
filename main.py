from fastapi import FastAPI, Form, HTTPException
from typing import Optional
import databases
import sqlalchemy

DATABASE_URL = "mysql://root:root@localhost/test2"
database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("username", sqlalchemy.String(length=50)),
    sqlalchemy.Column("password", sqlalchemy.String(length=50)),
    sqlalchemy.Column("role", sqlalchemy.String(length=50)),
)

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.post("/test/v1/reg/")
async def register_user(username: str = Form(...), password: str = Form(...), role: str = Form(...)):
    query = users.insert().values(username=username, password=password, role=role)
    last_record_id = await database.execute(query)
    return {"id": last_record_id, "username": username, "role": role}

@app.post("/test/v1/auth/")
async def authenticate_user(username: str = Form(...), password: str = Form(...)):
    query = users.select().where(users.c.username == username).where(users.c.password == password)
    user = await database.fetch_one(query)
    if user:
        # Извлечение роли пользователя из результата запроса
        user_role = user["role"]  # Убедитесь, что у вас есть колонка 'role' в таблице 'users'
        return {"message": "Успешная авторизация", "username": username, "role": user_role}
    else:
        raise HTTPException(status_code=400, detail="Неверные учетные данные")