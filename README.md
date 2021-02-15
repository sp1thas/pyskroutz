<div align="center">
    <h1>pyskroutz</h1>
    <p>A Python client for <a href="https://developer.skroutz.gr/api/v3/">Skroutz API</a>.</p>
    <img src="https://github.com/sp1thas/pyskroutz/workflows/testing/badge.svg" alt="testing badge">
    <img src="https://github.com/sp1thas/pyskroutz/workflows/build/badge.svg" alt="build badge">
    <img src="https://readthedocs.org/projects/pyskroutz/badge/?version=latest" alt="docs badge">
    <a href="https://pypi.python.org/pypi/pyskroutz/">
        <img src="https://img.shields.io/pypi/v/pyskroutz.svg" alt="pypi badge" />
    </a>
    <a href="https://codecov.io/gh/sp1thas/pyskroutz">
        <img alt="code coverage badge" src="https://codecov.io/gh/sp1thas/pyskroutz/branch/master/graph/badge.svg?token=WTYZU0ENYX" />
    </a>
    <img src="https://img.shields.io/badge/code%20style-black-black">
</div>
<hr>


## Installation
```bash
pip install pyskroutz
```

## Usage

First of all, you have to initiate an client in order to interact with Skroutz API. Make sure that you have a valid pair of client id and client secret. From now on, `client` will be the following object.

```python
import pyskroutz
client = pyskroutz.client('<client-id>', '<client-secret>')
```

The `client` object will be passed as parameter in order to retrieve data from a resource's endpoint.

### Search

```python
>>> results = pyskroutz.search(client)("iphone").execute()
```
<details>
    <summary><code>results.dict()</code></summary>

```python
{'categories': [],
 'meta': {'alternatives': [],
          'pagination': {'page': 1,
                         'per': 25,
                         'total_pages': 0,
                         'total_results': 0},
          'q': None,
          'strong_matches': {'manufacturer': {'id': 356,
                                              'image_url': HttpUrl('https://a.scdn.gr/ds/manufacturers/356/20160322115406_ae6f9a87.png', scheme='https', host='a.scdn.gr', tld='gr', host_type='domain', path='/ds/manufacturers/356/20160322115406_ae6f9a87.png'),
                                              'name': 'Apple'},
                             'sku': None}}}
```
</details>

### List Categories

```python
>>> categories = pyskroutz.categories(client).get(per=3).execute()
```
<details>
    <summary><code>categories.dict()</code></summary>

