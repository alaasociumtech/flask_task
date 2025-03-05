from typing import Any

from flask import jsonify, request
from flask.views import MethodView

from flask_task.application.student_service import StudentService
from flask_task.infrastructure.repos.unit_of_work import UnitOfWork


class StudentAPI(MethodView):
    def __init__(self) -> None:
        self.uow = UnitOfWork()
        self.student_service = StudentService(self.uow)

    def get(self, student_id: int | None = None) -> Any:
        if student_id is None:
            students = self.student_service.student_repo.get_all()
            return jsonify([student.to_dict() for student in students])

        student = self.student_service.get_student(student_id)
        if not student:
            return jsonify({'error': 'Student not found'}), 404

        return jsonify(student.to_dict())

    def post(self) -> Any:
        data = request.get_json()
        if not all(k in data for k in ('name', 'age', 'grade')):
            return jsonify({'error': 'Missing required fields'}), 400

        student = self.student_service.add_student(data['name'], data['age'], data['grade'])
        return jsonify(student.to_dict())

    def put(self, student_id: int) -> Any:
        data = request.get_json()
        updated_student = self.student_service.update_student(
            student_id, data.get('name'), data.get('age'), data.get('grade')
        )
        if not updated_student:
            return jsonify({'error': 'Student not found'}), 404

        return jsonify(updated_student.to_dict())

    def delete(self, student_id: int) -> Any:
        deleted_student = self.student_service.delete_student(student_id)
        if not deleted_student:
            return jsonify({'error': 'Student not found'}), 404

        return jsonify({'message': 'Student deleted', 'deleted_student': deleted_student.to_dict()})
