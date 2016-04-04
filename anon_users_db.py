from google.appengine.ext import db
import logging

class AnonUser(db.Model):
	first_login = db.DateTimeProperty(auto_now_add=True)
	user_id = db.StringProperty(required=True)
	# first_login = db.DateTimeProperty(auto_now_add=True)
 	# user_ip = db.StringProperty(required=True)
  
	@classmethod
	def init_user(cls, uid):
		if not AnonUser.user_exists(uid):
			new_user = AnonUser(user_id=uid)
			new_user.put()
			logging.info("user %s doesnt exist so were storing user, ok bitch", uid)
			return True
		return False
    # Check to see if the user Exists. Hashtag python comments
	@classmethod
	def user_exists(cls, user_id):
		return user_id in AnonUser.all_ids()

    # Return a list of all user_ids
	@classmethod
	def all_ids(cls):
		return [user.user_id for user in AnonUser.all()]