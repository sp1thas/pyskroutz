![# Shop](https://developer.skroutz.gr/api/v3/shop/)

###Retrieve a single shop
```python
>>> skrtz.shop(452)
```

###Retrieve a shop's reviews
```python
>>> skrtz.shop_reviews(452)
```
###List shop locations
```python
>>> skrtz.shop_locations(452)
>>> skrtz.shop_locations(452, embed_address=True)
```

###Retrieve a single shop location
```python
>>> skrtz.shop_location(shop_id=452, lc_id=2500)
```
###Search for shops
```python
>>> skrtz.search('spartoo')
```
