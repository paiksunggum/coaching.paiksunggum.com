from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession


class DbCheckAdapter:
    """DB 연결·쿼리 결과를 HTTP와 무관한 dict로 만든다."""

    @staticmethod
    async def neon_now(session: AsyncSession) -> dict:
        try:
            result = await session.execute(text("SELECT NOW();"))
            now = result.scalar()
            return {"status": "success", "neon_time": str(now) if now is not None else None}
        except Exception as e:
            return {"status": "error", "message": str(e)}
