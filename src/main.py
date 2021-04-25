
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

@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

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
        raise APIException('El genero con el id especificado, no fue encontrado.',status_code=403)

    try:
        db.session.delete(genderCat)
        db.session.commit()
        
        return jsonify('El genero fue eliminado satisfactoriamente.'), 200
    
    except AssertionError as exception_message: 
        return jsonify(msg='Error: {}. '.format(exception_message)), 400
# FIN - Definición de EndPoints para el Modelo [GenderCat] - FIN


# INICIO - Definición de EndPoints para el Modelo [HairColorCat] - INICIO
# [GET] - Ruta para obtener todos los [HairColorCat]
@app.route('/api/haircolorcat', methods=['GET'])
@jwt_required()
def indexAllHairColorCat():

    results = HairColorCat.query.all()

    return jsonify(list(map(lambda x: x.serialize(), results))), 200

# [GET] - Ruta para obtener un [HairColorCat]
@app.route('/api/haircolorcat/<int:id>', methods=['GET'])
@jwt_required()
def indexHairColorCat(id):
    hairColorCat = HairColorCat.query.get(id)

    if hairColorCat is None:
        raise APIException('El color de cabello con el id especificado, no fue encontrado.',status_code=403)

    return jsonify(HairColorCat.serialize(hairColorCat)), 200

# [POST] - Ruta para crear un [HairColorCat]
@app.route('/api/haircolorcat', methods=['POST'])
@jwt_required()
def storeHairColorCat():

    data_request = request.get_json()

    hairColorCat = HairColorCat.query.filter_by(name=data_request["name"]).first()
    
    # Se valida que el name no haya sido registrado.
    if hairColorCat:
        return jsonify({"msg": "El name ya fue registrado."}), 401
    
    hairColorCat = HairColorCat(name=data_request["name"])

    try:
        db.session.add(hairColorCat) 
        db.session.commit()
        
        return jsonify(HairColorCat.serialize(hairColorCat)), 201
    
    except AssertionError as exception_message: 
        return jsonify(msg='Error: {}. '.format(exception_message)), 400

# [PUT] - Ruta para modificar un [HairColorCat]
@app.route('/api/haircolorcat/<int:id>', methods=['PUT'])
@jwt_required()
def updateHairColorCat(id):

    haircolorcat = HairColorCat.query.get(id)

    if haircolorcat is None:
        raise APIException('El color de cabello con el id especificado, no fue encontrado.',status_code=403)

    data_request = request.get_json()
    
    haircolorcat.name = data_request["name"]

    try: 
        db.session.commit()
        
        return jsonify(HairColorCat.serialize(haircolorcat)), 200
    
    except AssertionError as exception_message: 
        return jsonify(msg='Error: {}. '.format(exception_message)), 400

# [DELETE] - Ruta para eliminar un [HairColorCat]
@app.route('/api/haircolorcat/<int:id>', methods=['DELETE'])
@jwt_required()
def deleteHairColorCat(id):

    hairColorCat = HairColorCat.query.get(id)

    if hairColorCat is None:
        raise APIException('El color de cabello con el id especificado, no fue encontrado.',status_code=403)

    try:
        db.session.delete(hairColorCat)
        db.session.commit()
        
        return jsonify('El color de cabello fue eliminado satisfactoriamente.'), 200
    
    except AssertionError as exception_message: 
        return jsonify(msg='Error: {}. '.format(exception_message)), 400
# FIN - Definición de EndPoints para el Modelo [HairColorCat] - FIN


# INICIO - Definición de EndPoints para el Modelo [SkinColorCat] - INICIO
@app.route('/api/skincolorcat', methods=['GET'])
@jwt_required()
def indexAllSkinColorCat():

    results = SkinColorCat.query.all()

    return jsonify(list(map(lambda x: x.serialize(), results))), 200

# [GET] - Ruta para obtener un [SkinColorCat]
@app.route('/api/skincolorcat/<int:id>', methods=['GET'])
@jwt_required()
def indexSkinColorCat(id):
    skinColorCat = SkinColorCat.query.get(id)

    if skinColorCat is None:
        raise APIException('El color de piel con el id especificado, no fue encontrado.',status_code=403)

    return jsonify(SkinColorCat.serialize(skinColorCat)), 200

