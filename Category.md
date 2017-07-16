# Category

```python
>>> # List all categories
>>> skrtz.categories()
>>> # Retrieve a single category
>>> skrtz.category(1442)
>>> # Retrieve the parent of a category: 
>>> skrtz.category_parent(1442)
>>> # Retrieve the root category
>>> skrtz.category_root(1442)
>>> # List the children categories of a category
>>> skrtz.category_children(252)
>>> # List a category's specifications
>>> skrtz.category_specifications(40)
>>> # specification group
>>> skrtz.category_specifications(40, group=True)
>>> # List a category's manufacturers
>>> skrtz.category_manufacturers(25)
```