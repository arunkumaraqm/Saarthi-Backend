from rest_framework import serializers
from .models import *

class IceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Book
		fields = (
			'id',
			'name',
		)