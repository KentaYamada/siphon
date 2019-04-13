CREATE TABLE sales (
    id serial NOT NULL,
    sales_date date NOT NULL,
    sales_time time without time zone NOT NULL,
    total_price integer NOT NULL,
    discount_price integer NOT NULL,
    discount_rate integer NOT NULL,
    inclusive_tax integer NOT NULL,
    exclusive_tax integer NOT NULL,
    deposit integer NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE sales_items (
    id serial NOT NULL,
    sales_id integer NOT NULL,
    item_no integer NOT NULL,
    item_name text NOT NULL,
    unit_price integer NOT NULL,
    quantity integer NOT NULL,
    subtotal integer NOT NULL,
    PRIMARY KEY(id),
    UNIQUE(sales_id, item_no)
);

CREATE TABLE monthly_sales (
    id serial NOT NULL,
    sales_date date NOT NULL,
    proceeds integer NOT NULL,
    PRIMARY KEY(id),
    UNIQUE(sales_date)
);


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
