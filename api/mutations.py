from ariadne import convert_kwargs_to_snake_case, ObjectType
from datetime import date

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

@mutation.field("createWarehouse")
@convert_kwargs_to_snake_case
def resolve_create_warehouse(obj, info, input):
    try:
        warehouse = Warehouse(
            location = input['location']
        )
        db.session.add(warehouse)
        db.session.commit()
        payload = {
            "success": True,
            "warehouse": warehouse.to_dict()
        }
    except Exception as error:  # could not add warehouse
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

@mutation.field("createShipment")
@convert_kwargs_to_snake_case
def resolve_create_warehouse(obj, info, input):
    try:
        shipment = Shipment(
            date = date.fromisoformat(input['date']),
            product_sku = input['product_sku'],
            quantity = input['quantity']
        )
        db.session.add(shipment)
        db.session.commit()
        payload = {
            "success": True,
            "warehouse": shipment.to_dict()
        }
    except Exception as error:  # could not add shipment
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

@mutation.field("updateProduct")
@convert_kwargs_to_snake_case
def resolve_update_product(obj, info, sku, input):
    try:
        product = Product.query.get(sku)
        for key, value in input.items():
            setattr(product, key, value)
        db.session.commit()
        payload = {
            "success": True,
            "product": product.to_dict()
        }
    except Exception as error:  # could not update product
        payload = {
            "success": False,
            "errors":  [str(error)],
        }
    return payload

