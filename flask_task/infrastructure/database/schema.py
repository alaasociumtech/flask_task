from sqlalchemy import Column, Integer, String, Table

from flask_task.infrastructure.database.connection import engine, metadata

students = Table(
    'students',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String, nullable=False),
    Column('age', Integer, nullable=False),
    Column('grade', String, nullable=False),
)

metadata.create_all(engine)
