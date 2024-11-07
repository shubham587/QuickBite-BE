from marshmallow import fields, Schema, validate,ValidationError

def validate_price(price):
    if price > 0:
        return True
    return ValidationError("Price must greater than zero")

class ProductSchema(Schema):
    id = fields.Int(required=True)
    food_name = fields.Str(required=True, validate=validate.Length(min=2))
    price = fields.Float(required=True, validate = validate.Range(min=1, error="Price must be greater than zero"))
    seller_name = fields.Str(required=True, validate=validate.Length(min=2))
    description = fields.Str(required=True)
    category = fields.Str(required=True)
    type = fields.Str(required=True, validate=validate.OneOf(["veg", "non-veg"]))
    image = fields.Url(required=True, error_messages={"invalid": "Not a valid URL"})
    location = fields.List(fields.Str(), required=True)