# [POST] - Ruta para crear un [SkinColorCat]
@app.route('/api/skincolorcat', methods=['POST'])
@jwt_required()
def storeSkinColorCat():

    data_request = request.get_json()

    skinColorCat = SkinColorCat.query.filter_by(name=data_request["name"]).first()
    
    # Se valida que el name no haya sido registrado.
    if skinColorCat:
        return jsonify({"msg": "El name ya fue registrado."}), 401
    
    skinColorCat = SkinColorCat(name=data_request["name"])

    try:
        db.session.add(skinColorCat) 
        db.session.commit()
        
        return jsonify(SkinColorCat.serialize(skinColorCat)), 201
    
    except AssertionError as exception_message: 
        return jsonify(msg='Error: {}. '.format(exception_message)), 400

# [PUT] - Ruta para modificar un [SkinColorCat]
@app.route('/api/skincolorcat/<int:id>', methods=['PUT'])
@jwt_required()
def updateSkinColorCat(id):

    skincolorcat = SkinColorCat.query.get(id)

    if skincolorcat is None:
        raise APIException('El color de piel con el id especificado, no fue encontrado.',status_code=403)

    data_request = request.get_json()
    
    skincolorcat.name = data_request["name"]

    try: 
        db.session.commit()
        
        return jsonify(SkinColorCat.serialize(skincolorcat)), 200
    
    except AssertionError as exception_message: 
        return jsonify(msg='Error: {}. '.format(exception_message)), 400

# [DELETE] - Ruta para eliminar un [SkinColorCat]
@app.route('/api/skincolorcat/<int:id>', methods=['DELETE'])
@jwt_required()
def deleteSkinColorCat(id):

    skinColorCat = SkinColorCat.query.get(id)

    if skinColorCat is None:
        raise APIException('El color de piel con el id especificado, no fue encontrado.',status_code=403)

    try:
        db.session.delete(skinColorCat)
        db.session.commit()
        
        return jsonify('El color de piel fue eliminado satisfactoriamente.'), 200
    
    except AssertionError as exception_message: 
        return jsonify(msg='Error: {}. '.format(exception_message)), 400
# FIN - Definición de EndPoints para el Modelo [SkinColorCat] - FIN


# INICIO - Definición de EndPoints para el Modelo [EyeColorCat] - INICIO
@app.route('/api/eyecolorcat', methods=['GET'])
@jwt_required()
def indexAllEyeColorCat():

    results = EyeColorCat.query.all()

    return jsonify(list(map(lambda x: x.serialize(), results))), 200

# [GET] - Ruta para obtener un [EyeColorCat]
@app.route('/api/eyecolorcat/<int:id>', methods=['GET'])
@jwt_required()
def indexEyeColorCat(id):
    eyeColorCat = EyeColorCat.query.get(id)

    if eyeColorCat is None:
        raise APIException('El color de ojos con el id especificado, no fue encontrado.',status_code=403)

    return jsonify(EyeColorCat.serialize(eyeColorCat)), 200

# [POST] - Ruta para crear un [EyeColorCat]
@app.route('/api/eyecolorcat', methods=['POST'])
@jwt_required()
def storeEyeColorCat():

    data_request = request.get_json()

    eyeColorCat = EyeColorCat.query.filter_by(name=data_request["name"]).first()
    
    # Se valida que el name no haya sido registrado.
    if eyeColorCat:
        return jsonify({"msg": "El name ya fue registrado."}), 401
    
    eyeColorCat = EyeColorCat(name=data_request["name"])

    try:
        db.session.add(eyeColorCat) 
        db.session.commit()
        
        return jsonify(EyeColorCat.serialize(eyeColorCat)), 201
    
    except AssertionError as exception_message: 
        return jsonify(msg='Error: {}. '.format(exception_message)), 400

