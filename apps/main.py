from fastapi import FastAPI

try:
    from titanic.app.james import James
except ModuleNotFoundError:
    from titanic.app.james import James

app = FastAPI(title="paiksunggum Main Page")

@app.get("/")
def root():
    return {"message": "FAST API 메인 페이지"}

@app.get("/data")
def read_titanic_data():
    james = James()
    df = james.get_data()

    return df.to_dict(orient="records")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)