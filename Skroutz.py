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
import Category
import 

class Skroutz(Category.Skroutz):
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


