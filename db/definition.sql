CREATE TABLE categories (
    id serial NOT NULL,
    name text NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE items (
    id serial NOT NULL,
    category_id integer NOT NULL,
    name text NOT NULL,
    unit_price integer NOT NULL,
    PRIMARY KEY(id)
);
