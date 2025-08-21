from flask import Flask
from api.controllers.pet_controller import pet_bp
from api.controllers.booking_controller import booking_bp
from api.controllers.user_controller import user_bp
from api.controllers.medical_controller import medical_bp
from api.controllers.room_controller import room_bp

def register_routes(app: Flask):
    app.register_blueprint(pet_bp)
    app.register_blueprint(booking_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(medical_bp)
    app.register_blueprint(room_bp)