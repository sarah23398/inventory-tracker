PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

INSERT INTO collection (
                           name
                       )
                       VALUES (
                           'Food'
                       );

INSERT INTO collection (
                           name
                       )
                       VALUES (
                           'Electronics'
                       );

INSERT INTO collection (
                           name
                       )
                       VALUES (
                           'Books'
                       );

INSERT INTO collection (
                           name
                       )
                       VALUES (
                           'Kids'
                       );

INSERT INTO contains (
                         id,
                         sku
                     )
                     VALUES (
                         2,
                         6
                     );

INSERT INTO contains (
                         id,
                         sku
                     )
                     VALUES (
                         2,
                         2
                     );

INSERT INTO contains (
                         id,
                         sku
                     )
                     VALUES (
                         3,
                         5
                     );

INSERT INTO contains (
                         id,
                         sku
                     )
                     VALUES (
                         4,
                         1
                     );


INSERT INTO product (
                        name,
                        description,
                        unit_price,
                        unit_cost,
                        stock,
                        tags,
                        image,
                        warehouse_id
                    )
                    VALUES (
                        'Rubik''s Cube',
                        '3D combination puzzle',
                        12.99,
                        10.0,
                        10,
                        'toy',
                        NULL,
                        1
                    );

INSERT INTO product (
                        name,
                        description,
                        unit_price,
                        unit_cost,
                        stock,
                        tags,
                        image,
                        warehouse_id
                    )
                    VALUES (
                        'Treadmill',
                        'Exercise machine',
                        150.0,
                        130.0,
                        30,
                        'fitness, machine',
                        NULL,
                        3
                    );

INSERT INTO product (
                        name,
                        description,
                        unit_price,
                        unit_cost,
                        stock,
                        tags,
                        image,
                        warehouse_id
                    )
                    VALUES (
                        'Eyeglasses',
                        'Designer vision glasses',
                        79.0,
                        50.0,
                        15,
                        'accessories, eyecare',
                        NULL,
                        2
                    );

INSERT INTO product (
                        name,
                        description,
                        unit_price,
                        unit_cost,
                        stock,
                        tags,
                        image,
                        warehouse_id
                    )
                    VALUES (
                        'Cat Painting',
                        'Oil painting of a cat by a fireplace',
                        30.0,
                        15.0,
                        3,
                        'decor, art',
                        NULL,
                        4
                    );

INSERT INTO product (
                        name,
                        description,
                        unit_price,
                        unit_cost,
                        stock,
                        tags,
                        image,
                        warehouse_id
                    )
                    VALUES (
                        'Atomic Habits by James Clear',
                        'Self help book, create tiny changes and see remarkable results',
                        19.99,
                        11.0,
                        6,
                        'books, self-help',
                        NULL,
                        5
                    );

INSERT INTO product (
                        name,
                        description,
                        unit_price,
                        unit_cost,
                        stock,
                        tags,
                        image,
                        warehouse_id
                    )
                    VALUES (
                        'Mario Party Superstars',
                        'Video game for Nintendo Switch',
                        39.99,
                        20.0,
                        6,
                        'video games, switch',
                        NULL,
                        1
                    );


INSERT INTO warehouse (
                          location
                      )
                      VALUES (
                          'London'
                      );

INSERT INTO warehouse (
                          location
                      )
                      VALUES (
                          'Toronto'
                      );

INSERT INTO warehouse (
                          location
                      )
                      VALUES (
                          'Montreal'
                      );

INSERT INTO warehouse (
                          location
                      )
                      VALUES (
                          'Paris'
                      );

INSERT INTO warehouse (
                          location
                      )
                      VALUES (
                          'New York City'
                      );


COMMIT;
PRAGMA foreign_keys = off;