# [PUT] - Ruta para modificar un [EyeColorCat]
@app.route('/api/eyecolorcat/<int:id>', methods=['PUT'])
@jwt_required()
def updateEyeColorCat(id):

    eyecolorcat = EyeColorCat.query.get(id)

    if eyecolorcat is None:
        raise APIException('El color de ojos con el id especificado, no fue encontrado.',status_code=403)

    data_request = request.get_json()
    
    eyecolorcat.name = data_request["name"]

    try: 
        db.session.commit()
        
        return jsonify(EyeColorCat.serialize(eyecolorcat)), 200
    
    except AssertionError as exception_message: 
        return jsonify(msg='Error: {}. '.format(exception_message)), 400

# [DELETE] - Ruta para eliminar un [EyeColorCat]
@app.route('/api/eyecolorcat/<int:id>', methods=['DELETE'])
@jwt_required()
def deleteEyeColorCat(id):

    eyeColorCat = EyeColorCat.query.get(id)

    if eyeColorCat is None:
        raise APIException('El color de ojos con el id especificado, no fue encontrado.',status_code=403)

    try:
        db.session.delete(eyeColorCat)
        db.session.commit()
        
        return jsonify('El color de ojos fue eliminado satisfactoriamente.'), 200
    
    except AssertionError as exception_message: 
        return jsonify(msg='Error: {}. '.format(exception_message)), 400
# FIN - Definición de EndPoints para el Modelo [EyeColorCat] - FIN

# INICIO - Definición de EndPoints para el Modelo [ClimateCat] - INICIO
@app.route('/api/climatecat', methods=['GET'])
@jwt_required()
def indexAllClimateCat():

    results = ClimateCat.query.all()

    return jsonify(list(map(lambda x: x.serialize(), results))), 200

# [GET] - Ruta para obtener un [ClimateCat]
@app.route('/api/climatecat/<int:id>', methods=['GET'])
@jwt_required()
def indexClimateCat(id):
    climateCat = ClimateCat.query.get(id)

    if climateCat is None:
        raise APIException('El clima con el id especificado, no fue encontrado.',status_code=403)

    return jsonify(ClimateCat.serialize(climateCat)), 200

# [POST] - Ruta para crear un [ClimateCat]
@app.route('/api/climatecat', methods=['POST'])
@jwt_required()
def storeClimateCat():

    data_request = request.get_json()

    climateCat = ClimateCat.query.filter_by(name=data_request["name"]).first()
    
    # Se valida que el name no haya sido registrado.
    if climateCat:
        return jsonify({"msg": "El name ya fue registrado."}), 401
    
    climateCat = ClimateCat(name=data_request["name"])

    try:
        db.session.add(climateCat) 
        db.session.commit()
        
        return jsonify(ClimateCat.serialize(climateCat)), 201
    
    except AssertionError as exception_message: 
        return jsonify(msg='Error: {}. '.format(exception_message)), 400

# [PUT] - Ruta para modificar un [ClimateCat]
@app.route('/api/climatecat/<int:id>', methods=['PUT'])
@jwt_required()
def updateClimateCat(id):

    climatecat = ClimateCat.query.get(id)

    if climatecat is None:
        raise APIException('El clima con el id especificado, no fue encontrado.',status_code=403)

    data_request = request.get_json()
    
    climatecat.name = data_request["name"]

    try: 
        db.session.commit()
        
        return jsonify(ClimateCat.serialize(climatecat)), 200
    
    except AssertionError as exception_message: 
        return jsonify(msg='Error: {}. '.format(exception_message)), 400

# [DELETE] - Ruta para eliminar un [ClimateCat]
@app.route('/api/climatecat/<int:id>', methods=['DELETE'])
@jwt_required()
def deleteClimateCat(id):

    climateCat = ClimateCat.query.get(id)

    if climateCat is None:
        raise APIException('El clima con el id especificado, no fue encontrado.',status_code=403)

    try:
        db.session.delete(climateCat)
        db.session.commit()
        
        return jsonify('El clima fue eliminado satisfactoriamente.'), 200
    
    except AssertionError as exception_message: 
        return jsonify(msg='Error: {}. '.format(exception_message)), 400
# FIN - Definición de EndPoints para el Modelo [ClimateCat] - FIN


