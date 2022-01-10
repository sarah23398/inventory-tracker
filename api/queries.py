from .models import Product, Warehouse, Shipment, Collections


def resolve_products(obj, info):
    try:
        products = [product.to_dict() for product in Product.query.all()]
        payload = {
            "success": True,
            "products": products
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

def resolve_warehouses(obj, info):
    try:
        warehouses = [warehouse.to_dict() for warehouse in Warehouse.query.all()]
        payload = {
            "success": True,
            "products": warehouses
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

def resolve_shipments(obj, info):
    try:
        shipments = [shipment.to_dict() for shipment in Shipment.query.all()]
        payload = {
            "success": True,
            "products": shipments
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

def resolve_collections(obj, info):
    try:
        collections = [collection.to_dict() for collection in Collection.query.all()]
        payload = {
            "success": True,
            "products": collections
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload