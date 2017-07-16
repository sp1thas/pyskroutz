#SKU

```python
>>> # List SKUs of specific category
>>> skrtz.sku_category(40)
>>> # Ordering
>>> # order_by=pricevat|popularity|rating
>>> skrtz.sku_category(40 order_by='name')
>>> # order_dir=asc|desc
>>> skrtz.sku_category(40, order_dir='asc')
>>> # Filtring
>>> # By search keyword
>>> skrtz.sku_category(40, q='iphone')
>>> # By manufacturers
>>> skrtz.sku_category(40, manufacturer_ids=[28,2])
>>> # By filters
>>> skrtz.sku_category(40, filter_ids=['355559','6282'])
>>> # Meta
>>> skrtz.sku_category(40, include_meta='available_filters')
>>> # Retrieve a single SKU
>>> skrtz.sku_single(3690169)
>>> # Retrieve similar SKUs
>>> skrtz.sku_similar(3034682)
>>> # Retrieve an SKU's products
>>> skrtz.sku_products(3783654)
>>> # Retrieve an SKU's reviews
>>> skrtz.sku_reviews(3783654)
>>> # Retrieve an SKU's specifications
>>> skrtz.sku_specifications(3783654)
>>> # Retrieve a SKU's price history
>>> skrtz.sku_pricehistory(3783654)
```
