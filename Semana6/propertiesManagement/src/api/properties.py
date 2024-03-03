from http import HTTPStatus
from flask import request

from src.seedwork.presentation.api import crear_blueprint
from src.modules.properties.application.commands.save_property import SaveProperty
from src.modules.properties.application.commands.update_property import UpdateProperty
from src.modules.properties.application.mappers import MapperPropertyDTOJson
from src.seedwork.application.commands import exec_command
from src.seedwork.domain.exceptions import DomainException

properties_bp = crear_blueprint('properties', '/properties')

@properties_bp.route("", methods=["POST"])
def add_property():
    try:
        property_dict = request.json
        property_map = MapperPropertyDTOJson()
        py_dto = property_map.external_to_dto(property_dict)
        command = SaveProperty(property_size=py_dto.property_size,
                               property_type=py_dto.property_type,
                               total_area_size=py_dto.total_area_size,
                               floors_number=py_dto.floors_number,
                               is_parking=py_dto.is_parking,
                               photos_registry=py_dto.photos_registry,
                               ubication=py_dto.ubication)
        exec_command(command)
        return { 'msg': 'Property saved'}, HTTPStatus.ACCEPTED
    except Exception as e:
        return {"msg": str(e)}, HTTPStatus.INTERNAL_SERVER_ERROR

@properties_bp.route("/<string:property_id>", methods=["PUT"])
def update_property(property_id):
    try:
        property_dict = request.json
        property_map = MapperPropertyDTOJson()
        py_dto = property_map.external_to_dto(property_dict)
        command = UpdateProperty(id=property_id,
                                property_size=py_dto.property_size,
                                property_type=py_dto.property_type,
                                total_area_size=py_dto.total_area_size,
                                floors_number=py_dto.floors_number,
                                is_parking=py_dto.is_parking,
                                photos_registry=py_dto.photos_registry,
                                ubication=py_dto.ubication)
        exec_command(command)
        return { 'msg': 'Property updated'}, HTTPStatus.ACCEPTED
    except Exception as e:
        return {"msg": str(e)}, HTTPStatus.INTERNAL_SERVER_ERROR
