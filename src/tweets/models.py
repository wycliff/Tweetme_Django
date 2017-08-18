from django.db import models
from django.conf import settings # associating with user model 
from django.core.exceptions import ValidationError

from .validators import validate_content


# Create your models here.
class Tweet(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1) #id of 1.  Associating with the user.
	content	= models.CharField(max_length = 140 , validators=[validate_content]) 
	updated = models.DateTimeField(auto_now = True) # Read a little mor eof the documentation. 
	timestamp = models.DateTimeField(auto_now_add = True)  
		
	def __str__(self):
		return str(self.id) 


	#===========you can add validation right in the model (inline validation) not specifically for a field though 
	# def clean(self, *args, **kwargs):
	# 	content = self.content
	# 	if content == "abc":
	# 		raise ValidationError("Content cannot be ABC")
	# 	return super(Tweet , self).clean(*args, **kwargs)




 