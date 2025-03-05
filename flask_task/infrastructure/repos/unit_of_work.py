from sqlalchemy.orm import sessionmaker

from flask_task.infrastructure.database.connection import engine

SessionLocal = sessionmaker(bind=engine)


class UnitOfWork:
    def __init__(self) -> None:
        self.session = SessionLocal()

    def commit(self) -> None:
        self.session.commit()

    def rollback(self) -> None:
        self.session.rollback()

    def close(self) -> None:
        self.session.close()
