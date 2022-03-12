-- item                                       can have

-- customers                                  many addresses
-- ----                                       many orders
-- id serial pk
-- first_name varchar(30) 
-- last_name varchar(30)



-- products                                  many orders
-- ----                                      one category
-- id serial pk 
-- name varchar(100)
-- description text
-- price money
-- category_id FK >- categories.id



-- categories                                  many products
-- ----
-- id serial pk
-- name varchar(100)
-- description varchar(255)




-- orders                                  one customer
-- ----                                    one address
-- id serial pk                            many products      
-- order_id UUID
-- order_date date
-- ship_date date
-- delivery_date date
-- customer_id FK >- customers.id
-- address_id FK >- address.id



-- addresses                                  many customers
-- ----                                       many orders
-- id serial pk 
-- line_1 varchar(255)
-- city varchar(255)
-- state varchar(255)
-- zip int(10)



-- product_orders
-- ----
-- id serial pk
-- product_id FK - products.id
-- order_id FK - orders.order_id



-- customer_addresses
-- ----
-- id serial pk
-- customer_id FK - customers.id
-- address_id FK - addresses.id

