from asyncpg import Connection
from fastapi import APIRouter, Depends

from app import db
from . import crud
from .schemas import TeacherId

router = APIRouter(prefix='/teachers', tags=['Teachers'])


@router.get('/', response_model=list[TeacherId])
async def get_teachers(conn: Connection = Depends(db.get_connection)
                       ) -> list[TeacherId]:
    return await crud.get_teachers(conn=conn)
