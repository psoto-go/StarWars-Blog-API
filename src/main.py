"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Characters, Planets, Favorites
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():
    req = User.query.all()
    response = []
    # for x in req:
    #     response.append(x.serialize())
    return jsonify({"response" : list(map(lambda x:x.serialize(), req))}), 200

@app.route('/user', methods=['POST'])
def handle_hello1():
    body_request = request.get_json()

    name = body_request.get("name", None)
    last_name = body_request.get("last_name", None)
    username = body_request.get("username", None)
    email= body_request.get("email", None)
    password= body_request.get("password", None)
    # fvcharacter = body_request.get("fvcharacter", None)
    # fvplanet = body_request.get("fvplanet", None)

    user1 = User(name=name, last_name=last_name, username=username, email = email, password=password)
    db.session.add(user1)
    db.session.commit()


    return jsonify({"msg":  "Usuario creado exitosamente"}), 200


@app.route('/people', methods=['POST'])
def people():
    body_request = request.get_json()

    name = body_request.get("name", None)
    height = body_request.get("height", None)
    mass = body_request.get("mass", None)
    hair_color= body_request.get("hair_color", None)
    skin_color= body_request.get("skin_color", None)
    birth_year= body_request.get("birth_year", None)


    Newcha = Characters(name=name, height=height, mass=mass, hair_color = hair_color, skin_color=skin_color, birth_year=birth_year)
    db.session.add(Newcha)
    db.session.commit()


    return jsonify({"msg":  "Character creado exitosamente"}), 200

@app.route('/people', methods=['GET'])
def peolpeget():
    req = Characters.query.all()
    response = []
    # for x in req:
    #     response.append(x.serialize())
    return jsonify({"response" : list(map(lambda x:x.serialize(), req))}), 200

@app.route('/people/<int:people_id>', methods=['GET'])
def peopleid(people_id):
    body = request.get_json()
    cha = Characters.query.get(people_id)
    return jsonify(cha.serialize()), 200

@app.route('/planets', methods=['POST'])
def planets():
    body_request = request.get_json()

    name = body_request.get("name", None)
    rotation_period = body_request.get("rotation_period", None)
    orbital_period = body_request.get("orbital_period", None)
    diameter= body_request.get("diameter", None)
    gravity= body_request.get("gravity", None)
    population= body_request.get("population", None)


    Newpla = Planets(name=name, rotation_period=rotation_period, orbital_period=orbital_period, diameter = diameter, gravity=gravity, population=population)
    db.session.add(Newpla)
    db.session.commit()


    return jsonify({"msg":  "Character creado exitosamente"}), 200

@app.route('/planets', methods=['GET'])
def plaget():
    req = Planets.query.all()
    response = []
    # for x in req:
    #     response.append(x.serialize())
    return jsonify({"response" : list(map(lambda x:x.serialize(), req))}), 200

@app.route('/planets/<int:planets_id>', methods=['GET'])
def planetsid(planets_id):
    body = request.get_json()
    cha = Planets.query.get(planets_id)
    return jsonify(cha.serialize()), 200

@app.route('/user/favorites', methods=['POST'])
def favuser():
    body_request = request.get_json()

    user_id = body_request.get("user_id", None)
    planet_id = body_request.get("planet_id", None)
    character_id = body_request.get("character_id", None)
    #if ... is not None

    Newfav = Favorites(user_id=user_id, planet_id=planet_id, character_id=character_id)
    db.session.add(Newfav)
    db.session.commit()


    return jsonify({"msg":  "Character creado exitosamente"}), 200

@app.route('/user/favorites', methods=['GET'])
def favgetuser():
    req = Favorites.query.all()
    response = []
    # for x in req:
    #     response.append(x.serialize())
    return jsonify({"response" : list(map(lambda x:x.serialize(), req))}), 200


@app.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def favplaid(planet_id):
    body_request = request.get_json()
    planet_id = body_request.get("planet_id", None)
    name = body_request.get("name", None)
    rotation_period = body_request.get("rotation_period", None)
    orbital_period = body_request.get("orbital_period", None)
    diameter= body_request.get("diameter", None)
    gravity= body_request.get("gravity", None)
    population= body_request.get("population", None)


    Newpla = Planets(name=name, rotation_period=rotation_period, orbital_period=orbital_period, diameter = diameter, gravity=gravity, population=population)
    db.session.add(Newpla)
    db.session.commit()


    return jsonify({"msg":  "Planet creado exitosamente"}), 200

@app.route('/favorite/people/<int:people_id>', methods=['POST'])
def favpeople(people_id):
    body_request = request.get_json()
    people_id = body_request.get("people_id", None)
    name = body_request.get("name", None)
    height = body_request.get("height", None)
    mass = body_request.get("mass", None)
    hair_color= body_request.get("hair_color", None)
    skin_color= body_request.get("skin_color", None)
    birth_year= body_request.get("birth_year", None)


    Newcha = Characters(name=name, height=height, mass=mass, hair_color = hair_color, skin_color=skin_color, birth_year=birth_year)
    db.session.add(Newcha)
    db.session.commit()


    return jsonify({"msg":  "Character creado exitosamente"}), 200

@app.route('/favorite/planet/<int:planet_id>', methods=['GET'])
def planetsidfav(planet_id):
    body = request.get_json()
    cha = Planets.query.get(planet_id)
    return jsonify(cha.serialize()), 200

@app.route('/favorite/people/<int:people_id>', methods=['GET'])
def peoplesidfav(people_id):
    body = request.get_json()
    cha = Characters.query.get(people_id)
    return jsonify(cha.serialize()), 200

@app.route('/favorite/people/<int:people_id>', methods=['DELETE'])
def peoplesidfavdelete(people_id):
    people = Favorites.query.get(character_id)
    print(character_id)
    db.session.delete(people)
    db.session.commit()
    return jsonify(people.serialize()), 200


# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
