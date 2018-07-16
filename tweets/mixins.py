from django import forms
from django.forms.utils import ErrorList

# mixin to supply user to tweet if logged in
class FormUserNeededMixin(object):
	def form_valid(self, form):
		if(self.request.user.is_authenticated):
			form.instance.user = self.request.user
			return super(FormUserNeededMixin, self).form_valid(form)
		else:
			form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["User must be logged in to continue."])
			return self.form_invalid(form)

class UserMixin(object):
	def form_valid(self, form):
		if(form.instance.user == self.request.user):
			return super(UserMixin, self).form_valid(form)
		else:
			form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["This user is not allowed to change this data. Original User must be logged in."])
			return self.form_invalid(form)