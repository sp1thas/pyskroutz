# Category Docs: https://developer.skroutz.gr/api/v3/category/

# List all categories
print skrtz.categories()

# Retrieve a single category
print skrtz.category(1442)

# Retrieve the parent of a category: 
print skrtz.category_parent(1442)

# Retrieve the root category
print skrtz.category_root(1442)

# List the children categories of a category
print skrtz.category_children(252)

# List a category's specifications
print skrtz.category_specifications(40)

# specification group
print skrtz.category_specifications(40, group=True)

# List a category's manufacturers
print skrtz.category_manufacturers(25)
