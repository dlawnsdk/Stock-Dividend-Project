from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from domain.board import board_router
from domain.stock import stock_router
from domain.member import login_router

from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles

# 전체적인 환경을 설정하는 파일

app = FastAPI()

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(board_router.router)
app.include_router(stock_router.router)
app.include_router(login_router.router)

"""
frontend build 후 dist 등록
"""
app.mount("/assets", StaticFiles(directory="frontend/dist/assets"))


@app.get("/")
def index():
    return FileResponse("frontend/dist/index.html")

