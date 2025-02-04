from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from config import settings


async_engine = create_async_engine(str(settings.DATABASE_URL), echo=True)
async_session_maker = async_sessionmaker(async_engine, expire_on_commit=False)


async def get_async_session():
    async with async_session_maker() as session:
        yield session
