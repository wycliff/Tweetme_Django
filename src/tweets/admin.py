from django.contrib import admin

# Register your models here.
# Create admin forms as well

#the first 
from .models import Tweet
from .forms import TweetModelForm

admin.site.register(Tweet) 


#django admin inline model 
class TweetModelAdmin(admin.ModelAdmin):
	# form = TweetModelForm
	class Meta:
		model = Tweet
		
# admin.site.unregister(Tweet)	#bug fix   	
# admin.site.register(Tweet, TweetModelAdmin)  # giving an error		
