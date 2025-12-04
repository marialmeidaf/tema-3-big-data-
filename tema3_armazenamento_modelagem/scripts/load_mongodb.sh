
#!/usr/bin/env bash
# from project root: bash scripts/load_mongodb.sh
docker exec -i ceub_mongodb bash -c "mkdir -p /tmp/data"
docker cp data/products.json ceub_mongodb:/tmp/data/products.json
docker cp data/orders.json ceub_mongodb:/tmp/data/orders.json
docker exec -i ceub_mongodb mongoimport --username root --password example --authenticationDatabase admin --db ceubdb --collection products --file /tmp/data/products.json --jsonArray --drop
docker exec -i ceub_mongodb mongoimport --username root --password example --authenticationDatabase admin --db ceubdb --collection orders --file /tmp/data/orders.json --jsonArray --drop
