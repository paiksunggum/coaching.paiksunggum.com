from fastapi import FastAPI

from doro.app.doroj import Doroj

app = FastAPI(title="paiksunggum Main Page")

@app.get("/")
def read_root():
    return {"message": "FAST API 메인 페이지", "docs": "/docs"}

@app.get("/doro/data")
def read_doro_data():
    doroj = Doroj()
    df = doroj.get_data()

    return df.to_dict(orient="records")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)