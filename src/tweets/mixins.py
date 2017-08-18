from django import forms
from django.forms.utils import ErrorList



class FormUserNeededMixin(object):
	def form_valid(self, form):
		if self.request.user.is_authenticated(): # dont allow submit if user is not authenticated.
			form.instance.user = self.request.user
			return super(FormUserNeededMixin, self).form_valid(form)
		else:
			form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["User must be logged in to continue"]) # confirm login status of the user 
			return self.form_invalid(form)


# ===== Prevents a certain user from altering details entered by other user
class UserOwnerMixin(FormUserNeededMixin,object):
	def form_valid(self, form):
		if form.instance.user == self.request.user:    # this cond checked first before that of FormUserNeededMixin
			return super(FormUserNeededMixin, self).form_valid(form)

		else:
			form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["This user is not allowed to change this <data>	</data>"]) # confirm login status of the user 
			return self.form_invalid(form)
		

