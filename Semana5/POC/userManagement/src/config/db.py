from os import environ as env

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

user = env.get("DB_USER", "postgres")
password = env.get("DB_PASSWORD", "postgres")
host = env.get("DB_HOST", "localhost")
port = env.get("DB_PORT", "5432")
db_name = env.get("DB_NAME", "postgres")
db_driver = env.get("DB_DRIVER", "postgresql")

db_url = f"{db_driver}://{user}:{password}@{host}:{port}/{db_name}"

engine = create_engine(db_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
