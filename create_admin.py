from app import app, db
from app.models import User
from werkzeug.security import generate_password_hash

# Crear una aplicación de contexto para ejecutar comandos directamente con Flask
with app.app_context():
    # Revisar si el usuario admin ya existe
    admin = User.query.filter_by(username='admin').first()
    if admin:
        print("El usuario administrador ya existe.")
    else:
        # Crear el usuario administrador
        admin = User(
            username='admin',
            email='admin@example.com',
            password_hash=generate_password_hash('adminpassword', method='pbkdf2:sha256'),
            role='admin'  # Asignando el rol de 'admin'
        )
        db.session.add(admin)
        db.session.commit()
        print(f"Admin user {admin.username} created with ID {admin.id}")

