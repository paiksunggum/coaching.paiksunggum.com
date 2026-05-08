from fastapi import FastAPI

from titanic.app.james import James

app = FastAPI(title="paiksunggum Main Page")

@app.get("/")
def read_root():
    return {"message": "FAST API 메인 페이지", "docs": "/docs"}

@app.get("/titanic/data")
def read_titanic_data():
    james = James()
    df = james.get_data()

    return df.to_dict(orient="records")

@app.get("/titanic/count")
def read_titanic_count():
    james = James()
    df = james.get_count()

    return {"count": james.get_count()}

@app.get("/titanic/count/survived")
def read_titanic_survived():
    james = James()
    return {"survived": james.get_survived_count()}

@app.get("/titanic/count/dead")
def read_titanic_dead():
    james = James()
    return {"dead": james.get_dead_count()}

@app.get("/titanic/tree")
def read_titanic_tree():
    james = James()
    
    return {"tree": james.get_tree()}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