# INICIO - Definición de EndPoints para el Modelo [TerrainCat] - INICIO
@app.route('/api/terraincat', methods=['GET'])
@jwt_required()
def indexAllTerrainCat():

    results = TerrainCat.query.all()

    return jsonify(list(map(lambda x: x.serialize(), results))), 200

# [GET] - Ruta para obtener un [TerrainCat]
@app.route('/api/terraincat/<int:id>', methods=['GET'])
@jwt_required()
def indexTerrainCat(id):
    terrainCat = TerrainCat.query.get(id)

    if terrainCat is None:
        raise APIException('El terreno con el id especificado, no fue encontrado.',status_code=403)

    return jsonify(TerrainCat.serialize(terrainCat)), 200

# [POST] - Ruta para crear un [TerrainCat]
@app.route('/api/terraincat', methods=['POST'])
@jwt_required()
def storeTerrainCat():

    data_request = request.get_json()

    terrainCat = TerrainCat.query.filter_by(name=data_request["name"]).first()
    
    # Se valida que el name no haya sido registrado.
    if terrainCat:
        return jsonify({"msg": "El name ya fue registrado."}), 401
    
    terrainCat = TerrainCat(name=data_request["name"])

    try:
        db.session.add(terrainCat) 
        db.session.commit()
        
        return jsonify(TerrainCat.serialize(terrainCat)), 201
    
    except AssertionError as exception_message: 
        return jsonify(msg='Error: {}. '.format(exception_message)), 400

# [PUT] - Ruta para modificar un [TerrainCat]
@app.route('/api/terraincat/<int:id>', methods=['PUT'])
@jwt_required()
def updateTerrainCat(id):

    terraincat = TerrainCat.query.get(id)

    if terraincat is None:
        raise APIException('El terreno con el id especificado, no fue encontrado.',status_code=403)

    data_request = request.get_json()
    
    terraincat.name = data_request["name"]

    try: 
        db.session.commit()
        
        return jsonify(TerrainCat.serialize(terraincat)), 200
    
    except AssertionError as exception_message: 
        return jsonify(msg='Error: {}. '.format(exception_message)), 400

# [DELETE] - Ruta para eliminar un [TerrainCat]
@app.route('/api/terraincat/<int:id>', methods=['DELETE'])
@jwt_required()
def deleteTerrainCat(id):

    terrainCat = TerrainCat.query.get(id)

    if terrainCat is None:
        raise APIException('El terreno con el id especificado, no fue encontrado.',status_code=403)

    try:
        db.session.delete(terrainCat)
        db.session.commit()
        
        return jsonify('El terreno fue eliminado satisfactoriamente.'), 200
    
    except AssertionError as exception_message: 
        return jsonify(msg='Error: {}. '.format(exception_message)), 400
# FIN - Definición de EndPoints para el Modelo [TerrainCat] - FIN


# INICIO - Definición de EndPoints para el Modelo [VehicleClassCat] - INICIO
@app.route('/api/vehicleclasscat', methods=['GET'])
@jwt_required()
def indexAllVehicleClassCat():

    results = VehicleClassCat.query.all()

    return jsonify(list(map(lambda x: x.serialize(), results))), 200

# [GET] - Ruta para obtener un [VehicleClassCat]
@app.route('/api/vehicleclasscat/<int:id>', methods=['GET'])
@jwt_required()
def indexVehicleClassCat(id):
    vehicleClassCat = VehicleClassCat.query.get(id)

    if vehicleClassCat is None:
        raise APIException('La clase de vehículo con el id especificado, no fue encontrado.',status_code=403)

    return jsonify(VehicleClassCat.serialize(vehicleClassCat)), 200

# [POST] - Ruta para crear un [VehicleClassCat]
@app.route('/api/vehicleclasscat', methods=['POST'])
@jwt_required()
def storeVehicleClassCat():

    data_request = request.get_json()

    vehicleClassCat = VehicleClassCat.query.filter_by(name=data_request["name"]).first()
    
    # Se valida que el name no haya sido registrado.
    if vehicleClassCat:
        return jsonify({"msg": "El name ya fue registrado."}), 401
    
    vehicleClassCat = VehicleClassCat(name=data_request["name"])

    try:
        db.session.add(vehicleClassCat) 
        db.session.commit()
        
        return jsonify(VehicleClassCat.serialize(vehicleClassCat)), 201
    
    except AssertionError as exception_message: 
        return jsonify(msg='Error: {}. '.format(exception_message)), 400

