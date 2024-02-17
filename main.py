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
