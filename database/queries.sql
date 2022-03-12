  -- 1. Retrieve the first name, last name, and email address of all customers that have a Gmail email address.

select first_name, last_name, email 
from customers
where email like '%@gmail.com';

  -- 2. Retrieve the address of the customers and the order IDs for all orders that were placed in 2020

select orders.id as order_id, addresses.* 
from orders 
join addresses on orders.shipping_address = addresses.id
where date_part('year', order_date) = 2020;

  -- 3. Retrieve all product details for products that are under the "Kitchen" category

select products.*
from products
join categories on products.category_id = categories.id
where categories.name ilike '%kitchen%';

  -- 4. Retrieve the product names and prices of all products ordered by the customer with first name "Bugs" and last name "Bunny"

select product_orders.quantity, products.name, products.price
from products
join product_orders on products.id = product_orders.product_id
join orders on product_orders.order_id = orders.id
join customers on orders.customer_id = customers.id
where first_name = 'Bugs'
and last_name = 'Bunny';