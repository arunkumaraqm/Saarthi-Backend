from django.forms import ModelForm
from .models import *

class BookForm(ModelForm):
	class Meta:
		verbose_name = 'Book'	
		verbose_name_plural = 'Books'	
		
		model = Book 
		fields = '__all__'