from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import DB_HOST, DB_USER, DB_NAME, DB_PASS

# SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
# SQLALCHEMY_DATABASE_URL = "mysql+mysqldb://u:p@host/inovacao"
# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:password@127.0.0.1/ain_php"
SQLALCHEMY_DATABASE_URL = f"mysql+mysqldb://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# engine = create_engine("mysql+pymysql://root:whatever@localhost:3307/mydb")
# connection = engine.raw_connection()
# cursor = connection.cursor(pymysql.cursors.DictCursor)

# DB Section
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()