from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=False, nullable=False)
    last_name = db.Column(db.String(250), unique=False, nullable=False)
    username = db.Column(db.String(250), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=True)
    fvcharacter = db.relationship("CharactersFavorites", backref='user', lazy=True)
    fvplanet = db.relationship("PlanetsFavorites", backref='user', lazy=True)


    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "last_name": self.last_name,
            "username": self.username,
            "email": self.email
            # do not serialize the password, its a security breach
        }

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=False, nullable=False)
    rotation_period = db.Column(db.Integer, unique=False,nullable=False)
    orbital_period = db.Column(db.Integer, unique=False,nullable=False)
    diameter = db.Column(db.Integer, unique=False,nullable=False)
    gravity = db.Column(db.String(250), unique=False, nullable=False)
    population = db.Column(db.Integer, unique=False,nullable=False)
    fvplanet = db.relationship("PlanetsFavorites", backref='Planets', lazy=True) 

    def __repr__(self):
        return '<Planets %r>' % self.name 

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "diameter": self.diameter,
            "gravity": self.gravity,
            "population": self.population
            # do not serialize the password, its a security breach
        }

  
class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=False, nullable=False)
    height = db.Column(db.Integer, unique=False,nullable=False)
    mass = db.Column(db.Integer, unique=False,nullable=False)
    hair_color = db.Column(db.String(250), unique=False, nullable=False)
    skin_color = db.Column(db.String(250), unique=False, nullable=False)
    birth_year = db.Column(db.String(250), unique=False, nullable=False)
    fvcharacter = db.relationship("CharactersFavorites", backref='characters', lazy=True)

    def __repr__(self):
        return '<Characters %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "birth_year": self.birth_year,
            "fvcharacter": list(map(lambda x: x.serialize(), self.fvcharacter))
            # do not serialize the password, its a security breach
        }

 
class PlanetsFavorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    planet_id = db.Column(db.Integer, db.ForeignKey("planets.id"))

    def __repr__(self):
        return '<PlanetsFavorites %r>' % self.user_id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id
        }


class CharactersFavorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    character_id = db.Column(db.Integer, db.ForeignKey("characters.id"))

    def __repr__(self):
        return '<CharactersFavorites %r>' % self.user_id 

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id
            # do not serialize the password, its a security breach
        }
