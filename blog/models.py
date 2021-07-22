from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


# create class post inherited from models.Model
# each class is going to be its own table in the database
# each attribute will be a different field in the database
class Post(models.Model):  
	title = models.CharField(max_length = 100)
	content = models.TextField()
	date_posted = models.DateTimeField(default = timezone.now) # remeber we have not put () after timezone.now, 
	author = models.ForeignKey(User, on_delete = models.CASCADE)# we are not passing function, we are just passing reference

	def __str__(self):
		return self.title
	#If you do not provide a success_url attribute and a custom get_success_url method on the view class, 
	#Django will try to get the URL to redirect from
	#the get_absolute_url method on the newly created object if the method is defined in the model class. 
	def get_absolute_url(self):
		return reverse('post-detail', kwargs = {'pk': self.pk})
