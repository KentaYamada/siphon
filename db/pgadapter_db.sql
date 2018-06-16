/**
 * PostgreSQL database helper database
 * Author: Kenta Yamada
 */
DROP DATABASE IF EXISTS pgadapter_test;

-- pgadapter test database
CREATE DATABASE pgadapter_test
    WITH
    OWNER = kenta
    ENCODING = 'utf-8'
    LC_COLLATE = 'ja_JP.UTF-8'
    LC_CTYPE = 'ja_JP.UTF-8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;


CREATE TABLE car_makers (
    id serial NOT NULL,
    name text NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE cars (
    id serial NOT NULL,
    maker_id integer NOT NULL,
    name text NOT NULL,
    PRIMARY KEY(id)
);

CREATE OR REPLACE FUNCTION save_car_maker (
    p_id integer,
    p_name text
)
RETURNS void
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
    IF p_id IS NOT NULL THEN
        UPDATE car_makers SET
            name = p_name
        WHERE id = p_id;
    ELSE
        INSERT INTO car_makers (
            name
        ) VALUES (
            p_name
        );
    END IF;
END $$;

CREATE OR REPLACE FUNCTION delete_car_maker (
    p_id integer
)
RETURNS void
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
    DELETE FROM car_makers WHERE id = p_id;
END $$;

CREATE OR REPLACE FUNCTION find_car_makers_by (
    p_name text
)
RETURNS TABLE (id integer, name text)
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
    RETURN QUERY
    SELECT
        c.id,
        c.name
    FROM car_makers AS c
    WHERE c.name like '%' || p_name || '%';
END $$;


CREATE OR REPLACE FUNCTION save_car (
    p_id integer,
    p_maker_id integer,
    p_name text
)
RETURNS void
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
    IF p_id IS NOT NULL THEN
        UPDATE cars SET
            maker_id = p_maker_id,
            name = p_name
        WHERE id = p_id;
    ELSE
        INSERT INTO cars (
            maker_id,
            name
        ) VALUES (
            p_maker_id,
            p_name
        );
    END IF;
END $$;

CREATE OR REPLACE FUNCTION delete_car (
    p_id integer
)
RETURNS void
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
    DELETE FROM cars where id = p_id;
END $$;


CREATE OR REPLACE FUNCTION find_cars_by (
    p_maker_id integer
)
RETURNS TABLE (maker_name text, car_name text)
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
    RETURN QUERY
    SELECT
        m.name,
        c.name
    FROM car_makers AS m
    INNER JOIN cars AS c on m.id = c.maker_id
    WHERE m.id = p_maker_id;
END $$;
