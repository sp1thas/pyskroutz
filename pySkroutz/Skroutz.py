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

  def category_root(self):
    req = requests.get('http://api.skroutz.gr/categories/root', headers=self.headers)
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

  def sku_category(self, category_id, q=None, manufacturer_ids=[], filter_ids=None, order_by=None, order_dir=None, include_meta=None):
    url = 'http://api.skroutz.gr/categories/%s' % str(category_id)
    if manufacturer_ids is not None: url = 'http://api.skroutz.gr/categories/%s/skus?manufacturer_ids[]=%s' % (str(category_id), '&manufacturer_ids[]='.join([str(_) for _ in manufacturer_ids]))
    if q is not None: url = 'http://api.skroutz.gr/categories/40/skus?q=%s' % q.replace(' ', '+')
    if filter_ids: url = 'http://api.skroutz.gr/categories/%s/skus?filter_ids[]=%s' % (category_id, '&filter_ids[]='.join([str(_) for _ in filter_ids]))
    if order_by: url += '?order_by=%s' % order_by
    elif order_dir: url += '?order_dir=%s' % order_dir
    if include_meta: url += '?include_meta=%s' % include_meta
    req = requests.get(url, headers=self.headers)
    return req.json()

  def sku_single(self, sku_id, sku_rating_breakdown=False, sku_reviews_aggregation=False):
    if sku_rating_breakdown: req = requests.get('http://api.skroutz.gr/skus/%s?include_meta=sku_rating_breakdown' % str(sku_id), headers=self.headers)
    elif sku_rating_breakdown: req = requests.get('http://api.skroutz.gr/skus/%s?include_meta=sku_reviews_aggregation' % str(sku_id), headers=self.headers)
    else: req = requests.get('http://api.skroutz.gr/skus/%s' % str(sku_id), headers=self.headers)
    return req.json()

  def sku_similar(self, sku_id, sku_rating_breakdown=False, sku_reviews_aggregation=False):
    if sku_rating_breakdown: req = requests.get('http://api.skroutz.gr/skus/%s/similar?include_meta=sku_rating_breakdown' % str(sku_id), headers=self.headers)
    elif sku_reviews_aggregation: req = requests.get('http://api.skroutz.gr/skus/%s/similar?include_meta=sku_reviews_aggregation' % str(sku_id), headers=self.headers)
    else: req = requests.get('http://api.skroutz.gr/skus/%s/similar' % str(sku_id), headers=self.headers)
    return req.json()

  def sku_products(self, sku_id, sku_rating_breakdown=False, sku_reviews_aggregation=False):
    if sku_rating_breakdown: req = requests.get('http://api.skroutz.gr/skus/%s/products?include_meta=sku_rating_breakdown' % str(sku_id), headers=self.headers)
    elif sku_reviews_aggregation: req = requests.get('http://api.skroutz.gr/skus/%s/products?include_meta=sku_reviews_aggregation' % str(sku_id), headers=self.headers)
    else: req = requests.get('http://api.skroutz.gr/skus/%s/products' % str(sku_id), headers=self.headers)
    return req.json()

  def sku_reviews(self, sku_id, sku_rating_breakdown=False, sku_reviews_aggregation=False):
    if sku_rating_breakdown:
      req = requests.get('http://api.skroutz.gr/skus/%s/reviews?include_meta=sku_rating_breakdown' % str(sku_id), headers=self.headers)
    elif sku_reviews_aggregation:
      req = requests.get('http://api.skroutz.gr/skus/%s/reviews?include_meta=sku_reviews_aggregation' % str(sku_id), headers=self.headers) 
    req = requests.get('http://api.skroutz.gr/skus/%s/reviews' % str(sku_id), headers=self.headers)
    return req.json()

  def sku_vote_review(self, sku_id=None, review_id=None, helpful=None):
    pass

  def sku_review_votes(self, sku_id=None, review_id=None):
    req = requests.post('http://api.skroutz.gr/skus/%s/reviews/%s/votes' % (str(sku_id), str(review_id)), headers=self.headers)
    return req.json()

  def sku_specifications(self, sku_id, group=False):
    if group: req = requests.get('http://api.skroutz.gr/skus/%s/specifications?include=group' % str(sku_id), headers=self.headers)
    else: req = requests.get('http://api.skroutz.gr/skus/%s/specifications' % str(sku_id), headers=self.headers)
    return req.json()
  
  def sku_pricehistory(self, sku_id):
    req = requests.get('http://api.skroutz.gr/skus/%s/price_history' % str(sku_id), headers=self.headers)
    return req.json()
  
  def sku_favorite(self, sku_id):
    req = requests.get('http://api.skroutz.gr/skus/%s/favorite' % str(sku_id), headers=self.headers)
    return req.json()
    
  #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  #~ Product
  #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  
  def product_single(self, pr_id):
    req = requests.get('http://api.skroutz.gr/products/%s' % str(pr_id), headers=self.headers)
    return req.json()
    
  def product_search(self, shop_id=None, shop_uid=None):
    req = requests.get('http://api.skroutz.gr/shops/%s/products/search?shop_uid=%s' % (str(shop_id), str(shop_uid)), headers=self.headers)
    return req.json()

    
  #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  #~ Shop
  #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  
  def shop(self, shop_id):
    req = requests.get('http://api.skroutz.gr/shops/%s' % str(shop_id), headers=self.headers)
    return req.json()
  
  def shop_reviews(self, shop_id):
    req = requests.get('http://api.skroutz.gr/%s/reviews' % str(shop_id), headers=self.headers)
    return req.json()
    
  def shop_locations(self, shop_id, embed_address=False):
    if not embed_address: req = requests.get('http://api.skroutz.gr/shops/%s/locations' % str(shop_id), headers=self.headers)
    else: req = requests.get('http://api.skroutz.gr/shops/%s/locations?embed=address' % str(shop_id), headers=self.headers)
    return req.json()
    
  def shop_location(self, shop_id=None, lc_id=None, embed_address=False):
    if not embed_address: req = requests.get('http://api.skroutz.gr/shops/%s/locations/%s' % (str(shop_id), str(lc_id)), headers=self.headers)
    else: req = requests.get('http://api.skroutz.gr/shops/%s/locations/%s?embed=address' % (str(shop_id), str(lc_id)), headers=self.headers)
    return req.json()

  def shop_search(self, q):
    req = requests.get('http://api.skroutz.gr/shops/search?q=%s' % str(q), headers=self.headers)
    return req.json()
  
  #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  #~ Manufacturer
  #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  
  def manufacturer_listall(self):
    req = requests.get('http://api.skroutz.gr/manufacturers', headers=self.headers)
    return req.json()
  
  def manufacturer(self, mnfct_id):
    req = requests.get('http://api.skroutz.gr/manufacturers/%s' % str(mnfct_id), headers=self.headers)
    return req.json()
    
  def manufacturer_categories(self, mnfct_id, order_by=None, order_dir=None):
    if order_by: req = requests.get('http://api.skroutz.gr/manufacturers/%s/categories?order_by=%s' % (str(mnfct_id), order_by), headers=self.headers)
    elif order_dir: req = requests.get('http://api.skroutz.gr/manufacturers/%s/categories?order_dir=%s' % (str(mnfct_id), order_dir), headers=self.headers)
    else: req = requests.get('http://api.skroutz.gr/manufacturers/%s/categories' % str(mnfct_id), headers=self.headers)
    return req.json()
  
  def manufacturer_sku(self, mnfct_id, order_by=None, order_dir=None):
    if order_by:
      req = requests.get('http://api.skroutz.gr/manufacturers/%s/skus?order_by=%s' % (str(mnfct_id), order_by), headers=self.headers)
      return req.json()
    elif order_dir:
      req = requests.get('http://api.skroutz.gr/manufacturers/%s/skus?order_dir=%s' % (str(mnfct_id), order_dir), headers=self.headers)
      return req.json()
    else:
      req = requests.get('http://api.skroutz.gr/manufacturers/%s/skus' % str(mnfct_id), headers=self.headers)
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

  def user_favorite_destroy_list(self, usr_fv_id):
    req = requests.delete('http://api.skroutz.gr/favorite_lists/%s' % str(usr_fv_id), headers=self.headers)
    return req.json()
    
