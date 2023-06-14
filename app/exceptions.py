from fastapi import HTTPException


class Base404(HTTPException):
    key: str = None
    tablename: str = None

    def __init__(self, instance_id: int):
        super().__init__(
            status_code=404,
            detail=f'Key ({self.key})=({instance_id}) is not presented in '
                   f'table \'{self.tablename}\'')