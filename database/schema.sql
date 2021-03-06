create table customers ( 
  id serial primary key,
  account_number integer unique not null,
  first_name varchar(30) not null,
  last_name varchar(30) not null,
  email varchar(100) not null
);

create table addresses (
  id serial primary key, 
  line_1 varchar(255) not null,
  city varchar(255) not null, 
  state varchar(255) not null,
  zip integer not null
);

create table customer_addresses (
  id serial primary key,
  customer_id integer not null references customers (id),
  addresses_id integer not null references addresses (id)
);

create table categories (
  id serial primary key,
  name varchar(100) not null,
  description varchar(255) not null
);

create table products (
  id serial primary key,
  name varchar(100) not null,
  description text not null,
  price money not null,
  category_id integer not null references categories (id) 
);

create table orders (
  id serial primary key, 
  order_num varchar(100) unique not null,
  order_date date not null,
  ship_date date not null,
  delivery_date date not null,
  customer_id integer not null references customers (id),
  shipping_address integer not null references addresses (id)
);

create table product_orders (
  id serial primary key,
  product_id integer not null references products (id),
  quantity integer not null,
  order_id integer not null references orders (id)
);