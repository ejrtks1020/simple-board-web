from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from starlette.responses import JSONResponse
from contextlib import asynccontextmanager
from icecream import ic
import uvicorn
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ic(BASE_DIR)
STATIC_DIR = BASE_DIR / "static"
@asynccontextmanager
async def lifespan(app: FastAPI):
    ic("start")

    yield

    ic("end")

app = FastAPI(lifespan=lifespan)

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

@app.get("/")
def get_board():
    with open(STATIC_DIR / "index.html", "r", encoding="utf-8") as file:
      html_content = file.read()
    return HTMLResponse(content=html_content)

if __name__ == "__main__":
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)
