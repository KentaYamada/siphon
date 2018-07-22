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

CREATE TABLE users (
    id serial NOT NULL,
    name text NOT NULL,
    nickname text NULL,
    email text NOT NULL,
    password text NOT NULL,
    PRIMARY KEY(id),
    UNIQUE(password)
);
