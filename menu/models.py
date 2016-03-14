from django.db import models

# Create your models here.

class Restaurant(models.Model):
	name = models.CharField(max_length = 20,verbose_name = 'Restaurant Name')
	phone_number = models.CharField(max_length = 15,verbose_name = 'Phone Number')
	address = models.CharField(max_length=50,blank = True,verbose_name='Restaurant Address')

	def __unicode__(self):
		return self.name

class Food(models.Model):
	name = models.CharField(max_length = 30,verbose_name = 'Dish Name')
	price = models.DecimalField(max_digits = 3,decimal_places = 0,verbose_name ='Price')
	comment = models.CharField(max_length = 70,blank = True,verbose_name = 'Leave a comment')
	is_spicy = models.BooleanField(default = False,verbose_name = 'Is it spicy')
	restaurant = models.ForeignKey(Restaurant)
	image = models.CharField(max_length = 150, default = 'none.jpgs',verbose_name = 'Image Name')

	def __unicode__(self):
		return self.name