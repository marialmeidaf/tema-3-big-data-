
#!/usr/bin/env bash
# from project root: bash scripts/load_cassandra.sh
docker cp cql/schema.cql ceub_cassandra:/schema.cql
docker exec -i ceub_cassandra cqlsh -f /schema.cql
docker cp data/products_for_cassandra.csv ceub_cassandra:/products.csv
docker exec -i ceub_cassandra cqlsh -e "COPY ceubks.products(product_id, name, category, price, created_at) FROM '/products.csv' WITH HEADER = TRUE;"
