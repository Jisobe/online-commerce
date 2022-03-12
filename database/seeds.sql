insert into addresses (line_1, city, state, zip)
values
('123 Sesame St', 'Los Angeles', 'California', 93028),
('554 E York Pl', 'New York', 'New York', 10553),
('5321 Mellow Ln', 'San Diego', 'California', 92014),
('45 Castle Dr', 'Little Rock', 'Arkansas', 64093),
('3880 Veterans Ave', 'Columbus', 'Ohio', 54007),
('39309 Main St', 'Denver', 'Colorado', 75419),
('70689 Kings Way', 'Norfolk', 'Virginia', 23095),
('785 Green Ave', 'Austin', 'Texas', 56071);

insert into customers (account_number, first_name, last_name, email)
values
(294058395, 'Daisy', 'Duke', 'dduke@hotmail.com'),
(930284932, 'Harry', 'Potter', 'chosen.one@gmail.com'),
(495837290, 'Ron', 'Weasley', 'weasley8@mailto.com'),
(201938573, 'Hermione', 'Granger', 'hermione.granger@gmail.com'),
(102958395, 'Albus', 'Dumbledore', 'dumle1887@yahoo.com'),
(302948593, 'Severus', 'Snape', 'potionmaster22@gmail.com'),
(049303920, 'Bugs', 'Bunny', 'bunnyhop90@yahoo.com');
  

insert into customer_addresses (customer_id, addresses_id)
values
(1, 5),
(2, 3),
(3, 7),
(4, 7),
(5, 2),
(6, 1),
(7, 4);

insert into categories (name, description)
values
('Kitchen and Cookware', 'Kitchen Essentials, pots, pans, towels, dishes'),
('Electronics', 'Computers, Headphones, Monitors, TVs'),
('Garden', 'Seeds, Pots, Soil, Fertilizer'),
('Toys and Games', 'Kids toys, puzzles, board games, bikes, rollerblades'),
('Entertainment', 'Books, movies, records, cds'),
('Apparel', 'Mens clothes, womens clothes, boys clothes, girls clothes');

insert into products (name, description, price, category_id)
values
('Skillet', '10 inch non-stick skillet', 35.99, 1),
('Step Stool', 'Two step step stool', 14.50, 1),
('t-shirt', 'mens size L grey t-shirt, crew neck', 5.99, 6),
('Vizio TV', '65 inch HD Vizio TV', 899.99, 2),
('Harry Potter and the Prisoner of Azkaban', 'DVD, third Harry Potter Movie', 15.50, 5),
('Plumaria Fertilizer', 'Easy shake fertilizer for plumarias', 22.49, 3),
('Monoploy', 'boardgame fun for the whole family', 19.99, 4),
('Kettle', 'Grey electric kettle for water', 42.59, 1),
('pants', 'size 10 womens sweatpants', 10.00, 6),
('Glasses', 'set of 6 cups', 21.80, 1),
('Sound Bar', 'Spacial Awareness sound bar for entertainment center', 68.95, 2),
('Pots', 'Set of 2 12 inch pots', 40.00, 3),
('Aja by Steely Dan', 'Vinyl Record', 25.70, 5),
('Mario Party', 'Game for Nintendo switch', 59.99, 4),
('Untamed by Glennon Doyle', 'Help self book', 18.89, 5),
('Basketball', 'Professional grade', 18.50, 4);

insert into orders (order_num, order_date, ship_date, delivery_date, customer_id, shipping_address)
values
('1nnid02jed39dn92', '2019-01-19', '2019-01-21', '2019-01-31', 5, 2),
('9n1nd9d3n10sklso', '2019-03-10', '2019-03-20', '2019-04-01', 2, 6),
('30dm0md94nfoqdkn', '2019-06-20', '2019-06-25', '2019-07-02', 1, 5),
('59fn302dkdm202ms', '2020-02-16', '2020-02-19', '2020-02-28', 4, 7),
('mo340dk03dn39014', '2020-04-11', '2020-04-16', '2020-04-26', 6, 1),
('2292d003n30sm1pq', '2020-05-09', '2020-05-17', '2020-05-30', 3, 7),
('02mxmene9303495d', '2020-07-15', '2020-07-18', '2020-07-29', 7, 4),
('1jd0wm03n58fj920', '2020-07-19', '2020-07-30', '2020-08-07', 6, 8),
('2nis0wmx03n48dnw', '2020-10-22', '2020-10-31', '2020-11-17', 5, 2),
('93nd93n20snue8c2', '2020-12-01', '2020-12-14', '2020-12-28', 1, 5),
('ksm9m302ms0846jd', '2021-05-03', '2021-05-18', '2021-05-26', 3, 7),
('2nx93nf84ncm2902', '2021-07-02', '2021-07-15', '2021-07-30', 7, 4),
('02md1nd984b9cnn3', '2021-08-19', '2021-08-29', '2021-09-12', 5, 2),
('93nc930qjacnieie', '2021-10-26', '2021-10-30', '2021-11-11', 4, 7),
('2n9ncwxkmsj94nfq', '2021-11-13', '2021-11-17', '2021-12-02', 2, 6);

insert into product_orders (product_id, quantity, order_id)
values
(2, 1, 1),
(5, 1, 1),
(16, 1, 2),
(4, 1, 3),
(7, 1, 4),
(3, 5, 5),
(8, 1, 5),
(11, 1, 6),
(1, 1, 7),
(9, 2, 8),
(6, 1, 9),
(13, 1, 10),
(10, 1, 11),
(5, 1, 11),
(16, 1, 12),
(12, 1, 13),
(14, 1, 13),
(3, 5, 14),
(15, 1, 15);