# [PUT] - Ruta para modificar un [VehicleClassCat]
@app.route('/api/vehicleclasscat/<int:id>', methods=['PUT'])
@jwt_required()
def updateVehicleClassCat(id):

    vehicleclasscat = VehicleClassCat.query.get(id)

    if vehicleclasscat is None:
        raise APIException('La clase de vehículo con el id especificado, no fue encontrado.',status_code=403)

    data_request = request.get_json()
    
    vehicleclasscat.name = data_request["name"]

    try: 
        db.session.commit()
        
        return jsonify(VehicleClassCat.serialize(vehicleclasscat)), 200
    
    except AssertionError as exception_message: 
        return jsonify(msg='Error: {}. '.format(exception_message)), 400

# [DELETE] - Ruta para eliminar un [VehicleClassCat]
@app.route('/api/vehicleclasscat/<int:id>', methods=['DELETE'])
@jwt_required()
def deleteVehicleClassCat(id):

    vehicleClassCat = VehicleClassCat.query.get(id)

    if vehicleClassCat is None:
        raise APIException('La clase de vehículo con el id especificado, no fue encontrado.',status_code=403)

    try:
        db.session.delete(vehicleClassCat)
        db.session.commit()
        
        return jsonify('La clase de vehículo fue eliminado satisfactoriamente.'), 200
    
    except AssertionError as exception_message: 
        return jsonify(msg='Error: {}. '.format(exception_message)), 400
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
    
    user = User(name = data_request["name"],
    first_surname = data_request["first_surname"],
    second_surname = data_request["second_surname"],
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
        raise APIException('El usuario con el id especificado, no fue encontrado.',status_code=403)

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
def indexAllPeople():

    results = People.query.all()

    return jsonify(list(map(lambda x: x.serialize(), results))), 200

# [GET] - Ruta para obtener un [People]
@app.route('/api/peoples/<int:id>', methods=['GET'])
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
        raise APIException('La persona con el id especificado, no fue encontrado.',status_code=403)

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
def indexAllPlanet():

    results = Planet.query.all()

    return jsonify(list(map(lambda x: x.serialize(), results))), 200

# [GET] - Ruta para obtener un [Planet]
@app.route('/api/planets/<int:id>', methods=['GET'])
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
        raise APIException('El planeta con el id especificado, no fue encontrado.',status_code=403)

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
def indexAllVehicle():

    results = Vehicle.query.all()

    return jsonify(list(map(lambda x: x.serialize(), results))), 200

# [GET] - Ruta para obtener un [Vehicle]
@app.route('/api/vehicles/<int:id>', methods=['GET'])
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
# [GET] - Ruta para obtener todos los [Favorite] por usuario
@app.route('/api/favorites/<int:userId>', methods=['GET'])
@jwt_required()
def indexAllFavorite(userId):
    results = Favorite.query.filter_by(user_id=userId)

    if results is None:
        raise APIException('Los favoritos del usuario con el id especificado, no fueron0 encontrados.',status_code=403)

    return jsonify(list(map(lambda x: x.serialize(), results))), 200
    # return jsonify('Entro al favorito'), 200

# [POST] - Ruta para crear un [Favorite]
@app.route('/api/favorites', methods=['POST'])
@jwt_required()
def storeFavorite():
    data_request = request.get_json()

    if  data_request["user_id"] is None or data_request["user_id"] == '':
         raise APIException('El user_id es requerido.',status_code=403)
   
    if  data_request["name"] is None or data_request["name"] == '':
         raise APIException('El name es requerido.',status_code=403)
    
    if  data_request["favorite_id"] is None or data_request["favorite_id"] == '':
         raise APIException('El favorite_id es requerido.',status_code=403)
    
    if  data_request["favorite_type"] is None or data_request["favorite_type"] == '':
         raise APIException('El favorite_type es requerido.',status_code=403)
    
    favorite = Favorite(user_id = data_request["user_id"],
    name = data_request["name"],
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

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
