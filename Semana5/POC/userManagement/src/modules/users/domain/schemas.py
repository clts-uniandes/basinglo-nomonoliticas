from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from .entities import User
from .entities import PersonalInformation

class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        exclude = ("password", "salt", "token", "expireAt")

    id = fields.String()
    username = fields.String()
    email = fields.String()
    fullName = fields.String()
    dni = fields.String()
    phoneNumber = fields.String()
    status = fields.String()
    createdAt = fields.DateTime(format="iso")
    updateAt = fields.DateTime(format="iso")

class PersonalInformationSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = PersonalInformation
        exclude = ("password")
    id = fields.String()
    username = fields.String()
    email = fields.String()
    fullName = fields.String()
    dni = fields.String()
    phoneNumber = fields.String()
    createdAt = fields.DateTime(format="iso")
    
    

