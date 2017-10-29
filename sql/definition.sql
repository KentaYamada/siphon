DROP TABLE IF EXISTS categories;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS tax;

CREATE TABLE sales (
     no             serial    NOT NULL
    ,sales_date     timestamp NOT NULL
    ,total          integer   NOT NULL
    ,discount_price integer   NOT NULL
    ,discount_rate  integer   NOT NULL
    ,inclusive_tax  integer   NOT NULL
    ,external_tax   integer   NOT NULL
    ,deposit        integer   NOT NULL
    ,PRIMARY KEY(no)
);

CREATE TABLE sales_items (
    no        integer NOT NULL
   ,item_no   integer NOT NULL
   ,item_name text    NOT NULL
   ,price     integer NOT NULL
   ,quantity  integer NOT NULL
   ,subtotal  integer NOT NULL
   ,PRIMARY KEY(no, item_no)
);

CREATE TABLE monthly_sales (
    sales_date date    NOT NULL
   ,amount     integer NOT NULL
   ,PRIMARY KEY(sales_date)
);

CREATE TABLE monthly_sales_items (
    ,sales_date date    NOT NULL
    ,item       text    NOT NULL
    ,quantity   integer NOT NULL
    ,PRIMARY KEY(sales_date)
);

CREATE TABLE categories (
    id    serial  NOT NULL
    ,name text    NOT NULL
    ,PRIMARY KEY(id)
);

CREATE TABLE products (
    id           serial  NOT NULL
    ,category_id integer NOT NULL
    ,name        text    NOT NULL
    ,price       integer NOT NULL
    ,PRIMARY KEY(id)
);

CREATE TABLE tax (
    rate integer NOT NULL
   ,tax_type text NOT NULL
);
