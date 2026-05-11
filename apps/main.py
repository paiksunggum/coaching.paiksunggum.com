from fastapi import FastAPI

from titanic.app.james_controller import JamesController

app = FastAPI(title="paiksunggum Main Page")

@app.get("/")
def read_root():
    return {"message": "FAST API 메인 페이지", "docs": "/docs"}

@app.get("/titanic/model/data")
def read_titanic_data():
    james_controller = JamesController()
    df = james_controller.get_data()

    return df.to_dict(orient="records")

@app.get("/titanic/model/count")
def read_titanic_count():
    james_controller = JamesController()
    df = james_controller.get_count()

    return {"count": james_controller.get_count()}

@app.get("/titanic/model/count/survived")
def read_titanic_survived():
    james_controller = JamesController()
    return {"survived": james_controller.get_survived_count()}

@app.get("/titanic/model/count/dead")
def read_titanic_dead():
    james_controller = JamesController()
    return {"dead": james_controller.get_dead_count()}

@app.get("/titanic/model/tree")
def read_has_decision_tree_model_tree():
    james_controller = JamesController()
    return {"tree": james_controller.has_decision_tree_model()}

@app.get("/titanic/model")
def read_titanic_model_name():
    james_controller = JamesController()
    return james_controller.get_model_info()



if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)