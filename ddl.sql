PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

INSERT INTO collection (
                           id,
                           name
                       )
                       VALUES (
                           1,
                           'food'
                       );

INSERT INTO collection (
                           id,
                           name
                       )
                       VALUES (
                           2,
                           'electronics'
                       );

INSERT INTO collection (
                           id,
                           name
                       )
                       VALUES (
                           3,
                           'Books'
                       );

INSERT INTO collection (
                           id,
                           name
                       )
                       VALUES (
                           4,
                           'Kids'
                       );

INSERT INTO contains (
                         collection_id,
                         sku
                     )
                     VALUES (
                         2,
                         6
                     );

INSERT INTO contains (
                         collection_id,
                         sku
                     )
                     VALUES (
                         2,
                         2
                     );

INSERT INTO contains (
                         collection_id,
                         sku
                     )
                     VALUES (
                         3,
                         5
                     );

INSERT INTO contains (
                         collection_id,
                         sku
                     )
                     VALUES (
                         4,
                         1
                     );


INSERT INTO product (
                        sku,
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
                        1,
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
                        sku,
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
                        2,
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
                        sku,
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
                        3,
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
                        sku,
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
                        4,
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
                        sku,
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
                        5,
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
                        sku,
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
                        6,
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
                          id,
                          location
                      )
                      VALUES (
                          1,
                          'london'
                      );

INSERT INTO warehouse (
                          id,
                          location
                      )
                      VALUES (
                          2,
                          'Toronto'
                      );

INSERT INTO warehouse (
                          id,
                          location
                      )
                      VALUES (
                          3,
                          'Montreal'
                      );

INSERT INTO warehouse (
                          id,
                          location
                      )
                      VALUES (
                          4,
                          'Paris'
                      );

INSERT INTO warehouse (
                          id,
                          location
                      )
                      VALUES (
                          5,
                          'New York City'
                      );


COMMIT;
PRAGMA foreign_keys = off;