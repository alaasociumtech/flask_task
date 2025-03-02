from typing import Any

from flask import jsonify, request
from flask.views import MethodView

from flask_task.infrastructure.student_repo import StudentRepo


class StudentAPI(MethodView):
    student_repo = StudentRepo()

    def get(self, student_id: int | None = None) -> Any:
        if student_id is None:
            students = self.student_repo.get_all()
            return jsonify([student.to_dict() for student in students])

        student = self.student_repo.get_entity_by_id(student_id)
        if not student:
            return jsonify({'error': 'Student not found'}), 404

        return jsonify(student.to_dict())

    def post(self) -> Any:
        data = request.get_json()
        if not all(k in data for k in ('name', 'age', 'grade')):
            return jsonify({'error': 'Missing required fields'}), 400

        student = self.student_repo.add_student(
            data['name'], data['age'], data['grade'])
        return jsonify(student.to_dict())

    def put(self, student_id: int) -> Any:
        student = self.student_repo.get_entity_by_id(student_id)
        if not student_id:
            return jsonify({'error': 'Student not found'}), 404

        data = request.get_json()
        student.name = data.get('name', student.name)
        student.age = data.get('age', student.age)
        student.grade = data.get('grade', student.grade)

        updated_student = self.student_repo.update(student_id, student)
        return jsonify(updated_student.to_dict())

    def delete(self, student_id: int) -> Any:
        deleted_student = self.student_repo.delete(student_id)
        if not student_id:
            return jsonify({'error': 'Student not found'}), 404

        return jsonify({'message': 'Student deleted',
                        'deleted_student': deleted_student.to_dict()})
