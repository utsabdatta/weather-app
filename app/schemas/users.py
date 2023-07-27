from marshmallow import Schema, fields


class UserSchema(Schema):
    fname = fields.String()
    lname = fields.String()
    email = fields.String()
    created_at = fields.DateTime()
    last_login = fields.DateTime()
    is_admin = fields.Boolean()
