from flask import jsonify, request
from flask.views import MethodView
from infrastructure.student_repo import StudentRepo

student_repo = StudentRepo()


class StudentAPI(MethodView):
    def get(self, student_id=None):
        if student_id is None:
            students = student_repo.get_all()
            return jsonify([student.to_dict() for student in students])

        student = student_repo.get_entity_by_id(student_id)
        if not student:
            return jsonify({'error: Student not found'}), 404

        return jsonify(student.to_dict())

    def post(self):
        data = request.get_json()
        if not all(k in data for k in ('name', 'age', 'grade')):
            return jsonify({'error': 'Missing required fields'}), 400

        student = student_repo.add_student(
            data['name'], data['age'], data['grade'])
        return jsonify(student.to_dict())

    def put(self, student_id):
        student = student_repo.get_entity_by_id(student_id)
        if not student_id:
            return jsonify({'error: Student not found'}), 404

        data = request.get_json()
        student.name = data.get('name', student.name)
        student.age = data.get('age', student.age)
        student.grade = data.get('grade', student.grade)

        updated_student = student_repo.update(student_id, student)
        return jsonify(updated_student.to_dict())

    def delete(self, student_id):
        deleted_student = student_repo.delete(student_id)
        if not student_id:
            return jsonify({'error: Student not found'}), 404

        return jsonify({'message': 'Student deleted',
                        'deleted_student': deleted_student.to_dict()})
