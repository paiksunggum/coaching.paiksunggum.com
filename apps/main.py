from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from sqlalchemy.ext.asyncio import AsyncSession

from .database import get_db
from .db_check_adapter import DbCheckAdapter
from .titanic.app.james_controller import JamesController


app = FastAPI(title="TJ Watson Main Page")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "FAST API 메인 페이지 ", "docs": "/docs"}


@app.get("/db-check")
async def check_db(db: AsyncSession = Depends(get_db)):
    return await DbCheckAdapter.neon_now(db)


@app.get("/titanic/data")
def read_titanic_data():
    james = JamesController()
    df = james.get_data()

    return df.to_dict(orient="records")

@app.get("/titanic/count")
def read_titanic_count():
    james = JamesController()
    count = james.get_count()

    return {"count": count}

@app.get("/titanic/tree")
def read_titanic_tree():
    james = JamesController()
    tree = james.has_decision_tree_model()

    return {"tree": tree}


@app.get("/titanic/model")
def read_titanic_model():
    controller = JamesController()
    return controller.get_model_name_and_accuracy()



if __name__ == "__main__":
    import uvicorn

    uvicorn.run("apps.main:app", host="127.0.0.1", port=8000, reload=True)
