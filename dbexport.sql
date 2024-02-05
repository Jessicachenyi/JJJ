--
-- File generated with SQLiteStudio v3.4.4 on Mon Feb 5 04:38:21 2024
--
-- Text encoding used: UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: menu_items
CREATE TABLE IF NOT EXISTS menu_items (
    id          INTEGER PRIMARY KEY,
    name        TEXT    NOT NULL,
    description TEXT,
    price       REAL    NOT NULL,
    category    TEXT
);

INSERT INTO menu_items (
                           id,
                           name,
                           description,
                           price,
                           category
                       )
                       VALUES (
                           1,
                           'Bun (Pork/Chicken/Beef/Mushrooms/Vegetables',
                           'Delicious steamed buns filled with your choice of filling',
                           1.5,
                           'Eat'
                       );

INSERT INTO menu_items (
                           id,
                           name,
                           description,
                           price,
                           category
                       )
                       VALUES (
                           2,
                           'Deep Fried Dough Stick',
                           'Crispy and golden brown, perfect for dipping',
                           1.5,
                           'Eat'
                       );

INSERT INTO menu_items (
                           id,
                           name,
                           description,
                           price,
                           category
                       )
                       VALUES (
                           3,
                           'Soup Dumpling',
                           'Juicy dumplings filled with savory broth.',
                           3.2,
                           'Eat'
                       );

INSERT INTO menu_items (
                           id,
                           name,
                           description,
                           price,
                           category
                       )
                       VALUES (
                           4,
                           'Tea Egg',
                           'Hard-boiled egg soaked in a flavorful tea-infused marinade.',
                           0.8,
                           'Eat'
                       );

INSERT INTO menu_items (
                           id,
                           name,
                           description,
                           price,
                           category
                       )
                       VALUES (
                           5,
                           'Congee/Rice Porridge',
                           'Warm and comforting, perfect for any meal.',
                           3.8,
                           'Eat'
                       );

INSERT INTO menu_items (
                           id,
                           name,
                           description,
                           price,
                           category
                       )
                       VALUES (
                           6,
                           'Soy Milk',
                           'Freshly made, rich, and creamy.',
                           2.5,
                           'Drink'
                       );

INSERT INTO menu_items (
                           id,
                           name,
                           description,
                           price,
                           category
                       )
                       VALUES (
                           7,
                           'Still/Mineral Water',
                           'Refreshingly pure water, still or sparkling.',
                           0.99,
                           'Drink'
                       );

INSERT INTO menu_items (
                           id,
                           name,
                           description,
                           price,
                           category
                       )
                       VALUES (
                           8,
                           'Cola',
                           'Classic cola, chilled to perfection.',
                           1.2,
                           'Drink'
                       );

INSERT INTO menu_items (
                           id,
                           name,
                           description,
                           price,
                           category
                       )
                       VALUES (
                           9,
                           'Hot Tea',
                           'A selection of fine teas served hot.',
                           1.5,
                           'Drink'
                       );

INSERT INTO menu_items (
                           id,
                           name,
                           description,
                           price,
                           category
                       )
                       VALUES (
                           10,
                           'Hot Milk',
                           'Warm milk, a comforting classic.',
                           0.99,
                           'Drink'
                       );


-- Table: username
CREATE TABLE IF NOT EXISTS username (
    userid   NUMERIC PRIMARY KEY
                     UNIQUE
                     NOT NULL,
    username TEXT    NOT NULL,
    password TEXT    NOT NULL,
    email    TEXT    NOT NULL
);

INSERT INTO username (
                         userid,
                         username,
                         password,
                         email
                     )
                     VALUES (
                         1,
                         'Duncan',
                         'NotGood',
                         'me@example.com'
                     );

INSERT INTO username (
                         userid,
                         username,
                         password,
                         email
                     )
                     VALUES (
                         6,
                         'JQ',
                         '1234567',
                         'me5@example.com'
                     );

INSERT INTO username (
                         userid,
                         username,
                         password,
                         email
                     )
                     VALUES (
                         5,
                         'Ralph',
                         '12345678',
                         'me4@example.com'
                     );

INSERT INTO username (
                         userid,
                         username,
                         password,
                         email
                     )
                     VALUES (
                         4,
                         'Charles',
                         'hello',
                         'me3@example.com'
                     );

INSERT INTO username (
                         userid,
                         username,
                         password,
                         email
                     )
                     VALUES (
                         3,
                         'Vera',
                         'Hell',
                         'me2@example.com'
                     );

INSERT INTO username (
                         userid,
                         username,
                         password,
                         email
                     )
                     VALUES (
                         2,
                         'Jessica',
                         '123456',
                         'me1@example.com'
                     );


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
