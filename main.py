from api import app, db
from api import models
from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, snake_case_fallback_resolvers, ObjectType
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify
from api.queries import resolve_products, resolve_product, resolve_warehouses, resolve_warehouse, \
    resolve_shipments, resolve_shipment, resolve_collections, resolve_collection

query = ObjectType("Query")

query.set_field("products", resolve_products)
query.set_field("product", resolve_product)
query.set_field("warehouses", resolve_warehouses)
query.set_field("warehouse", resolve_warehouse)
query.set_field("shipments", resolve_shipments)
query.set_field("shipment", resolve_shipment)
query.set_field("collections", resolve_collections)
query.set_field("collection", resolve_collection)

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, query, snake_case_fallback_resolvers
)

@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()

    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code
