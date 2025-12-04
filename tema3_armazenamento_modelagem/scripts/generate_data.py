
# generate_data.py (run from project root): python scripts/generate_data.py
import json, random, uuid
from datetime import datetime, timedelta
from pathlib import Path
OUT = Path('data')
OUT.mkdir(parents=True, exist_ok=True)

def random_date(start_days_back=365):
    base = datetime.now()
    delta = timedelta(days=random.randint(0, start_days_back))
    return (base - delta).isoformat()

categories = ['electronics','fashion','home','sports','beauty']

products = []
for i in range(1,501):
    p = {
        'product_id': f'P{i:04d}',
        'name': f'Product {i}',
        'category': random.choice(categories),
        'price': round(random.uniform(5,500),2),
        'created_at': random_date(1000)
    }
    products.append(p)

orders = []
for i in range(1,2001):
    o = {
        'order_id': str(uuid.uuid4()),
        'customer_id': f'C{random.randint(1,300):04d}',
        'items': [
            {'product_id': random.choice(products)['product_id'], 'qty': random.randint(1,5)}
            for _ in range(random.randint(1,4))
        ],
        'total': None,
        'order_date': random_date(365)
    }
    o['total'] = round(sum([float(next(p for p in products if p['product_id']==it['product_id'])['price'])*it['qty'] for it in o['items']]),2)
    orders.append(o)

with open(OUT/'products.json','w',encoding='utf-8') as f:
    json.dump(products, f, indent=2, ensure_ascii=False)
with open(OUT/'orders.json','w',encoding='utf-8') as f:
    json.dump(orders, f, indent=2, ensure_ascii=False)
print('Generated data in data/')
