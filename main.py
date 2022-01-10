from api import app, db
from api import models
from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, snake_case_fallback_resolvers, ObjectType
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify
from api.queries import resolve_products, resolve_warehouses, resolve_shipments, resolve_collections

query = ObjectType("Query")

query.set_field("products", resolve_products)
query.set_field("warehouses", resolve_warehouses)
query.set_field("shipments", resolve_shipments)
query.set_field("collections", resolve_collections)

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, query, snake_case_fallback_resolvers
)
