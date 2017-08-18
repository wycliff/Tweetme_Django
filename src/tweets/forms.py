from django import forms
from .models import Tweet


#This creates a form in the admin for you to dd tweets into the Tweet model for the Tweet app 
class TweetModelForm(forms.ModelForm):
	class Meta:
		model = Tweet
		fields = [

             #"user",  # these ar inbuilt form fields : see documentations
             "content"
		]
		#exclude['user']


	#====================Basic form validation  - not working needs a fix/ but alteernatives are used =======				
	# def clean_user(self, *args, **kwargs):
	# 	content = self.cleaned_data.get("content")
	# 	if content == "abcde":
	# 		raise forms.ValidationError("Cannot be ABC") #inbuilt exception 
	# 	return content