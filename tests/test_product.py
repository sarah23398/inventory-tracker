import unittest
from flask import Flask
from ariadne import graphql_sync
import json

from main import schema

all_products = """
{
  "data": {
    "products": [
      {
        "collections": [
          {
            "id": "4",
            "name": "Kids"
          }
        ],
        "description": "3D combination puzzle",
        "image": null,
        "name": "Rubik's Cube",
        "shipments": [
          {
            "cost": 40,
            "id": "1",
            "quantity": 4
          }
        ],
        "sku": "1",
        "stock": 6,
        "tags": "toy",
        "unitCost": 10,
        "unitPrice": 12.99,
        "warehouse": {
          "id": "1",
          "location": "London"
        }
      },
      {
        "collections": [
          {
            "id": "2",
            "name": "Electronics"
          }
        ],
        "description": "Exercise machine",
        "image": null,
        "name": "Treadmill",
        "shipments": [],
        "sku": "2",
        "stock": 30,
        "tags": "fitness, machine",
        "unitCost": 130,
        "unitPrice": 150,
        "warehouse": {
          "id": "3",
          "location": "Montreal"
        }
      },
      {
        "collections": [],
        "description": "Designer vision glasses",
        "image": null,
        "name": "Eyeglasses",
        "shipments": [],
        "sku": "3",
        "stock": 15,
        "tags": "accessories, eyecare",
        "unitCost": 50,
        "unitPrice": 79,
        "warehouse": {
          "id": "2",
          "location": "Toronto"
        }
      },
      {
        "collections": [],
        "description": "Oil painting of a cat by a fireplace",
        "image": null,
        "name": "Cat Painting",
        "shipments": [],
        "sku": "4",
        "stock": 3,
        "tags": "decor, art",
        "unitCost": 15,
        "unitPrice": 30,
        "warehouse": {
          "id": "4",
          "location": "Paris"
        }
      },
      {
        "collections": [
          {
            "id": "3",
            "name": "Books"
          }
        ],
        "description": "Self help book, create tiny changes and see remarkable results",
        "image": null,
        "name": "Atomic Habits by James Clear",
        "shipments": [],
        "sku": "5",
        "stock": 6,
        "tags": "books, self-help",
        "unitCost": 11,
        "unitPrice": 19.99,
        "warehouse": {
          "id": "5",
          "location": "New York City"
        }
      },
      {
        "collections": [
          {
            "id": "2",
            "name": "Electronics"
          }
        ],
        "description": "Video game for Nintendo Switch",
        "image": null,
        "name": "Mario Party Superstars",
        "shipments": [],
        "sku": "6",
        "stock": 6,
        "tags": "video games, switch",
        "unitCost": 20,
        "unitPrice": 39.99,
        "warehouse": {
          "id": "1",
          "location": "London"
        }
      }
    ]
  }
}
"""

class ProductTest(unittest.TestCase):

    def test_query_products(self):
        query = """
query {
    products {
        sku
        name
        description
        unitPrice
        unitCost
        stock
        tags
        image
        warehouse {
            id
            location
        }
        collections {
            id
            name
        }
        shipments {
            id
            quantity
            cost
        }
    }
}
        """
        result = graphql_sync(schema, query)
        print(result)
        self.assertEqual(result, json.loads(all_products))
