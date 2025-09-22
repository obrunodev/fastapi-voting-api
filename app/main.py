from fastapi import FastAPI
from contextlib import asynccontextmanager

from .database import engine
from .models import Base
from .routers.users import router as users_routers


async def create_db_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Iniciando a aplicação e criando as tabelas do banco de dados...")
    await create_db_tables()
    print("Tabelas criadas com sucesso.")
    yield
    print("Desligando a aplicação.")


app = FastAPI(lifespan=lifespan)

app.include_router(users_routers)
