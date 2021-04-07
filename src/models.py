from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Modelo para la tabla [HairColorCat]
class HairColorCat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<HairColorCat %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
        }

# Modelo para la tabla [SkinColorCat]
class SkinColorCat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<SkinColorCat %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
        }

# Modelo para la tabla [EyeColorCat]
class  EyeColorCat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<EyeColorCat %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
        }

# Modelo para la tabla [ClimateCat]
class  ClimateCat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<ClimateCat %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
        }

# Modelo para la tabla [TerrainCat]
class  TerrainCat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<TerrainCat %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
        }

# Modelo para la tabla [VehicleClassCat]
class  VehicleClassCat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<VehicleClassCat %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
        }

# Modelo para la tabla [User]
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    first_surname = db.Column(db.String(100), nullable=False)
    second_surname = db.Column(db.String(100))
    user_name = db.Column(db.String(50), unique=True)
    user_image = db.Column(db.String(2000))
    email = db.Column(db.String(250), unique=True)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "first_surname": self.first_surname,
            "second_surname": self.second_surname,
            "user_name": self.user_name,
            "user_image": self.user_image,
            "email": self.email,
            "password": self.password,
            "is_active": self.is_active
        }