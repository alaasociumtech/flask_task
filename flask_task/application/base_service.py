from flask_task.infrastructure.repos.unit_of_work import UnitOfWork


class BaseService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow
