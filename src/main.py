
import os
import json
import datetime
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, GenderCat, HairColorCat, SkinColorCat, EyeColorCat, ClimateCat, TerrainCat, VehicleClassCat, User, People, Planet, Vehicle, Favorite
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["JWT_SECRET_KEY"] = "Secr3tKeyR3sTAp1StarWars#123$456%789&"
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

jwt = JWTManager(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# INICIO - Definición de EndPoints para el Modelo [GenderCat] - INICIO
# [GET] - Ruta para obtener todos los [GenderCat]
@app.route('/api/gendercat', methods=['GET'])
@jwt_required()
def indexAllGenderCat():

    results = GenderCat.query.all()

    return jsonify(list(map(lambda x: x.serialize(), results))), 200

# [GET] - Ruta para obtener un [GenderCat]
@app.route('/api/gendercat/<int:id>', methods=['GET'])
@jwt_required()
def indexGenderCat(id):
    genderCat = GenderCat.query.get(id)

    if genderCat is None:
        raise APIException('El genero con el id especificado, no fue encontrado.',status_code=403)

    return jsonify(GenderCat.serialize(genderCat)), 200

# [POST] - Ruta para crear un [GenderCat]
@app.route('/api/gendercat', methods=['POST'])
@jwt_required()
def storeGenderCat():

    data_request = request.get_json()

    genderCat = GenderCat.query.filter_by(name=data_request["name"]).first()
    
    # Se valida que el name no haya sido registrado.
    if genderCat:
        return jsonify({"msg": "El name ya fue registrado."}), 401
    
    genderCat = GenderCat(name=data_request["name"])

    try:
        db.session.add(genderCat) 
        db.session.commit()
        
        return jsonify(GenderCat.serialize(genderCat)), 201
    
    except AssertionError as exception_message: 
        return jsonify(msg='Error: {}. '.format(exception_message)), 400

# [PUT] - Ruta para modificar un [GenderCat]
@app.route('/api/gendercat/<int:id>', methods=['PUT'])
@jwt_required()
def updateGenderCat(id):

    genderCat = GenderCat.query.get(id)

    if genderCat is None:
        raise APIException('El genero con el id especificado, no fue encontrado.',status_code=403)

    data_request = request.get_json()
    
    genderCat.name = data_request["name"]

    try: 
        db.session.commit()
        
        return jsonify(GenderCat.serialize(genderCat)), 200
    
    except AssertionError as exception_message: 
        return jsonify(msg='Error: {}. '.format(exception_message)), 400

# [DELETE] - Ruta para eliminar un [GenderCat]
@app.route('/api/gendercat/<int:id>', methods=['DELETE'])
@jwt_required()
def deleteGenderCat(id):

    genderCat = GenderCat.query.get(id)

    if genderCat is None:
        raise APIException('El genero con el id indicado, no fue encontrado.',status_code=403)

    try:
        db.session.delete(genderCat)
        db.session.commit()
        
        return jsonify('El genero fue eliminado satisfactoriamente.'), 200
    
    except AssertionError as exception_message: 
        return jsonify(msg='Error: {}. '.format(exception_message)), 400
# FIN - Definición de EndPoints para el Modelo [GenderCat] - FIN

# INICIO - Definición de EndPoints para el Modelo [HairColorCat] - INICIO
# FIN - Definición de EndPoints para el Modelo [HairColorCat] - FIN

# INICIO - Definición de EndPoints para el Modelo [SkinColorCat] - INICIO
# FIN - Definición de EndPoints para el Modelo [SkinColorCat] - FIN

# INICIO - Definición de EndPoints para el Modelo [EyeColorCat] - INICIO
# FIN - Definición de EndPoints para el Modelo [EyeColorCat] - FIN

# INICIO - Definición de EndPoints para el Modelo [ClimateCat] - INICIO
# FIN - Definición de EndPoints para el Modelo [ClimateCat] - FIN

# INICIO - Definición de EndPoints para el Modelo [TerrainCat] - INICIO
# FIN - Definición de EndPoints para el Modelo [TerrainCat] - FIN

# INICIO - Definición de EndPoints para el Modelo [VehicleClassCat] - INICIO
# FIN - Definición de EndPoints para el Modelo [VehicleClassCat] - FIN

# INICIO - Definición de EndPoints para el Modelo [User] para Login y Registro - INICIO
@app.route("/api/users/login", methods=["POST"])
def login():
    email = request.json.get("email", None)
    password = request.json.get("password", None)

    if email is None:
        return jsonify({"msg": "El email es requerido."}), 400

    if password is None:
        return jsonify({"msg": "El password es requerido."}), 400
    
    user = User.query.filter_by(email=email, password=password).first()
    
    if user is None:
        # the user was not found on the database
        return jsonify({"msg": "El email o el password son invalidos."}), 401
    else:
        expiration_date = datetime.timedelta(days=1)
        access_token = create_access_token(identity=user.id,expires_delta=expiration_date)
        return jsonify({ "token": access_token, "user_id": user.id }), 200

# [POST] - Ruta para registro de un [user]
@app.route('/api/users/register', methods=['POST'])
def register():

    data_request = request.get_json()

    user = User.query.filter_by(email=data_request["email"]).first()
    
    # Se valida que el email no haya sido registrado.
    if user:
        return jsonify({"msg": "El email ya fue registrado."}), 401
    
    user = User(email=data_request["email"], password=data_request["password"], is_active=data_request["is_active"])

    try:
        db.session.add(user) 
        db.session.commit()
        
        return jsonify(User.serialize(user)), 201
    
    except AssertionError as exception_message: 
        return jsonify(msg='Error: {}. '.format(exception_message)), 400
# FIN - Definición de EndPoints para el Modelo [User] para Login y Registro - FIN

# INICIO - Definición de EndPoints para el Modelo [User] - INICIO
# [GET] - Ruta para obtener todos los [user]
@app.route('/api/users', methods=['GET'])
@jwt_required()
def indexAllUser():

    results = User.query.all()

    return jsonify(list(map(lambda x: x.serialize(), results))), 200

# [GET] - Ruta para obtener un [user]
@app.route('/api/users/<int:id>', methods=['GET'])
@jwt_required()
def indexUser(id):
    user = User.query.get(id)

    if user is None:
        raise APIException('El usuario con el id especificado, no fue encontrado.',status_code=403)

    return jsonify(User.serialize(user)), 200

# [POST] - Ruta para crear un [user]
@app.route('/api/users', methods=['POST'])
@jwt_required()
def storeUser():

    data_request = request.get_json()

    user = User.query.filter_by(email=data_request["email"]).first()
    
    # Se valida que el email no haya sido registrado.
    if user:
        return jsonify({"msg": "El email ya fue registrado."}), 401

    user = User(name = data_request["name"],
    first_surname = data_request["first_surname"],
    second_surname = data_request["second_surname"],
    user_name = data_request["user_name"],
    user_image = data_request["user_image"],
    email = data_request["email"],
    password = data_request["password"],
    is_active = data_request["is_active"])

    try:
        db.session.add(user)
        db.session.commit()
        
        return jsonify(User.serialize(user)), 201
    
    except AssertionError as exception_message: 
        return jsonify(msg='Error: {}. '.format(exception_message)), 400

# [PUT] - Ruta para modificar un [user]
@app.route('/api/users/<int:id>', methods=['PUT'])
@jwt_required()
def updateUser(id):

    user = User.query.get(id)

    if user is None:
        raise APIException('El user con el id especificado, no fue encontrado.',status_code=403)

    data_request = request.get_json()

    user.name = data_request["name"]
    user.first_surname = data_request["first_surname"]
    user.second_surname = data_request["second_surname"]
    user.user_image = data_request["user_image"]
    user.password = data_request["password"]
    user.is_active = data_request["is_active"]

    try: 
        db.session.commit()
        
        return jsonify(User.serialize(user)), 200
    
    except AssertionError as exception_message: 
        return jsonify(msg='Error: {}. '.format(exception_message)), 400

# [DELETE] - Ruta para eliminar un [user]
@app.route('/api/users/<int:id>', methods=['DELETE'])
@jwt_required()
def deleteUser(id):

    user = User.query.get(id)

    if user is None:
        raise APIException('El usuario con el id indicado, no fue encontrado.',status_code=403)

    try:
        db.session.delete(user)
        db.session.commit()
        
        return jsonify('El usuario fue eliminado satisfactoriamente.'), 200
    
    except AssertionError as exception_message: 
        return jsonify(msg='Error: {}. '.format(exception_message)), 400
# FIN - Definición de EndPoints para el Modelo [User] - FIN

# INICIO - Definición de EndPoints para el Modelo [People] - INICIO
# [GET] - Ruta para obtener todos los [People]
@app.route('/api/peoples', methods=['GET'])
@jwt_required()
def indexAllPeople():

    results = People.query.all()

    return jsonify(list(map(lambda x: x.serialize(), results))), 200

# [GET] - Ruta para obtener un [People]
@app.route('/api/peoples/<int:id>', methods=['GET'])
@jwt_required()
def indexPeople(id):
    people = People.query.get(id)

    if people is None:
        raise APIException('La persona con el id especificado, no fue encontrado.',status_code=403)

    return jsonify(People.serialize(people)), 200

# [POST] - Ruta para crear un [People]
@app.route('/api/peoples', methods=['POST'])
@jwt_required()
def storePeople():

    data_request = request.get_json()

    if  data_request["name"] is None or data_request["name"] == '':
         raise APIException('El name es requerido.',status_code=403)
    
    people = People(name = data_request["name"],
    birth_year = data_request["birth_year"],
    height = data_request["height"],
    mass = data_request["mass"],
    people_image = data_request["people_image"],
    gender_cat_id = data_request["gender_cat_id"],
    hair_color_cat_id = data_request["hair_color_cat_id"],
    skin_color_cat_id = data_request["skin_color_cat_id"],
    eye_color_cat_id = data_request["eye_color_cat_id"])

    try: 
        db.session.add(people) 
        db.session.commit()
        
        return jsonify(People.serialize(people)), 201
    
    except AssertionError as exception_message: 
        return jsonify(msg='Error: {}. '.format(exception_message)), 400

# [PUT] - Ruta para modificar un [People]
@app.route('/api/peoples/<int:id>', methods=['PUT'])
@jwt_required()
def updatePeople(id):

    people = People.query.get(id)

    if people is None:
        raise APIException('La persona con el id especificado, no fue encontrado.',status_code=403)

    data_request = request.get_json()

    people.name = data_request["name"]
    people.birth_year = data_request["birth_year"]
    people.height = data_request["height"]
    people.mass = data_request["mass"]
    people.people_image = data_request["people_image"]
    people.gender_cat_id = data_request["gender_cat_id"]
    people.hair_color_cat_id = data_request["hair_color_cat_id"]
    people.skin_color_cat_id = data_request["skin_color_cat_id"]
    people.eye_color_cat_id = data_request["eye_color_cat_id"]

    try: 
        db.session.commit()
        
        return jsonify(People.serialize(people)), 200
    
    except AssertionError as exception_message: 
        return jsonify(msg='Error: {}. '.format(exception_message)), 400

# [DELETE] - Ruta para eliminar un [People]
@app.route('/api/peoples/<int:id>', methods=['DELETE'])
@jwt_required()
def deletePeople(id):

    people = People.query.get(id)

    if people is None:
        raise APIException('La persona con el id indicado, no fue encontrado.',status_code=403)

    try:
        db.session.delete(people)
        db.session.commit()
        
        return jsonify('La persona fue eliminada satisfactoriamente.'), 200
    
    except AssertionError as exception_message: 
        return jsonify(msg='Error: {}. '.format(exception_message)), 400
# FIN - Definición de EndPoints para el Modelo [People] - FIN


# INICIO - Definición de EndPoints para el Modelo [Planet] - INICIO
# [GET] - Ruta para obtener todos los [Planet]
@app.route('/api/planets', methods=['GET'])
@jwt_required()
def indexAllPlanet():

    results = Planet.query.all()

    return jsonify(list(map(lambda x: x.serialize(), results))), 200

# [GET] - Ruta para obtener un [Planet]
@app.route('/api/planets/<int:id>', methods=['GET'])
@jwt_required()
def indexPlanet(id):
    planet = Planet.query.get(id)

    if planet is None:
        raise APIException('El planeta con el id especificado, no fue encontrado.',status_code=403)

    return jsonify(Planet.serialize(planet)), 200

# [POST] - Ruta para crear un [Planet]
@app.route('/api/planets', methods=['POST'])
@jwt_required()
def storePlanet():

    data_request = request.get_json()

    if  data_request["name"] is None or data_request["name"] == '':
         raise APIException('El name es requerido.',status_code=403)
    
    planet = Planet(name = data_request["name"],
    rotation_period = data_request["rotation_period"],
    orbital_period = data_request["orbital_period"],
    diameter = data_request["diameter"],
    gravity = data_request["gravity"],
    surface_water = data_request["surface_water"],
    population = data_request["population"],
    planet_image = data_request["planet_image"],
    climate_cat_id = data_request["climate_cat_id"],
    terrain_cat_id = data_request["terrain_cat_id"])

    try: 
        db.session.add(planet) 
        db.session.commit()
        
        return jsonify(Planet.serialize(planet)), 201
    
    except AssertionError as exception_message: 
        return jsonify(msg='Error: {}. '.format(exception_message)), 400

# [PUT] - Ruta para modificar un [Planet]
@app.route('/api/planets/<int:id>', methods=['PUT'])
@jwt_required()
def updatePlanet(id):

    planet = Planet.query.get(id)

    if planet is None:
        raise APIException('El planeta con el id especificado, no fue encontrado.',status_code=403)

    data_request = request.get_json()

    planet.name = data_request["name"]
    planet.rotation_period = data_request["rotation_period"]
    planet.orbital_period = data_request["orbital_period"]
    planet.diameter = data_request["diameter"]
    planet.gravity = data_request["gravity"]
    planet.surface_water = data_request["surface_water"]
    planet.population = data_request["population"]
    planet.planet_image = data_request["planet_image"]
    planet.climate_cat_id = data_request["climate_cat_id"]
    planet.terrain_cat_id = data_request["terrain_cat_id"]

    try: 
        db.session.commit()
        
        return jsonify(Planet.serialize(planet)), 200
    
    except AssertionError as exception_message:
        return jsonify(msg='Error: {}. '.format(exception_message)), 400

# [DELETE] - Ruta para eliminar un [Planet]
@app.route('/api/planets/<int:id>', methods=['DELETE'])
@jwt_required()
def deletePlanet(id):

    planet = Planet.query.get(id)

    if planet is None:
        raise APIException('El planeta con el id indicado, no fue encontrado.',status_code=403)

    try:
        db.session.delete(planet)
        db.session.commit()
        
        return jsonify('El planeta fue eliminado satisfactoriamente.'), 200
    
    except AssertionError as exception_message: 
        return jsonify(msg='Error: {}. '.format(exception_message)), 400
# FIN - Definición de EndPoints para el Modelo [Planet] - FIN


# INICIO - Definición de EndPoints para el Modelo [Vehicle] - INICIO
# [GET] - Ruta para obtener todos los [Vehicle]
@app.route('/api/vehicles', methods=['GET'])
@jwt_required()
def indexAllVehicle():

    results = Vehicle.query.all()

    return jsonify(list(map(lambda x: x.serialize(), results))), 200

# [GET] - Ruta para obtener un [Vehicle]
@app.route('/api/vehicles/<int:id>', methods=['GET'])
@jwt_required()
def indexVehicle(id):
    vehicle = Vehicle.query.get(id)

    if vehicle is None:
        raise APIException('El vehículo con el id especificado, no fue encontrado.',status_code=403)

    return jsonify(Vehicle.serialize(vehicle)), 200

# [POST] - Ruta para crear un [Vehicle]
@app.route('/api/vehicles', methods=['POST'])
@jwt_required()
def storeVehicle():

    data_request = request.get_json()

    if  data_request["name"] is None or data_request["name"] == '':
         raise APIException('El name es requerido.',status_code=403)
    
    vehicle = Vehicle(name = data_request["name"],
    model = data_request["model"],
    manufacturer = data_request["manufacturer"],
    cost_in_credits = data_request["cost_in_credits"],
    length = data_request["length"],
    max_atmosphering_speed = data_request["max_atmosphering_speed"],
    crew = data_request["crew"],
    passengers = data_request["passengers"],
    cargo_capacity = data_request["cargo_capacity"],
    consumables = data_request["consumables"],
    vehicle_image = data_request["vehicle_image"],
    vehicle_class_cat_id = data_request["vehicle_class_cat_id"])

    try: 
        db.session.add(vehicle) 
        db.session.commit()
        
        return jsonify(Vehicle.serialize(vehicle)), 201
    
    except AssertionError as exception_message: 
        return jsonify(msg='Error: {}. '.format(exception_message)), 400

# [PUT] - Ruta para modificar un [Vehicle]
@app.route('/api/vehicles/<int:id>', methods=['PUT'])
@jwt_required()
def updateVehicle(id):

    vehicle = Vehicle.query.get(id)

    if vehicle is None:
        raise APIException('El vehículo con el id especificado, no fue encontrado.',status_code=403)

    data_request = request.get_json()

    vehicle.name = data_request["name"]
    vehicle.model = data_request["model"]
    vehicle.manufacturer = data_request["manufacturer"]
    vehicle.cost_in_credits = data_request["cost_in_credits"]
    vehicle.length = data_request["length"]
    vehicle.max_atmosphering_speed = data_request["max_atmosphering_speed"]
    vehicle.crew = data_request["crew"]
    vehicle.passengers = data_request["passengers"]
    vehicle.cargo_capacity = data_request["cargo_capacity"]
    vehicle.consumables = data_request["consumables"]
    vehicle.vehicle_image = data_request["vehicle_image"]
    vehicle.vehicle_class_cat_id = data_request["vehicle_class_cat_id"]

    try: 
        db.session.commit()
        
        return jsonify(Vehicle.serialize(vehicle)), 200
    
    except AssertionError as exception_message:
        return jsonify(msg='Error: {}. '.format(exception_message)), 400

# [DELETE] - Ruta para eliminar un [Vehicle]
@app.route('/api/vehicles/<int:id>', methods=['DELETE'])
@jwt_required()
def deleteVehicle(id):

    vehicle = Vehicle.query.get(id)

    if vehicle is None:
        raise APIException('El vehiculo con el id especificado, no fue encontrado.',status_code=403)

    try:
        db.session.delete(vehicle)
        db.session.commit()
        
        return jsonify('El vehiculo fue eliminado satisfactoriamente.'), 200
    
    except AssertionError as exception_message: 
        return jsonify(msg='Error: {}. '.format(exception_message)), 400
# FIN - Definición de EndPoints para el Modelo [Vehicle] - FIN


# INICIO - Definición de EndPoints para el Modelo [Favorite] - INICIO
# [GET] - Ruta para obtener todos los [Favorite]
@app.route('/api/favorites', methods=['GET'])
@jwt_required()
def indexAllFavorite():

    results = Favorite.query.all()

    return jsonify(list(map(lambda x: x.serialize(), results))), 200

# [POST] - Ruta para crear un [Favorite]
@app.route('/api/favorites', methods=['POST'])
@jwt_required()
def storeFavorite():

    data_request = request.get_json()

    if  data_request["user_id"] is None or data_request["user_id"] == '':
         raise APIException('El user_id es requerido.',status_code=403)
    
    if  data_request["favorite_id"] is None or data_request["favorite_id"] == '':
         raise APIException('El favorite_id es requerido.',status_code=403)
    
    if  data_request["favorite_type"] is None or data_request["favorite_type"] == '':
         raise APIException('El favorite_type es requerido.',status_code=403)
    
    favorite = Favorite(user_id = data_request["user_id"],
    favorite_id = data_request["favorite_id"],
    favorite_type = data_request["favorite_type"])

    try: 
        db.session.add(favorite) 
        db.session.commit()
        
        return jsonify(Favorite.serialize(favorite)), 201
    
    except AssertionError as exception_message: 
        return jsonify(msg='Error: {}. '.format(exception_message)), 400

# [DELETE] - Ruta para eliminar un [Favorite]
@app.route('/api/favorites/<int:id>', methods=['DELETE'])
@jwt_required()
def deleteFavorite(id):

    favorite = Favorite.query.get(id)

    if favorite is None:
        raise APIException('El favorito con el id especificado, no fue encontrado.',status_code=403)

    try:
        db.session.delete(favorite)
        db.session.commit()
        
        return jsonify('El favorito fue eliminado satisfactoriamente.'), 200
    
    except AssertionError as exception_message: 
        return jsonify(msg='Error: {}. '.format(exception_message)), 400
# FIN - Definición de EndPoints para el Modelo [Favorite] - FIN

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
