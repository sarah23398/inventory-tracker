from main import db
from sqlalchemy.orm import relationship

association_table = db.Table('contains', db.Model.metadata,
    db.Column('collection_id', db.Integer, db.ForeignKey('collection.id')),
    db.Column('sku', db.Integer, db.ForeignKey('product.sku'))
)


class Product(db.Model):
    sku = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    unit_price: db.Column(db.Float)
    unit_cost: db.Column(db.Float)
    stock: db.Column(db.Integer)
    tags: db.Column(db.String)
    image: db.Column(db.String)
    warehouse: db.Column(db.Integer, db.ForeignKey("warehouse.id"))

    # Relationships
    storage = relationship("Warehouse", backref="products")
    collection = relationship("Collection", secondary="contains")

    def to_dict(self):
        return {
            "sku": self.sku,
            "name": self.name,
            "description": self.description,
            "unit_price": self.unit_price,
            "unit_cost": self.unit_cost,
            "stock": self.stock, 
            "tags": self.tags,
            "image": self.image,
            "warehouse": self.warehouse,
        }


class Warehouse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String)

    def to_dict(self):
        return {
            "id": self.id,
            "location": self.location
        }

class Shipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    product = db.Column(db.Integer, db.ForeignKey("product.sku"))
    quantity = db.Column(db.Integer)
    cost = db.Column(db.Float)

    # Relationship
    item = relationship("Product", backref="shipments")

    def to_dict(self):
        return {
            "id": self.id,
            "date": str(self.date.strftime('%d-%m-%Y')),
            "product": self.product,
            "quantity": self.quantity, 
            "cost": self.cost,
        }

class Collection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
        }