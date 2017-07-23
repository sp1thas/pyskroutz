[SKU](https://developer.skroutz.gr/api/v3/sku/)
=========================================
### List SKUs of specific category
```python
>>> skrtz.sku_category(40)
```
#### Ordering
order_by=pricevat|popularity|rating
```python
>>> skrtz.sku_category(40 order_by='name')
```
order_dir=asc|desc
```python
>>> skrtz.sku_category(40, order_dir='asc')
```
#### Filtring
By search keyword
```python
>>> skrtz.sku_category(40, q='iphone')
```
#### By manufacturers
```python
>>> skrtz.sku_category(40, manufacturer_ids=[28,2])
```
#### By filters
```python
>>> skrtz.sku_category(40, filter_ids=['355559','6282'])
```
#### Meta
```python
>>> skrtz.sku_category(40, include_meta='available_filters')
```
### Retrieve a single SKU
```python
>>> skrtz.sku_single(3690169)
```
### Retrieve similar SKUs
```python
>>> skrtz.sku_similar(3034682)
```
### Retrieve an SKU's products
```python
>>> skrtz.sku_products(3783654)
```
### Retrieve an SKU's reviews
```python
>>> skrtz.sku_reviews(3783654)
```
### Retrieve an SKU's specifications
```python
>>> skrtz.sku_specifications(3783654)
```
Retrieve a SKU's price history
```python
>>> skrtz.sku_pricehistory(3783654)
```
