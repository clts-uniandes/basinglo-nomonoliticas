from http import HTTPStatus
from flask import request

from src.seedwork.presentation.api import crear_blueprint
from src.properties.application.commands.save_property import SaveProperty
from src.properties.application.mappers import MapperPropertyDTOJson
from src.seedwork.application.commands import exec_command
from src.seedwork.domain.exceptions import DomainException

properties_bp = crear_blueprint('properties', '/properties')

@properties_bp.route("add", methods=["POST"])
def add_property():
    try:
        property_dict = request.json
        property_map = MapperPropertyDTOJson()
        py_dto = property_map.external_to_dto(property_dict)
        command = SaveProperty(property_size=py_dto.property_size,
                               total_area_size=py_dto.total_area_size,
                               floors_number=py_dto.floors_number,
                               is_parking=py_dto.is_parking,
                               photos_registry=py_dto.photos_registry,
                               ubication=py_dto.ubication)
        exec_command(command)
        return { 'msg': 'Property saved'}, HTTPStatus.ACCEPTED
    except DomainException as e:
        return { 'msg': str(e)}, HTTPStatus.INTERNAL_SERVER_ERROR
    except Exception as e:
        return { 'msg': str(e)}, HTTPStatus.BAD_REQUEST