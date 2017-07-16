#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  untitled.py
#
#  Copyright 2017 Simakis Panagiotis <spithas@yoga-deb>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

import requests


class Skroutz():
  BASE_URL = 'http://api.skroutz.gr/api/'

  def __init__(self, client_id=None, client_secret=None):
    if None in [client_id, client_secret]: raise TypeError('You have to give client_id and client_secret')
    self.client_id = client_id
    self.client_secret = client_secret
    req = requests.post('https://www.skroutz.gr/oauth2/token',
                data = {'client_id':self.client_id,
                    'client_secret': self.client_secret,
                    'grant_type': 'client_credentials',
                    'scope':'public'
                     }
               )
    if req.status_code == 200:
      self.access_token = req.json()['access_token']
      self.access_token_exp = req.json()['expires_in']
      self.access_token_type = req.json()['token_type']
      self.headers = {'Accept': 'application/vnd.skroutz+json; version=3', 'Authorization': '%s %s' % (self.access_token_type.capitalize(), self.access_token) }
    elif req.status_code == 401:
      raise TypeError(req.json()['error'])
    else:
      raise TypeError('Something bad happend')

  #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  #~ Category
  #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  def categories(self):
    req = requests.get('http://api.skroutz.gr/categories', headers=self.headers)
    return req.json()

  def category(self, category_id):
    req = requests.get('http://api.skroutz.gr/categories/%s' % str(category_id), headers=self.headers)
    return req.json()

  def category_parent(self, category_id):
    req = requests.get('http://api.skroutz.gr/categories/%s/parent' % str(category_id), headers=self.headers)
    return req.json()

  def category_root(self, category_id):
    req = requests.get('http://api.skroutz.gr/categories/%s/root' % str(category_id), headers=self.headers)
    return req.json()

  def category_children(self, category_id):
    req = requests.get('http://api.skroutz.gr/categories/%s/children' % str(category_id), headers=self.headers)
    return req.json()

  def category_specifications(self, category_id, group=False):
    if group: req = requests.get('http://api.skroutz.gr/categories/%s/specifications?include=group' % str(category_id), headers=self.headers)
    else: req = requests.get('http://api.skroutz.gr/categories/%s/specifications' % str(category_id), headers=self.headers)
    return req.json()

  def category_manufacturers(self, category_id, group=False):
    req = requests.get('http://api.skroutz.gr/categories/%s/manufacturers' % str(category_id), headers=self.headers)
    return req.json()

  def category_favorites(self,category_id):
    req = requests.get('http://api.skroutz.gr/categories/%s/favorites' % str(category_id), headers=self.headers)
    return req.json()

  #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  #~ SKU
  #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  def sku_category(self, category_id, q=None, manufacturer_ids=[], filter_ids=None):
    if manufacturer_ids:
      url = 'http://api.skroutz.gr/categories/%s/skus?manufacturer_ids[]=%s' % (category_id, '&manufacturer_ids[]='.join(manufacturer_ids))
    if q is not None: 'http://api.skroutz.gr/categories/40/skus?q=%s' % q
    if filter_ids:
      url = 'http://api.skroutz.gr/categories/%s/skus?filter_ids[]=%s' % (category_id, '&filter_ids[]='.join(filter_ids))
    req = requests.get(url, headers=self.headers)
    return req.json()

  def sku(self, id, sku_rating_breakdown=False, sku_reviews_aggregation=False):
    if sku_rating_breakdown: req = requests.get('http://api.skroutz.gr/skus/%s?include_meta=sku_rating_breakdown' % str(id), headers=self.headers)
    elif sku_rating_breakdown: req = requests.get('http://api.skroutz.gr/skus/%s?include_meta=sku_reviews_aggregation' % str(id), headers=self.headers)
    else: req = requests.get('http://api.skroutz.gr/skus/%s' % str(id), headers=self.headers)
    return req.json()

  def sku_similar(self, id, sku_rating_breakdown=False, sku_reviews_aggregation=False):
    if sku_rating_breakdown: req = requests.get('http://api.skroutz.gr/skus/%s/similar?include_meta=sku_rating_breakdown' % str(id), headers=self.headers)
    elif sku_reviews_aggregation: req = requests.get('http://api.skroutz.gr/skus/%s/similar?include_meta=sku_reviews_aggregation' % str(id), headers=self.headers)
    else: req = requests.get('http://api.skroutz.gr/skus/%s/similar' % str(id), headers=self.headers)
    return req.json()

  def sku_products(self, id, sku_rating_breakdown=False, sku_reviews_aggregation=False):
    if sku_rating_breakdown: req = requests.get('http://api.skroutz.gr/skus/%s/products?include_meta=sku_rating_breakdown' % str(id), headers=self.headers)
    elif sku_reviews_aggregation: req = requests.get('http://api.skroutz.gr/skus/%s/products?include_meta=sku_reviews_aggregation' % str(id), headers=self.headers)
    else: req = requests.get('http://api.skroutz.gr/skus/%s/products' % str(id), headers=self.headers)
    return req.json()

  def sku_reviews(self, id, sku_rating_breakdown=False, sku_reviews_aggregation=False):
    if sku_rating_breakdown: req = requests.get('http://api.skroutz.gr/skus/%s/reviews?include_meta=sku_rating_breakdown' % str(id), headers=self.headers)
    elif sku_reviews_aggregation: req = requests.get('http://api.skroutz.gr/skus/%s/reviews?include_meta=sku_reviews_aggregation' % str(id), headers=self.headers) 
    req = requests.get('http://api.skroutz.gr/skus/%s/reviews' % id, headers=self.headers)
    return req.json()
  
  def sku_vote_review(self, sku_id=None, review_id=None, helpful=None):
    pass
  
  def sku_review_votes(self, sku_id=None, review_id=None):
    req = requests.post('http://api.skroutz.gr/skus/%s/reviews/%s/votes' % (str(sku_id), str(review_id)), headers=self.headers)
    return req.json()
  
  def sku_specifications(self, id, group=False):
    if group: req = requests.get('http://api.skroutz.gr/skus/%s/specifications?include=group' % str(id), headers=self.headers)
    else: req = requests.get('http://api.skroutz.gr/skus/%s/specifications' % str(id), headers=self.headers)
    return req.json()
  
  def sku_pricehistory(self, id):
    req = requests.get('http://api.skroutz.gr/skus/%s/price_history' % str(id), headers=self.headers)
    return req.json()
  
  def sku_favorite(self, id):
    req = requests.get('http://api.skroutz.gr/skus/%s/favorite' % str(id), headers=self.headers)
    return req.json()
    
  #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  #~ Product
  #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  
  def product_single(self, id):
    req = requests.get('http://api.skroutz.gr/products/%s' % str(id), headers=self.headers)
    return req.json()
    
  def product_search(self, shop_id=None, shop_uid=None):
    req = requests.get('http://api.skroutz.gr/shops/%s/products/search?shop_uid=%s' % (str(shop_id), str(shop_uid)), headers=self.headers)
    return req.json()

    
  #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  #~ Shop
  #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  
  def shop(self, id):
    req = requests.get('http://api.skroutz.gr/shops/%s' % str(id), headers=self.headers)
    return req.json()
  
  def shop_reviews(self, id):
    req = requests.get('http://api.skroutz.gr/%s/reviews' % str(id), headers=self.headers)
    return req.json()
    
  def shop_locations(self, id, embed_address=False):
    if not embed_address: req = requests.get('http://api.skroutz.gr/shops/%s/locations' % str(id), headers=self.headers)
    else: req = requests.get('http://api.skroutz.gr/shops/%s/locations?embed=address' % str(id), headers=self.headers)
    return req.json()
    
  def shop_location(self, shop_id=None, id=None, embed_address=False):
    if not embed_address: req = requests.get('http://api.skroutz.gr/shops/%s/locations/%s' % (str(shop_id), str(id)), headers=self.headers)
    else: req = requests.get('http://api.skroutz.gr/shops/%s/locations/%s?embed=address' % (str(shop_id), str(id)), headers=self.headers)

  def shop_search(self, q):
    req = requests.get('http://api.skroutz.gr/shops/search?q=%s' % str(q), headers=self.headers)
    return req.json()
  
  #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  #~ Manufacturer
  #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  
  def manufacturer_listall(self):
    req = requests.get('http://api.skroutz.gr/manufacturers', headers=self.headers)
    return req.json()
  
  def manufacturer(self, id):
    req = requests.get('http://api.skroutz.gr/manufacturers/%s' % str(id), headers=self.headers)
    return req.json()
    
  def manufacturer_categories(self, id, order_by=None, order_dir=None):
    if order_by: req = requests.get('http://api.skroutz.gr/manufacturers/%s/categories?order_by=%s' % (str(id), order_by), headers=self.headers)
    elif order_dir: req = requests.get('http://api.skroutz.gr/manufacturers/%s/categories?order_dir=%s' % (str(id), order_dir), headers=self.headers)
    else: req = requests.get('http://api.skroutz.gr/manufacturers/%s/categories' % str(id), headers=self.headers)
    return req.json()
  
  def manufacturer_sku(self, id, order_by=None, order_dir=None):
    if order_by: req = requests.get('http://api.skroutz.gr/manufacturers/%s/skus?order_by=%s' % (str(id), order_by), headers=self.headers)
    elif order_dir: req = requests.get('http://api.skroutz.gr/manufacturers/%s/skus?order_dir=%s' % (str(id), order_dir), headers=self.headers)
    else: req = requests.get('http://api.skroutz.gr/manufacturers/%s/skus' % str(id), headers=self.headers)
    return req.json()  
  
  #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  #~ Search
  #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  
  def search(self, q):
    req = requests.get('http://api.skroutz.gr/search?q=%s' % q.replace(' ', '+'), headers=self.headers)
    return req.json()
  
  def search_autocomplete(self, q):
    req = requests.get('http://api.skroutz.gr/autocomplete?q=%s' % q.replace(' ', '+'), headers=self.headers)
    return req.json()
  
  #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  #~ Flag
  #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  def flags(self):
    req = requests.get('http://api.skroutz.gr/flags', headers=self.headers)
    return req.json()
    
  #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  #~ User
  #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  
  def user(self):
    req = requests.get('http://api.skroutz.gr/user', headers=self.headers)
    return req.json()
  
  #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  #~ User Favorite
  #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  def user_favorite_list(self):
    req = requests.get('http://api.skroutz.gr/favorite_lists', headers=self.headers)
    return req.json()
    
  def user_favorite_create_list(self, name):
    req = requests.post('http://api.skroutz.gr/favorite_lists[name]=%s' % name.replace(' ', '+'), headers=self.headers)
    return req.json()
    
  def user_favorite_destroy_list(self, id):
    req = requests.delete('http://api.skroutz.gr/favorite_lists/%s' % str(id), headers=sself.headers)
    return req.json()
    
