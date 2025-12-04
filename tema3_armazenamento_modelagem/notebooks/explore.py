
# Explore script for Tema 3
# Requires: pip install pymongo cassandra-driver
from pymongo import MongoClient
from cassandra.cluster import Cluster
mc = MongoClient('mongodb://root:example@localhost:27017/?authSource=admin')
db = mc['ceubdb']
print('collections:', db.list_collection_names())
for p in db.products.find().limit(2):
    print(p)
cluster = Cluster(['127.0.0.1'])
session = cluster.connect()
print('Cassandra session ready (list keyspaces):', session.execute("SELECT keyspace_name FROM system_schema.keyspaces;"))
