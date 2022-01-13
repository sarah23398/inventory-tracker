from .models import Product, Warehouse, Shipment, Collection
import sys
from ariadne import convert_kwargs_to_snake_case, ObjectType

query = ObjectType("Query")
product = ObjectType("Product")
warehouse = ObjectType("Warehouse")
shipment = ObjectType("Shipment")
collection = ObjectType("Collection")

@query.field("products")
def resolve_products(obj, info):
    products = [product.to_dict() for product in Product.query.all()]
    payload = products
    return payload

@query.field("product")
@convert_kwargs_to_snake_case
def resolve_product(obj, info, sku):
    product = Product.query.get(sku)
    payload = product.to_dict()
    return payload

@query.field("warehouses")
def resolve_warehouses(obj, info):
    warehouses = [warehouse.to_dict() for warehouse in Warehouse.query.all()]
    payload = warehouses
    return payload

@query.field("warehouse")
@convert_kwargs_to_snake_case
def resolve_warehouse(obj, info, id):
    warehouse = Warehouse.query.get(id)
    payload = warehouse.to_dict()
    return payload

@query.field("shipments")
def resolve_shipments(obj, info):
    shipments = [shipment.to_dict() for shipment in Shipment.query.all()]
    payload = shipments
    return payload

@query.field("shipment")
@convert_kwargs_to_snake_case
def resolve_shipment(obj, info, id):
    shipment = Shipment.query.get(id)
    payload = shipment.to_dict()
    return payload

@query.field("collections")
def resolve_collections(obj, info):
    collections = [collection.to_dict() for collection in Collection.query.all()]
    payload = collections
    return payload

@query.field("collection")
@convert_kwargs_to_snake_case
def resolve_collection(obj, info, id):
    collection = Collection.query.get(id)
    payload = collection.to_dict()
    return payload

@query.field("filterProduct")
@convert_kwargs_to_snake_case
def resolve_product_filter(obj, info, filter):
    products = []
    
    range = [None, None]
    if 'min_stock' in filter and 'max_stock' in filter:
        range[0] = filter['min_stock']
        range[1] = filter['max_stock']
    elif 'min_stock' in filter:
        range[0] = filter['min_stock']
    elif 'max_stock' in filter:
        range[1] = filter['max_stock']
    
    filter_tags = []
    if 'tags' in filter:
        filter_tags = filter['tags'].split(', ')

    for product in Product.query.all():
        insert = True
        if range[0] is not None and range[1] is not None:
            if product.stock < range[0] or product.stock > range[1]:
                insert = False
        elif range[0] is not None:
            if product.stock < range[0]:
                insert = False
        elif range[1] is not None:
            if product.stock > range[1]:
                insert = False
        
        product_tags = product.tags.split(', ')
        for tag in filter_tags:
            if tag not in product_tags:
                insert = False
        
        if insert:
            products.append(product)
    payload = [p.to_dict() for p in products]
    return payload
