from asyncpg import Connection, Record


async def get_teachers(conn: Connection) -> list[Record]:
    return await conn.fetch('SELECT * FROM teacher ORDER BY id')
