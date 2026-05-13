from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from . import config

engine = None
AsyncSessionLocal = None

if config.database_url:
    engine = create_async_engine(config.database_url, echo=False)
    AsyncSessionLocal = async_sessionmaker(
        engine,
        class_=AsyncSession,
        expire_on_commit=False,
        autoflush=False,
    )


async def dispose_engine() -> None:
    if engine is not None:
        await engine.dispose()
