from django import forms

from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,
	)


User = get_user_model()

class RegisterForm(forms.ModelForm):
	email = forms.EmailField(required=True, label='Email address')
	password = forms.CharField(widget=forms.PasswordInput)
	username = forms.CharField(required=False)

	class Meta:
		model = User
		fields = [
			'username',
			'email',
			'password'
		]




	def clean(self):
		user = self.authenticate_via_email()
		if user:
			raise forms.ValidationError("Este correo electrónico ya ha sido registrado.")
		else:
			self.user = user
		return self.cleaned_data

	def authenticate_via_email(self):

		email = self.cleaned_data.get('email')
		if email:
			try:
				user = User.objects.filter(email=email)
				if user:

					return user
			except ObjectDoesNotExist:
				pass
		return None






from django.core.exceptions import ObjectDoesNotExist




class LoginForm(forms.Form):
	email = forms.CharField()
	password = forms.CharField(
		widget=forms.PasswordInput(render_value=False)
		)
	keep_logged = forms.BooleanField(required=False, label="Keep me logged in")

	def clean(self):
		user = self.authenticate_via_email()
		if not user:
			raise forms.ValidationError("Usuario o contraseña invalido. Inténtalo de nuevo.")
		else:
			self.user = user
		return self.cleaned_data

	def authenticate_user(self):
		return authenticate(
			username=self.user.username,
			password=self.cleaned_data['password'])

	def authenticate_via_email(self):
		"""
			Authenticate user using email.
			Returns user object if authenticated else None
		"""
		email = self.cleaned_data['email']
		if email:
			try:
				user = User.objects.get(email__iexact=email)
				if user.check_password(self.cleaned_data['password']):
					return user
			except ObjectDoesNotExist:
				pass
		return None


'''
class LoginForm(forms.Form):
	email = forms.EmailField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput)
	keep_logged = forms.BooleanField(required=False, label="Keep me logged in")


	def authenticate_via_email(self):

		email = self.cleaned_data['email']
		if email:
			try:
				user = User.objects.get(email__iexact=email)
				if user.check_password(self.cleaned_data['password']):
					return user
			except ObjectDoesNotExist:
				pass
		return None

'''
