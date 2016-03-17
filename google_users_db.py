from google.appengine.ext import db
import logging

class GoogleUser(db.Model):
	first_login = db.DateTimeProperty(auto_now_add=True)
	user_id = db.StringProperty(required=True)
	# first_login = db.DateTimeProperty(auto_now_add=True)
 	# user_id = db.StringProperty(required=True)

    # When the user first uses the site with their google_account
    # I will call GoogleUser.init_user(user.user_id())
    # This method will check first to see if a user is present with the id passed in
  
	@classmethod
	def init_user(cls, uid):
		if not GoogleUser.user_exists(uid):
			new_user = GoogleUser(user_id=uid)
			new_user.put()
			logging.info("user %s doesnt exist so were storing user, ok bitch", uid)
			return True
		return False
    # Check to see if the user Exists. Hashtag python comments
	@classmethod
	def user_exists(cls, user_id):
		return user_id in GoogleUser.all_ids()

    # Return a list of all user_ids
	@classmethod
	def all_ids(cls):
		return [user.user_id for user in GoogleUser.all()]


    