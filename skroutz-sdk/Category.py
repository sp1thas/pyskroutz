#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Category.py
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

  def all(self):
    req = requests.get('http://api.skroutz.gr/categories', headers=self.headers)
    return req.json()
  
  def __init__(self, category_id=None):
    req = requests.get('http://api.skroutz.gr/categories/%s' % str(category_id), headers=self.headers)
    return req.json()

  def parent(self, category_id=None):
    req = requests.get('http://api.skroutz.gr/categories/%s/parent' % str(category_id), headers=self.headers)
    return req.json()

  def root(self, category_id=None):
    req = requests.get('http://api.skroutz.gr/categories/root', headers=self.headers)
    return req.json()

  def childrens(self, category_id=None):
    req = requests.get('http://api.skroutz.gr/categories/%s/children' % str(category_id), headers=self.headers)
    return req.json()
