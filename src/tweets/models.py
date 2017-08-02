from django.db import models
from django.conf import settings # associating with user model 

# Create your models here.
class Tweet(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1) #id of 1.  Associating with the user.
	content	= models.CharField(max_length = 140) 
	updated = models.DateTimeField(auto_now = True) # Read a little mor eof the documentation. 
	timestamp = models.DateTimeField(auto_now_add = True) 
		
	def __str__(self):
		return str(self.id) 


 