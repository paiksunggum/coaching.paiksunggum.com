from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from titanic.app.james_controller import JamesController

app = FastAPI(title="paiksunggum Main Page")


@app.get("/")
def read_root():
    return {"message": "FAST API 메인 페이지", "docs": "/docs"}


@app.get("/titanic/data")
def read_titanic_data():
    james = JamesController()
    df = james.get_data()
    return df.to_dict(orient="records")


@app.get("/titanic/count")
def read_titanic_count():
    james = JamesController()
    return {"count": james.get_count()}


@app.get("/titanic/tree")
def read_titanic_tree():
    james = JamesController()
    return {"tree": james.has_decision_tree_model()}


@app.get("/titanic/model")
def read_titanic_model():
    controller = JamesController()
    model_name = controller.get_model_name_and_accuracy()
    return JSONResponse(content=jsonable_encoder(model_name))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
