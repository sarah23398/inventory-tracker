from .models import Product, Warehouse, Shipment, Collection
import sys

def resolve_products(obj, info):
    products = [product.to_dict() for product in Product.query.all()]
    payload = products
    return payload


def resolve_warehouses(obj, info):
    warehouses = [warehouse.to_dict() for warehouse in Warehouse.query.all()]
    payload = warehouses
    return payload

def resolve_shipments(obj, info):
    shipments = [shipment.to_dict() for shipment in Shipment.query.all()]
    payload = shipments
    return payload

def resolve_collections(obj, info):
    collections = [collection.to_dict() for collection in Collection.query.all()]
    payload = collections
    return payload