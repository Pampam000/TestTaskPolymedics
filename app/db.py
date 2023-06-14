import asyncpg

from .config import POSTGRES_DB, POSTGRES_PORT, POSTGRES_PASSWORD, \
    POSTGRES_USER, POSTGRES_HOST


async def get_connection():
    conn: asyncpg.Connection = await asyncpg.connect(
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        host=POSTGRES_HOST,
        database=POSTGRES_DB,
        port=POSTGRES_PORT)

    try:
        yield conn
    finally:
        await conn.close()
