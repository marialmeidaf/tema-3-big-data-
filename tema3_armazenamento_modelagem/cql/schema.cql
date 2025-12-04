
CREATE KEYSPACE IF NOT EXISTS ceubks WITH replication = { 'class': 'SimpleStrategy', 'replication_factor': 1 };

CREATE TABLE IF NOT EXISTS ceubks.products (
  product_id text PRIMARY KEY,
  name text,
  category text,
  price decimal,
  created_at timestamp
);

CREATE TABLE IF NOT EXISTS ceubks.orders_by_customer (
  customer_id text,
  order_date timestamp,
  order_id uuid,
  items text,
  total decimal,
  PRIMARY KEY (customer_id, order_date, order_id)
) WITH CLUSTERING ORDER BY (order_date DESC);
