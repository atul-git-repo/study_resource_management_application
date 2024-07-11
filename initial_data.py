from main import app
from application.models import db, Role

with app.app_context():
    db.create_all()

    admin = Role(id="admin", name="Atul", description="software engineer")
    db.session.add(admin)
    student = Role(id="student", name="umesh", description="M.Sc Mathematics")
    db.session.add(student)
    instructor = Role(id = "inst", name="Avinash", description="Machine Learning")
    db.session.add(instructor)

    # db.session.add_all([admin, student, instructor])

    try:
        db.session.commit()
    except:
        pass