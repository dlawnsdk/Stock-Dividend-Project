import logging
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
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

DB_URL = f"mysql://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"

# 컨넥션 풀을 생성
engine = create_engine(
    DB_URL, connect_args={'check_same_thread': False}
)

# Querry Debugging Level
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO) # 실행 쿼리
# logging.getLogger('sqlalchemy.engine').setLevel(logging.DEBUG) # 조회 결과
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base() # 상속클래스들을 자동으로 매핑
naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
# 이름 지정규칙 세팅
Base.metadata = MetaData(naming_convention=naming_convention)

#  db 정류
# @contextlib.contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db # 제너레이터를 반환
    finally:
        db.close()
