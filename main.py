from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

# 전체적인 환경을 설정하는 파일

app = FastAPI()

origins = [
    "http://127.0.0.1:5173",  # 또는 "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




