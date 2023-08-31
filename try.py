
from models import session, Student, Subject, Grade, Group, Teacher


student = session.query(Student).get(92)
print(student.id, student.student_name)
