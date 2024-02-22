from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from ....modules.users.domain.entities import User

class EntitySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        exclude = ("username", "email", "phoneNumber", "dni", "fullName", "password", "salt", "status", "updateAt", "createdAt")

    id = fields.String()
    token = fields.String()
    expireAt = fields.DateTime(format="iso")
