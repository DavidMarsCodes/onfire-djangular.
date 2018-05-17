from rest_framework.authtoken.models import Token
from rest_framework import serializers
from rest_framework.serializers import (
	CharField,
	EmailField,
	HyperlinkedIdentityField,
	ModelSerializer,
	SerializerMethodField,
	ValidationError,    
	EmailField,
	CharField,
	TimeField,
	ValidationError
)
from django.db.models import Q

from django.contrib.auth import (
	authenticate,
	get_user_model,
	login as login_auth,
	logout as logout_auth,

	)



from accounts.api.serializers import UsuarioSerializer

from partys.models import Party

User = get_user_model()


class PartySerializer(ModelSerializer):
	class Meta:
		model = Party
		fields = ('id','username','email')


class PartyCreateUpdateSerializer(ModelSerializer):
	# email = EmailField(label = 'Email')
	#email2 = EmailField(label = 'Confirm Email')
	event_date  = serializers.DateField(format="%d-%m-%Y")
	time  = serializers.TimeField(format="%H:%M")
	class Meta: 
		model = Party
		fields = [
			'name',
			'description',
			'location',
			'address',
			'place',
			'user',
			'category',
			'createdAt',
			'event_date',
			'time'


		]


class PartyListSerializer(ModelSerializer):
	user = UsuarioSerializer()
	createdAt = serializers.DateTimeField(format="%d-%m-%Y a las %H:%M")
	#event_date  = serializers.DateField(format="%d-%m-%Y")
	time  = serializers.TimeField(format="%H:%M Hrs")

	class Meta: 
		model = Party
		fields = [
			'id',
			'name',
			'description',
			'status',
			'location',
			'user',
			'place',
			'category',
			'createdAt',
			'event_date',
			'time',
			'updatedAt',

		]




class PartyDetailSerializer(ModelSerializer):
	class Meta:
		model = Party
		fields = [
			'id',
			'name',

		]

