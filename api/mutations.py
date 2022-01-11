from ariadne import convert_kwargs_to_snake_case, ObjectType

from api import db
from api.models import Product, Warehouse, Shipment, Collection

mutation = ObjectType("Mutation")

@mutation.field("createProduct")
@convert_kwargs_to_snake_case
def resolve_create_product(obj, info, sku, name, description, unitPrice, unitCost, stock, tags, warehouse):
    try:
        product = Product(
            sku=sku, name=name, description=description, unitPrice=unitPrice, unitCost=unitCost, stock=stock, tags=tags, warehouse=warehouse
        )
        db.session.add(product)
        db.session.commit()
        payload = {
            "success": True,
            "product": product.to_dict()
        }
    except Exception:  # could not add product
        payload = {
            "success": False,
            "errors": [f"Product could not be added"]
        }
    return payload
