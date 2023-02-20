import logging
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

# 데이터 베이스와 관련된 설정하는 파일

logging.basicConfig()
# DB URL 주소
db = {
    'user': 'ajunsoft',
    'password': 'dla39275566!',
    'host': 'localhost',
    'port': 3306,
    'database': 'stockdvidend'
}
"""
비동기 DB 설치
$ pip install 'sqlalchemy[asyncio]'
$ pip install aiomysql
"""
DB_URL = f"mysql+aiomysql://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=UTF8MB4"

# create_engine -> 동기
# create_async_engine -> 비동기
# 컨넥션 풀을 생성
async_engine = create_async_engine(
    DB_URL, case_sensitive=False, convert_unicode=True
)

sync_engine = create_engine(
    DB_URL, case_sensitive=False, convert_unicode=True
)

# Query Debugging Level
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)  # 실행 쿼리
# logging.getLogger('sqlalchemy.engine').setLevel(logging.DEBUG) # 조회 결과
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=sync_engine)

Base = declarative_base()  # 상속 클래스들을 자동으로 매핑
naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
# 이름 지정 규칙 세팅
Base.metadata = MetaData(naming_convention=naming_convention)


# 동기 전용
def get_db():
    db = SessionLocal()  # db = SessionLocal()  DB 세션 생성
    try:
        yield db  # 제너레이터 반환
    finally:
        db.close()  # 사용한 세션을 컨넥션 풀에 반환(종료 아님)


# 비동기 전용
async def get_async_db():
    db = AsyncSession(bind=async_engine, expire_on_commit=False)
    try:
        yield db
    finally:
        await db.close()
