from .models import Product, Warehouse, Shipment, Collection
import sys
from ariadne import convert_kwargs_to_snake_case

def resolve_products(obj, info):
    products = [product.to_dict() for product in Product.query.all()]
    payload = products
    return payload

@convert_kwargs_to_snake_case
def resolve_product(obj, info, sku):
    product = Product.query.get(sku)
    payload = product.to_dict()
    return payload

def resolve_warehouses(obj, info):
    warehouses = [warehouse.to_dict() for warehouse in Warehouse.query.all()]
    payload = warehouses
    return payload

@convert_kwargs_to_snake_case
def resolve_warehouse(obj, info, id):
    warehouse = Warehouse.query.get(id)
    payload = warehouse.to_dict()
    return payload

def resolve_shipments(obj, info):
    shipments = [shipment.to_dict() for shipment in Shipment.query.all()]
    payload = shipments
    return payload

@convert_kwargs_to_snake_case
def resolve_shipment(obj, info, id):
    shipment = Shipment.query.get(id)
    payload = shipment.to_dict()
    return payload

def resolve_collections(obj, info):
    collections = [collection.to_dict() for collection in Collection.query.all()]
    payload = collections
    return payload

@convert_kwargs_to_snake_case
def resolve_collection(obj, info, id):
    collection = Collection.query.get(id)
    payload = collection.to_dict()
    return payload
