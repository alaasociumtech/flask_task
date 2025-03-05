from sqlalchemy import MetaData, create_engine

DATABASE_URL = "postgresql://postgres:mysecretpassword@localhost:5432/mydatabase"

engine = create_engine(DATABASE_URL)
metadata = MetaData()
