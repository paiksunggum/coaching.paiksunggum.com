from collections.abc import AsyncGenerator

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

import db


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    if db.AsyncSessionLocal is None:
        raise HTTPException(
            status_code=503,
            detail="DATABASE_URL is not set; add it to backend/.env",
        )
    async with db.AsyncSessionLocal() as session:
        yield session