```python
{'categories': [{'children_count': 5,
                 'code': 'statherh-tilefwnia',
                 'fashion': True,
                 'id': 1,
                 'image_url': HttpUrl('https://c.scdn.gr/ds/categories/1/20171113120915_72fa0f63.jpeg', scheme='https', host='c.scdn.gr', tld='gr', host_type='domain', path='/ds/categories/1/20171113120915_72fa0f63.jpeg'),
                 'layout_mode': 'tiles',
                 'manufacturer_title': 'Κατασκευαστές',
                 'name': 'Σταθερή Τηλεφωνία',
                 'parent_id': 2,
                 'path': '76,1269,2,1',
                 'show_specifications': False,
                 'web_uri': HttpUrl('https://skroutz.gr/c/1/statherh-tilefwnia.html', scheme='https', host='skroutz.gr', tld='gr', host_type='domain', path='/c/1/statherh-tilefwnia.html')},
                {'children_count': 2,
                 'code': 'tilefwnia',
                 'fashion': True,
                 'id': 2,
                 'image_url': HttpUrl('https://b.scdn.gr/ds/categories/2/20171113120916_9d335c35.jpeg', scheme='https', host='b.scdn.gr', tld='gr', host_type='domain', path='/ds/categories/2/20171113120916_9d335c35.jpeg'),
                 'layout_mode': 'tiles',
                 'manufacturer_title': 'Κατασκευαστές',
                 'name': 'Τηλεφωνία',
                 'parent_id': 1269,
                 'path': '76,1269,2',
                 'show_specifications': False,
                 'web_uri': HttpUrl('https://skroutz.gr/c/2/tilefwnia.html', scheme='https', host='skroutz.gr', tld='gr', host_type='domain', path='/c/2/tilefwnia.html')},
                {'children_count': 4,
                 'code': 'photografia-video',
                 'fashion': True,
                 'id': 5,
                 'image_url': HttpUrl('https://b.scdn.gr/ds/categories/5/20171113120916_dfd75306.jpeg', scheme='https', host='b.scdn.gr', tld='gr', host_type='domain', path='/ds/categories/5/20171113120916_dfd75306.jpeg'),
                 'layout_mode': 'tiles',
                 'manufacturer_title': 'Κατασκευαστές',
                 'name': 'Φωτογραφία & Video',
                 'parent_id': 1269,
                 'path': '76,1269,5',
                 'show_specifications': False,
                 'web_uri': HttpUrl('https://skroutz.gr/c/5/photografia-video.html', scheme='https', host='skroutz.gr', tld='gr', host_type='domain', path='/c/5/photografia-video.html')}],
 'meta': {'available_filters': None,
          'order_by': None,
          'order_by_methods': None,
          'pagination': {'page': 1,
                         'per': 3,
                         'total_pages': 1246,
                         'total_results': 3738},
          'personalization': None,
          'sku_rating_breakdown': None,
          'sku_reviews_aggregation': None}}
```
</details>

### Retrieve a book

```python
>>> book = pyskroutz.books(client).get(242327).execute()
```
<details>
    <summary><code>book.dict()</code></summary>

```python
{'book': {'id': 242327,
          'images': {'alternatives': None,
                     'main': HttpUrl('https://b.scdn.gr/images/sku_main_images/000242/242327/medium_20200219102603_o_chari_poter_kai_i_filosofiki_lithos.jpeg', scheme='https', host='b.scdn.gr', tld='gr', host_type='domain', path='/images/sku_main_images/000242/242327/medium_20200219102603_o_chari_poter_kai_i_filosofiki_lithos.jpeg')},
          'main_author': 'J. K. Rowling',
          'main_author_id': 385,
          'name': 'Ο Χάρι Πότερ και η φιλοσοφική λίθος',
          'price_max': 12.96,
          'price_min': 6.61,
          'reviewable': True,
          'reviews_count': 13,
          'reviewscore': 5.0,
          'shop_count': 42,
          'web_uri': HttpUrl('https://www.skroutz.gr/books/242327.%CE%9F-%CE%A7%CE%AC%CF%81%CE%B9-%CE%A0%CF%8C%CF%84%CE%B5%CF%81-%CE%BA%CE%B1%CE%B9-%CE%B7-%CF%86%CE%B9%CE%BB%CE%BF%CF%83%CE%BF%CF%86%CE%B9%CE%BA%CE%AE-%CE%BB%CE%AF%CE%B8%CE%BF%CF%82.html', scheme='https', host='www.skroutz.gr', tld='gr', host_type='domain', path='/books/242327.%CE%9F-%CE%A7%CE%AC%CF%81%CE%B9-%CE%A0%CF%8C%CF%84%CE%B5%CF%81-%CE%BA%CE%B1%CE%B9-%CE%B7-%CF%86%CE%B9%CE%BB%CE%BF%CF%83%CE%BF%CF%86%CE%B9%CE%BA%CE%AE-%CE%BB%CE%AF%CE%B8%CE%BF%CF%82.html')}}
```
</details>

For further usage details navigate to [API Documentation](https://pyskroutz.readthedocs.io/en/latest/). Almost every endpoint of Skroutz API is supported by this client.

## How to contribute

If you wish to contribute, check out the [CONTRIBUTING.md](docs/contributing.md) guide for further details.
