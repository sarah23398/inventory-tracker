from main import db
from sqlalchemy.orm import relationship

association_table = db.Table('contains', db.Model.metadata,
    db.Column('id', db.Integer, db.ForeignKey('collection.id')),
    db.Column('sku', db.Integer, db.ForeignKey('product.sku'))
)


class Warehouse(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    location = db.Column(db.String)

    # Relationships
    products = db.relationship('Product', back_populates='warehouse')

    def to_dict(self):
        return {
            "id": self.id,
            "location": self.location,
            "products": self.products,
        }


class Product(db.Model):
    sku = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    unit_price = db.Column(db.Float)
    unit_cost = db.Column(db.Float)
    stock = db.Column(db.Integer)
    tags = db.Column(db.String)
    image = db.Column(db.String)
    warehouse_id = db.Column(db.Integer, db.ForeignKey(Warehouse.id))

    # Relationships
    warehouse = db.relationship('Warehouse', back_populates='products')
    collections = db.relationship('Collection', secondary="contains", back_populates="products")
    shipments = db.relationship('Shipment', back_populates="product")

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
            "collections": self.collections,
            "shipments": self.shipments,
        }


class Collection(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    
    # Relationships
    products = db.relationship('Product', secondary="contains", back_populates="collections")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "products": self.products,
        }


class Shipment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date)
    product_sku = db.Column(db.Integer, db.ForeignKey(Product.sku))
    quantity = db.Column(db.Integer)
    cost = db.Column(db.Float)

    # Relationship
    product = relationship('Product', back_populates='shipments')

    def to_dict(self):
        return {
            "id": self.id,
            "date": self.date,
            "product": self.product,
            "quantity": self.quantity, 
            "cost": self.cost,
        }
