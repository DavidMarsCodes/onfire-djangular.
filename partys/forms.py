from django import forms


class PartyForm(forms.ModelForm):

	class Meta:
		model = User
		fields = [
			'name',
			'description',
			'place',
			'address',
			'location',
			'event_date',
			'time',
			'category',
		]

