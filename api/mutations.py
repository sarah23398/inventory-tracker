from ariadne import convert_kwargs_to_snake_case, ObjectType

from api import db
from api.models import Product, Warehouse, Shipment, Collection

mutation = ObjectType("Mutation")

@mutation.field("createProduct")
@convert_kwargs_to_snake_case
def resolve_create_product(obj, info, input):
    try:
        product = Product(
            name=input['name'], 
            description=input['description'], 
            unit_price=input['unit_price'], 
            unit_cost=input['unit_cost'], 
            stock=input['stock'], 
            tags=input['tags'], 
            warehouse_id=input['warehouse_id']
        )
        db.session.add(product)
        db.session.commit()
        payload = {
            "success": True,
            "product": product.to_dict()
        }
    except Exception as error:  # could not add product
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload
