from db.base_class import Base
from db.session import engine


async def create_tables():
    Base.metadata.create_all(bind=engine)


async def init_db() -> None:
    await create_tables()
