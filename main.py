#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import webapp2
import jinja2
import os
import json
import random
import pickle
import string
import re
import logging
import google_users_db
from google.appengine.ext import db
from google.appengine.api import mail
from xml.dom import minidom
from google.appengine.api import users

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), 
	autoescape = True)

GoogleUser = google_users_db.GoogleUser
class MainHandler(webapp2.RequestHandler):
    def write(self, *args, **kwargs):
        self.response.out.write(*args, **kwargs)
        
    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kwargs):
        self.write(self.render_str(template, **kwargs))

class HomePage(MainHandler):
	def get(self):
		try:
			user = users.get_current_user()
			if user:
				self.redirect("/google_user_profile")
				logging.info("user %s is signed in to this app through google", user.nickname())
			else:
				logging.info("user is not signed in, loading index.html")
				self.render("index.html")
		except Exception as e:
			pass

	def post(self):
		pass

class GoogleUserProfile(MainHandler):
	def get(self):
		try:
			google_user = users.get_current_user()
			if google_user:
				user_stored = GoogleUser.init_user(str(google_user.user_id()))
				logging.info("google user id is %s", google_user.user_id())
				if user_stored:
					self.render("user_profile.html", google_user=True, google_logout_link=users.create_logout_url("/"), ids=GoogleUser.all_ids(), user_brand_new=True)
				else:
					self.render("user_profile.html", google_user=True, google_logout_link=users.create_logout_url("/"), ids=GoogleUser.all_ids(), user_brand_new=True)

		except Exception as e:
			logging.info("Exception Encountered: %s", str(e))

	def post(self):
		pass

class FacebookUserProfile(MainHandler):
	def get(self):
		try:
			self.render("user_profile.html", fb_user=True)
		except Exception as e:
			logging.info("Exception Encountered: %s", str(e))

	def post(self):
		pass

class AuthenticateGoogle(MainHandler):
	def get(self):
		try:
			user = users.get_current_user()
			if not user:
				self.redirect(users.create_login_url("/"))
			else:
				self.redirect("/google_user_profile")
		except Exception as e:
			logging.info("Exception Caught! => %s", str(e))

class AuthenticateFacebook(MainHandler):
	def get(self):
		try:
			fb_user = self.request.get("fb_user")
			if fb_user == "true":
				self.redirect("/facebook_user_profile")
			else:
				self.redirect("/")
		except Exception as e:
			logging.info("Exception Encountered: %s", str(e))


app = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/authenticate_facebook', AuthenticateFacebook),
    ('/authenticate_google', AuthenticateGoogle),
    ('/google_user_profile', GoogleUserProfile),
    ('/facebook_user_profile', FacebookUserProfile)
], debug=True)


